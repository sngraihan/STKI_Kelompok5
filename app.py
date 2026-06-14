import pickle
import re
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

st.set_page_config(page_title="STKI - Pencarian Lirik Lagu", page_icon="🎵", layout="wide")

# Load model
@st.cache_resource
def load_models():
    tfidf = pickle.load(open('models/tfidf_vectorizer.pkl', 'rb'))
    tfidf_matrix = pickle.load(open('models/tfidf_matrix.pkl', 'rb'))
    bm25 = pickle.load(open('models/bm25_model.pkl', 'rb'))
    df = pd.read_pickle('models/df_processed.pkl')
    return tfidf, tfidf_matrix, bm25, df

tfidf, tfidf_matrix, bm25, df = load_models()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words and len(t) > 1]
    return ' '.join(tokens)

def search_tfidf(query, top_k=5):
    q_vec = tfidf.transform([preprocess(query)])
    scores = cosine_similarity(q_vec, tfidf_matrix).flatten()
    top_idx = scores.argsort()[-top_k:][::-1]
    return [{'rank': r+1, 'judul': df.iloc[i]['judul'], 'penyanyi': df.iloc[i]['penyanyi'],
             'score': round(float(scores[i]), 4), 'lirik': df.iloc[i]['lirik'][:300]}
            for r, i in enumerate(top_idx)]

def search_bm25(query, top_k=5):
    q_tokens = preprocess(query).split()
    scores = bm25.get_scores(q_tokens)
    top_idx = scores.argsort()[-top_k:][::-1]
    return [{'rank': r+1, 'judul': df.iloc[i]['judul'], 'penyanyi': df.iloc[i]['penyanyi'],
             'score': round(float(scores[i]), 4), 'lirik': df.iloc[i]['lirik'][:300]}
            for r, i in enumerate(top_idx)]

# Sidebar
st.sidebar.title("🎵 STKI Kelompok 5")
st.sidebar.caption("Sistem Temu Kembali Informasi")
st.sidebar.markdown("---")
st.sidebar.markdown(f"**Dataset:** {len(df):,} lagu")
st.sidebar.markdown(f"**Fitur TF-IDF:** {tfidf_matrix.shape[1]:,}")
st.sidebar.markdown(f"**Model:** TF-IDF & BM25")

tab1, tab2 = st.tabs(["🔍 Pencarian", "📊 Evaluasi"])

# ── TAB PENCARIAN ──
with tab1:
    st.title("Pencarian Lirik Lagu")
    st.caption("Masukkan potongan lirik atau kata kunci untuk mencari lagu.")

    query = st.text_input("Query:", placeholder="contoh: darling hold my hand")

    if query:
        preprocessed = preprocess(query)
        st.caption(f"Hasil preprocessing: `{preprocessed}`")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("TF-IDF + Cosine Similarity")
            results_tfidf = search_tfidf(query)
            for r in results_tfidf:
                with st.expander(f"#{r['rank']} {r['judul']} — {r['penyanyi']} ({r['score']})"):
                    st.code(r['lirik'], language=None)

        with col2:
            st.subheader("BM25 (Okapi)")
            results_bm25 = search_bm25(query)
            for r in results_bm25:
                with st.expander(f"#{r['rank']} {r['judul']} — {r['penyanyi']} ({r['score']})"):
                    st.code(r['lirik'], language=None)

# ── TAB EVALUASI ──
with tab2:
    st.title("Evaluasi Performa Sistem")
    st.caption("Membandingkan TF-IDF vs BM25 menggunakan 10 query uji dengan ground truth.")

    # Buat ground truth dari dataset
    @st.cache_data
    def build_ground_truth():
        gt_songs = df.sample(10, random_state=99).reset_index(drop=True)
        queries = []
        for _, row in gt_songs.iterrows():
            words = row['lirik'].split()
            start = len(words) // 3
            snippet = ' '.join(words[start:start + 20])
            queries.append({'query': snippet, 'ground_truth': row['judul']})
        return queries

    test_queries = build_ground_truth()

    st.subheader("Ground Truth (10 Query Uji)")
    gt_df = pd.DataFrame(test_queries)
    gt_df.index = gt_df.index + 1
    st.dataframe(gt_df, use_container_width=True)

    if st.button("🚀 Jalankan Evaluasi", use_container_width=True):
        def evaluate(search_fn, queries):
            rows = []
            total_ap = 0.0
            for i, tq in enumerate(queries):
                results = search_fn(tq['query'], top_k=3)
                titles = [r['judul'].lower().strip() for r in results]
                gt = tq['ground_truth'].lower().strip()

                p1 = 1 if titles and gt == titles[0] else 0
                rel = sum(1 for t in titles if gt == t)
                p3 = rel / 3.0
                r3 = 1 if gt in titles else 0

                ap = 0.0
                for rank, t in enumerate(titles):
                    if gt == t:
                        ap = 1.0 / (rank + 1)
                        break
                total_ap += ap

                ret_str = ' | '.join([f"#{r['rank']} {r['judul']} ({r['score']})" for r in results])
                rows.append({
                    'No': i + 1, 'Query': tq['query'][:60] + '...',
                    'Ground Truth': tq['ground_truth'], 'Hasil Retrieval': ret_str,
                    'P@1': p1, 'P@3': round(p3, 2), 'Recall@3': r3, 'AP': round(ap, 2)
                })
            return rows, total_ap / len(queries)

        with st.spinner("Menghitung metrik..."):
            tfidf_rows, tfidf_map = evaluate(search_tfidf, test_queries)
            bm25_rows, bm25_map = evaluate(search_bm25, test_queries)

        st.subheader("Hasil TF-IDF")
        st.dataframe(pd.DataFrame(tfidf_rows), use_container_width=True)

        st.subheader("Hasil BM25")
        st.dataframe(pd.DataFrame(bm25_rows), use_container_width=True)

        st.markdown("---")
        st.subheader("Ringkasan Performa")

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("MAP TF-IDF", f"{tfidf_map:.0%}")
        c2.metric("MAP BM25", f"{bm25_map:.0%}")
        c3.metric("P@1 TF-IDF", f"{np.mean([r['P@1'] for r in tfidf_rows]):.0%}")
        c4.metric("P@1 BM25", f"{np.mean([r['P@1'] for r in bm25_rows]):.0%}")

        best = "BM25" if bm25_map > tfidf_map else "TF-IDF"
        st.success(f"Model terbaik: **{best}**")

        # Grafik perbandingan
        st.subheader("Grafik Perbandingan")
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        labels = ['MAP', 'P@1', 'P@3', 'Recall@3']
        tfidf_vals = [tfidf_map, np.mean([r['P@1'] for r in tfidf_rows]),
                      np.mean([r['P@3'] for r in tfidf_rows]),
                      np.mean([r['Recall@3'] for r in tfidf_rows])]
        bm25_vals = [bm25_map, np.mean([r['P@1'] for r in bm25_rows]),
                     np.mean([r['P@3'] for r in bm25_rows]),
                     np.mean([r['Recall@3'] for r in bm25_rows])]

        x = np.arange(len(labels))
        axes[0].bar(x - 0.17, tfidf_vals, 0.34, label='TF-IDF', color='steelblue')
        axes[0].bar(x + 0.17, bm25_vals, 0.34, label='BM25', color='coral')
        axes[0].set_xticks(x)
        axes[0].set_xticklabels(labels)
        axes[0].set_ylim(0, 1.15)
        axes[0].set_title('Perbandingan Metrik')
        axes[0].legend()
        for i, (tv, bv) in enumerate(zip(tfidf_vals, bm25_vals)):
            axes[0].text(i - 0.17, tv + 0.03, f'{tv:.0%}', ha='center', fontsize=8)
            axes[0].text(i + 0.17, bv + 0.03, f'{bv:.0%}', ha='center', fontsize=8)

        q_idx = range(len(test_queries))
        axes[1].bar([i - 0.15 for i in q_idx], [r['P@1'] for r in tfidf_rows], 0.3, label='TF-IDF', color='steelblue')
        axes[1].bar([i + 0.15 for i in q_idx], [r['P@1'] for r in bm25_rows], 0.3, label='BM25', color='coral')
        axes[1].set_xlabel('Query ke-')
        axes[1].set_ylabel('P@1')
        axes[1].set_title('Precision@1 per Query')
        axes[1].set_xticks(q_idx)
        axes[1].set_xticklabels([str(i+1) for i in q_idx])
        axes[1].legend()

        plt.tight_layout()
        st.pyplot(fig)
