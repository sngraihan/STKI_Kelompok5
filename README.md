# 🎵 SISTEM TEMU KEMBALI INFORMASI PADA PENCARIAN LIRIK LAGU MENGGUNAKAN METODE *TF-IDF* DAN *BM25*

## 📖 Deskripsi Proyek

Proyek ini merupakan implementasi Sistem Temu Kembali Informasi (*Information Retrieval System*) yang digunakan untuk mencari lagu berdasarkan potongan lirik yang dimasukkan oleh pengguna. Sistem memanfaatkan metode *Term Frequency-Inverse Document Frequency* (*TF-IDF*) dan *Best Matching 25* (*BM25*) untuk menghitung tingkat relevansi antara *query* dan dokumen lirik lagu.

Pengguna dapat memasukkan sebagian lirik lagu yang diingat, kemudian sistem akan menampilkan daftar lagu yang paling relevan berdasarkan skor kemiripan yang dihasilkan oleh metode *TF-IDF* dan *BM25*. Aplikasi dikembangkan menggunakan Python dan Streamlit sehingga dapat diakses melalui antarmuka web yang interaktif dan mudah digunakan.

---

## 🌐 Demo Aplikasi

**Live Demo:**

🔗 https://sngraihan-stki-kelompok5-app-hore3h.streamlit.app/

---

## 🎯 Tujuan Proyek

- Membangun Sistem Temu Kembali Informasi untuk pencarian lirik lagu.
- Mengimplementasikan metode *TF-IDF* dan *BM25* dalam proses pencarian dokumen.
- Membandingkan performa kedua metode dalam menemukan dokumen yang relevan.
- Mengevaluasi performa sistem menggunakan metrik *Precision@1*, *Precision@3*, *Recall@3*, dan *Mean Average Precision* (*MAP*).

---

## 📂 Dataset

Dataset yang digunakan berasal dari **Spotify Songs Dataset** yang diperoleh dari Kaggle.

Dataset memuat informasi berupa:

- Judul Lagu
- Nama Penyanyi
- Genre
- Lirik Lagu

Dataset awal terdiri dari **551.443 lagu**, kemudian dilakukan proses penyaringan sehingga diperoleh **525.391 lagu** yang memenuhi kriteria. Penelitian ini menggunakan sampel sebanyak **50.000 dokumen lirik lagu** untuk proses pembangunan dan evaluasi sistem.

---

## ⚙️ Metode yang Digunakan

### 1. *Text Preprocessing*

Tahapan *preprocessing* yang diterapkan meliputi:

- *Case Folding*
- *Cleaning*
- *Tokenization*
- *Stopword Removal*

### 2. *TF-IDF*

Metode *Term Frequency-Inverse Document Frequency* (*TF-IDF*) digunakan untuk menghitung bobot setiap kata berdasarkan frekuensi kemunculannya dalam dokumen dan seluruh koleksi dokumen.

### 3. *Cosine Similarity*

*Cosine Similarity* digunakan untuk menghitung tingkat kemiripan antara *query* dan dokumen yang telah direpresentasikan dalam bentuk vektor *TF-IDF*.

### 4. *BM25*

*Best Matching 25* (*BM25*) merupakan model temu kembali informasi berbasis probabilistik yang mempertimbangkan frekuensi term dan panjang dokumen dalam proses pemeringkatan hasil pencarian.

---

## 🔄 Alur Sistem

```text
Dataset Spotify Songs
          ↓
   Text Preprocessing
          ↓
       Indexing
          ↓
 TF-IDF dan BM25
          ↓
   Query Pengguna
          ↓
 Perhitungan Relevansi
          ↓
  Ranking Dokumen
          ↓
 Evaluasi Sistem
```

---

## 📊 Evaluasi Sistem

Evaluasi sistem dilakukan menggunakan beberapa metrik, yaitu:

- *Precision@1*
- *Precision@3*
- *Recall@3*
- *Mean Average Precision (MAP)*

### Hasil Evaluasi

| Metrik | TF-IDF | BM25 |
|---------|---------|---------|
| MAP | 95% | 100% |
| Precision@1 | 90% | 100% |
| Precision@3 | 33% | 33% |
| Recall@3 | 100% | 100% |

Hasil pengujian menunjukkan bahwa metode **BM25** memberikan performa yang lebih baik dibandingkan metode **TF-IDF**, terutama pada metrik *MAP* dan *Precision@1*.

---

## 🛠 Teknologi yang Digunakan

- Python
- Streamlit
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Rank-BM25
- Matplotlib
- WordCloud

---

## 🚀 Menjalankan Proyek Secara Lokal

### Clone Repository

```bash
git clone https://github.com/username/repository-name.git
```

### Masuk ke Folder Proyek

```bash
cd repository-name
```

### Install Dependency

```bash
pip install -r requirements.txt
```

### Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan berjalan pada:

```text
http://localhost:8501
```

---

## 👥 Tim Pengembang

Proyek ini dikembangkan oleh Kelompok 5 pada Mata Kuliah Sistem Temu Kembali Informasi.

| Nama | NPM | Kelas |
|--------|--------|--------|
| Elena Oktaviani | 2317051056 | C |
| Sofia' Azahra | 2317051075 | A |
| Amala Ratri Nugraheni | 2317051007 | A |
| Raihan Andi Saungnaga | 2317051058 | D |
| Achmad Ghalib Hafizh | 2317051023 | C |

---

## 🎓 Mata Kuliah

**Sistem Temu Kembali Informasi**

Program Studi Teknik Informatika  
Fakultas Matematika dan Ilmu Pengetahuan Alam  
Universitas Lampung

---

## 📄 Keterangan

Proyek ini merupakan hasil pengerjaan Proyek Akhir yang disusun untuk memenuhi salah satu persyaratan Ujian Akhir Semester (UAS) pada Mata Kuliah Sistem Temu Kembali Informasi, Program Studi Teknik Informatika, Fakultas Matematika dan Ilmu Pengetahuan Alam, Universitas Lampung.

Proyek ini dibuat untuk tujuan akademik, pembelajaran, dan pengembangan pengetahuan di bidang Sistem Temu Kembali Informasi.
