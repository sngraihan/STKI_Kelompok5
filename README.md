# 🎵 LyrikMatch

### Smart Lyrics Search Engine menggunakan TF-IDF dan BM25

LyrikMatch merupakan aplikasi pencarian lirik lagu berbasis Sistem Temu Kembali Informasi (*Information Retrieval System*) yang memungkinkan pengguna menemukan lagu hanya dengan memasukkan potongan lirik yang diingat. Sistem memanfaatkan metode *Term Frequency-Inverse Document Frequency* (*TF-IDF*) dan *Best Matching 25* (*BM25*) untuk menghitung tingkat relevansi antara *query* dan dokumen lirik lagu sehingga menghasilkan pencarian yang akurat dan relevan.

---

## 🌐 Demo Aplikasi

🔗 **Live Demo**  
https://sngraihan-stki-kelompok5-app-hore3h.streamlit.app/

---

## 📖 Deskripsi Proyek

Banyak pengguna sering kali hanya mengingat sebagian lirik lagu tanpa mengetahui judul maupun penyanyinya. LyrikMatch dikembangkan untuk membantu pengguna menemukan lagu berdasarkan potongan lirik yang dimasukkan. Sistem melakukan proses pencarian menggunakan metode TF-IDF dan BM25 untuk menghitung relevansi antara *query* dan koleksi dokumen lirik lagu.

---

## 🎯 Tujuan Proyek

- Membangun sistem pencarian lirik lagu berbasis Sistem Temu Kembali Informasi.
- Mengimplementasikan metode TF-IDF dan BM25 dalam proses pencarian dokumen.
- Membandingkan performa kedua metode dalam menemukan dokumen yang relevan.
- Mengevaluasi performa sistem menggunakan metrik evaluasi standar.

---

## 📂 Dataset

Dataset yang digunakan berasal dari **Spotify Songs Dataset** yang berisi informasi lagu dari berbagai genre musik.

Atribut yang digunakan dalam penelitian meliputi:

- Judul Lagu
- Nama Penyanyi
- Genre
- Lirik Lagu

Dataset awal terdiri dari **551.443 lagu**, kemudian dilakukan proses penyaringan sehingga diperoleh **525.391 lagu** yang memenuhi kriteria penelitian. Sistem menggunakan **50.000 dokumen lirik lagu** sebagai sampel untuk proses pembangunan dan evaluasi.

---

## ⚙️ Metode yang Digunakan

### 1. Text Preprocessing

Tahapan *preprocessing* yang diterapkan meliputi:

- Case Folding
- Cleaning
- Tokenization
- Stopword Removal

### 2. TF-IDF

*Term Frequency-Inverse Document Frequency* (*TF-IDF*) digunakan untuk memberikan bobot pada setiap kata berdasarkan tingkat kepentingannya dalam dokumen dan koleksi dokumen.

### 3. Cosine Similarity

*Cosine Similarity* digunakan untuk menghitung tingkat kemiripan antara *query* dan dokumen yang telah direpresentasikan dalam bentuk vektor TF-IDF.

### 4. BM25

*Best Matching 25* (*BM25*) merupakan model temu kembali informasi berbasis probabilistik yang mempertimbangkan frekuensi kemunculan kata dan panjang dokumen dalam proses pemeringkatan hasil pencarian.

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

## 📊 Hasil Evaluasi

| Metrik | TF-IDF | BM25 |
|---------|---------|---------|
| MAP | 95% | 100% |
| Precision@1 | 90% | 100% |
| Precision@3 | 33% | 33% |
| Recall@3 | 100% | 100% |

Hasil pengujian menunjukkan bahwa metode **BM25** memberikan performa yang lebih baik dibandingkan metode **TF-IDF**, terutama pada metrik MAP dan Precision@1.

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
git clone https://github.com/sngraihan/STKI_Kelompok5.git
```

### Masuk ke Folder Proyek

```bash
cd STKI_Kelompok5
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

LyrikMatch dikembangkan oleh Kelompok 5 pada Mata Kuliah Sistem Temu Kembali Informasi.

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

LyrikMatch merupakan hasil pengerjaan Proyek Akhir yang disusun untuk memenuhi salah satu persyaratan Ujian Akhir Semester (UAS) pada Mata Kuliah Sistem Temu Kembali Informasi, Program Studi Teknik Informatika, Fakultas Matematika dan Ilmu Pengetahuan Alam, Universitas Lampung.

Proyek ini dibuat untuk tujuan akademik, pembelajaran, dan pengembangan pengetahuan di bidang Sistem Temu Kembali Informasi.
