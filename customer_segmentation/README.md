[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8083632&assignment_repo_type=AssignmentRepo)
# Graded Challenge 4

_Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Clustering._

---

## Assignment Objectives

*Graded Challenge 4* ini dibuat guna mengevaluasi konsep Clustering sebagai berikut:

- Mampu memperoleh data menggunakan BigQuery
- Mampu mempersiapkan data untuk digunakan dalam Clustering
- Mampu memahami konsep Clustering dengan menggunakan Scikit-Learn
- Mampu mengimplementasikan Clustering pada data yang diberikan

---

## Problems

Buatlah model clustering untuk melakukan Customer Segmentation dari data kartu kredit sebuah bank dibawah ini. Data ini merupakan data informasi penggunaan kartu kredit selama 6 bulan terakhir. 

---

## Conceptual Problems

*Jawab pertanyaan berikut:*

1. Apakah yang dimaksud dengan `inertia` pada algoritma K-Means ?

2. Jelaskan yang dimaksud dengan Elbow Method (alasan penggunaan, cara penggunaan, kelemahan/kelebihan, dll) !

3. Jelaskan perbedaan masing-masing algoritma clustering yang anda gunakan dalam kasus ini !

---

## Dataset

```{attention}
Perhatikan petunjuk penggunaan dataset!
```

1. Pada tugas kali ini, dataset yang digunakan **tidak akan menggunakan `bigquery-public-data`**. 

2. Masuk ke dalam Google BigQuery. Gunakan informasi dibawah ini sebagai tempat untuk mengambil data (gunakan sebagai informasi untuk klausa `FROM`).
   * Project ID : `ftds-hacktiv8-project`
   * Dataset Name : `phase1_assignments`
   * Table Name : `credit-card-information`

3. Ambil data dengan kriteria berikut ini : 
   * Batch ganjil (FTDS-001, FTDS-003, dst) : semua data dengan column `CUST_ID` bernilai ganjil.
   * Batch genap (FTDS-002, FTDS-004, dst) : semua data dengan column `CUST_ID` bernilai genap.

4. Berikut ini adalah informasi dari setiap column. 
   <img src='https://i.ibb.co/2sbf0Js/P1-G4-Dataset-Information.png'>

5. Simpan dataset dalam bentuk `.csv` dengan nama `h8dsft_P1G4_<nama-students>.csv` misal `h8dsft_P1G4_raka_ardhi.csv`.

6. Salin query yang telah dibuat di Google Cloud Platform. Tulislah pada bagian atas notebook!

7. Tampilkan `head` dan `tail` dari dataset pada notebook!

---

## Assignment Instructions

*Graded Challenge 4* dikerjakan dalam format ***notebook*** dengen beberapa **kriteria wajib** di bawah ini:

1. Machine learning framework yang digunakan adalah *Scikit-Learn*.

2. Ada penggunaan library visualisasi, seperti *matplotlib*, *seaborn*, atau yang lain.

3. Isi *notebook* harus mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, gambaran besar dataset yang digunakan, dan *objective* yang ingin dicapai.
   
   2. Import Libraries
      > *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
   
   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.
   
   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi explorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.
   
   5. Data Preprocessing
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-set dan inference-set, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.
   
   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.
   
   8. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   9. Model Inference
      > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled.
   
   10. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.
    
5. *Notebook* harus diupload dalam akun GitHub masing-masing siswa untuk selanjutnya dinilai.

---

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `h8dsft_P1G4_<nama-students>.ipynb` misal `h8dsft_P1G4_raka_ardhi.ipynb`.

- Push assignment yang telah Anda buat ke akun Github Classroom Anda masing-masing.

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| SQL | Mampu melakukan query data dengan kriteria yang telah diberikan | 20 pts |
| Preprocessing | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) | 20 pts |
| PCA | Mampu melakukan reduksi dimensi dengan menggunakan PCA | 10 pts |
| K-Means | Mengimplementasikan K-Means dan mengevaluasi hasil cluster yang terbentuk (**minimal 2 teknik berbeda**) | 20 pts |
| Other Algorithm Clustering | Mengimplementasikan **dua algoritma clustering yang lain** selain K-Means beserta hyperparameter yang tepat dengan Scikit-Learn | 20 pts each (40 pts max) |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts |
| Apakah Kode Berjalan Tanpa Ada Error? | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar| 10 pts |

### Concepts

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Clustering | Mampu menjawab pertanyaan dengan singkat, jelas, dan padat serta sesuai dengan konsep dan logika yang ada mengenai Conceptual Problems (Soal 1 : 10 pts. Soal 2 : 10 pts. Soal 3 : 20 pts) | 40 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 20 pts |

```
Kriteria tertata dengan baik diantaranya adalah: 

1. Terdapat section Perkenalan yang jelas.
2. Tidak menyalin markdown dari tugas lain.
3. Import library rapih (terdapat dalam 1 cell dan tidak ada unused libs).
4. Pemakaian fungsi markdown yang optimal (Heading, text formating, dll).
5. Terdapat komentar pada setiap baris kode.
6. Adanya pemisah yang jelas antar section, dll.
```

### Analysis

| Criteria | Meet Expectations | Points|
| --- | --- | --- |
| Model Analysis | Menganalisa informasi dari model yang telah dibuat | 30 pts |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan | 20 pts |

```
Contoh kriteria analisa yang baik diantaranya adalah: 

1. Terdapat penjelasan macam-macam hasil metric evaluasi dan interpretasinya terhadap kasus yang diselesaikan.
2. Dapat menjelaskan kelemahan/kekurangan dan kelebihan dari model yang dibuat.
3. Dapat memberikan statement untuk improvement selanjutnya dari model yang dibuat. 
4. Sebutkan insight yang dapat diambil setelah proses EDA, dll.
```

---

```
Total Points : 240
```

---

## Notes

* **Deadline : P1W4D2 pukul 23:59 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor GC 4 menjadi 0.**
