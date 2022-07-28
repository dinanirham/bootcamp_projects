[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8042867&assignment_repo_type=AssignmentRepo)
# Milestones 1

_Milestones ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada Phase 1 dalam konsep Supervised Learning._

---

## Assignment Instructions

Buka [Google Cloud Platform](https://console.cloud.google.com/), masuk ke BigQuery, lalu buka tab `bigquery-public-data` atau klik link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&page=dataset&_ga=2.245085957.1471931019.1642739417-486643658.1638156099) atau link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ml_datasets&t=credit_card_default&page=table) untuk langsung menuju ke dataset.

```{attention}
Perhatikan petunjuk penggunaan dataset!
```

1. Gunakan dataset `ml_datasets` dari database bernama `credit_card_default`.

2. Buatlah query dengan kriteria sebagai berikut:
   - Pilih **HANYA** kolom `limit_balance, sex, education_level, marital_status, age, pay_0, pay_2, pay_3, pay_4, pay_5, pay_6, bill_amt_1, bill_amt_2, bill_amt_3, bill_amt_4, bill_amt_5, bill_amt_6, pay_amt_1, pay_amt_2, pay_amt_3, pay_amt_4, pay_amt_5, pay_amt_6, default_payment_next_month`.
   - Kolom diatas hanya digunakan sebagai dataset awal. Silakan lakukan Feature Selection di-notebook setelah dataset dibuat.
   - Limit jumlah data menjadi sebanyak `nomor batch dikali dengan tahun lahir kalian`. ex: Batch 10 dan lahir tahun 1995, 10 x 1995 = 19950.

3. Simpan dataset dalam bentuk csv, dengan nama `h8dsft_P1M1_<nama-students>.csv`.

4. Salin query yang telah dibuat di Google Cloud Platform, tulislah pada bagian atas notebook!

5. Tampilkan `head` dan `tail` dari dataset pada notebook!

_Milestones 1_ dikerjakan dalam format _notebook_ dengen beberapa **kriteria wajib** di bawah ini:

1. Machine learning framework yang digunakan adalah _Scikit-Learn_.

2. Ada penggunaan library visualisasi, seperti _matplotlib_, _seaborn_, atau yang lain.

3. Isi _notebook_ harus mengikuti _outline_ di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, gambaran besar dataset yang digunakan, dan _objective_ yang ingin dicapai.

   2. Import Libraries
      > _Cell_ pertama pada _notebook_ **harus berisi dan hanya berisi** semua _library_ yang digunakan dalam _project_.

   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.

   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi eksplorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.

   5. Data Preprocessing
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-dev-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.

   8. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   9. Model Inference
      > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled.

   10. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan _objective_ yang sudah ditulis di bagian pengenalan.

4. Notebook harus diupload dalam akun GitHub Classroom masing-masing siswa untuk selanjutnya dinilai. Jika dalam sebuah tugas terdapat dua atau lebih soal, maka gabungkan jawaban ke dalam satu file notebook.

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `h8dsft_P1M1_<nama-student>.ipynb` misal `h8dsft_P1M1_raka_ardhi.ipynb`.
- Push Assigment yang telah kalian buat ke akun Github Classroom kalian masing-masing.

## Problems

Buatlah model Classification untuk memprediksi `default_payment_next_month` menggunakan dataset yang sudah kalian simpan.

## Conceptual Problems

_Jawab pertanyaan berikut:_

1. Apakah fungsi parameter `criterion` pada Decision Tree? Jelaskan salah satu criterion yang kalian pahami!
2. Apakah fungsi dari `pruning` pada Tree model?
3. Bagaimana cara memilih `K` yang optimal pada KNN?
4. Jelaskan apa yang kalian ketahui tentang `Cross Validation`!
5. Jelaskan apa yang kalian ketahui tentang `Accuracy, Precision, Recall, F1 Score`!

## Assignment Objectives

_Milestones 1_ ini dibuat guna mengevaluasi Pembelajaran Phase 1 dalam konsep Supervised Learning sebagai berikut:

- Mampu memperoleh data menggunakan BigQuery
- Mampu memahami konsep supervised learning
- Mampu mempersiapkan data untuk digunakan dalam model supervised learning
- Mampu mengimplementasikan supervised learning dengan data yang diberikan
- Mampu melakukan evaluasi model
- Mampu melakukan model tuning

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| SQL | Mampu melakukan query data dengan kriteria yang telah diberikan | 30 pts |
| Preprocessing | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) | 20 pts |
| Logistic Regression | Mengimplementasikan Logistic Regression dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| SVM | Mengimplementasikan SVM dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Decision Tree | Mengimplementasikan Decision Tree dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Random Forest | Mengimplementasikan Random Forest dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| KNN | Mengimplementasikan KNN dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Naive Bayes | Mengimplementasikan Naive Bayes dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Other Algorithm | Mengimplementasikan algoritma lain selain yang tersebut diatas dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 20 pts |
| Cross Validation | Mengimplementasikan Cross Validation dengan Scikit-Learn | 30 pts |
| Grid Search | Mengimplementasikan Grid Search dengan Scikit-Learn | 30 pts |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts |
| Apakah Kode Berjalan Tanpa Ada Error? | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar | 10 pts |

### Concepts

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Classifications 1 | Mampu menjawab pertanyaan dengan singkat, jelas, dan padat serta sesuai dengan konsep dan logika yang ada mengenai Conceptual Problems (10 each number) | 50 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 20 pts |

```
Kriteria tertata dengan baik diantaranya adalah : 

1. Terdapat section Perkenalan yang jelas
2. Tidak menyalin markdown dari tugas lain.
3. Import library rapih (terdapat dalam 1 cell dan tidak ada unused libs).
4. Pemakaian fungsi markdown yang optimal (Heading, text formating, dll). 
5. Terdapat komentar pada setiap baris kode.
6. Adanya pemisah yang jelas antar section, dll.
```

### Analysis

| Criteria | Meet Expectations | Points|
| --- | --- | --- |
| Model Analysis | Menganalisa informasi dari model yang telah dibuat | 20 pts |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan | 30 pts |

```
Contoh kriteria analisa yang baik diantaranya adalah : 
1. Terdapat penjelasan macam-macam hasil metric evaluasi dan interpretasinya terhadap kasus yang diselesaikan. 
2. Dapat menjelaskan kelemahan/kekurangan dan kelebihan dari model yang dibuat. 
3. Dapat memberikan statement untuk improvement selanjutnya dari model yang dibuat. 
4. Sebutkan insight yang dapat diambil setelah proses EDA, dll.
```

---

```
Total Points : 350
```

---

## Notes

- **Deadline : P1W3D3 pukul 23:59 WIB.**

- **Keterlambatan pengumpulan tugas mengakibatkan skor Milestone 1 menjadi 0.**
