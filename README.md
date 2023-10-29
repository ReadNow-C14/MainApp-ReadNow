<h1 align="center">ReadNow</h1>
<p align="center">Proyek berbasis Django untuk tugas kelompok tengah semester mata kuliah Pemrograman Berbasis Platform Ganjil 2023/2024.</p>

---
## Link Deployment
https://ristek.link/ReadNow-C14

## Anggota Kelompok
- Harjuno Abdullah (2206814053)
- Muhammad Fakhri Robbani (2206026252)
- Rachel Heningtyas Zanetta Erari (2206081944)
- Rakha Fadil Atmojo (2206082985)
- Zuhdy Nadhif Ayyasy (2206081212)

## Daftar Isi
- [Tentang ReadNow](#tentang-readnow)
- [Latar Belakang ReadNow](#latar-belakang-readnow)
- [Manfaat ReadNow](#manfaat-readnow)
- [Daftar Modul](#daftar-modul)
  - [Modul Wishlist (_Favorite Books_)](#modul-wishlist-favorite-books)
  - [Modul Rekomendasi Buku](#modul-rekomendasi-buku)
  - [Modul Review Buku dan Forum](#modul-review-buku-dan-forum)
  - [Modul Pinjam Buku](#modul-pinjam-buku)
- [Sumber Dataset Katalog Buku](#sumber-dataset-katalog-buku)
- [Role User](#role-user)
  - [Pengguna Tidak Log In](#pengguna-tidak-log-in)
  - [Pengguna Log In](#pengguna-log-in)
  - [Admin](#admin)

---

## Tentang ReadNow
ReadNow adalah sebuah perpustakaan virtual berbasis website yang memungkinkan penggunanya untuk menjelajahi dunia literatur dengan mudah dan nyaman. Dengan akses ke berbagai koleksi buku, pengguna dapat dengan cepat mencari judul-judul yang diminati, meminjam buku secara digital, serta mendapatkan rekomendasi buku berdasarkan preferensi mereka. Selain itu, ReadNow juga menyediakan platform interaktif yang memungkinkan pengguna untuk berinteraksi, berdiskusi, dan berbagi pandangan dengan sesama pecinta buku, menjadikan pengalaman membaca lebih bermakna dan sosial. 

## Latar Belakang ReadNow
Tingkat literasi di Indonesia menjadi tantangan serius yang perlu diatasi. Berdasarkan Program for International Student Assessment (PISA) yang diselenggarakan oleh OECD, Indonesia menempati peringkat 62 dari 70 negara pada tahun 2019 dalam hal tingkat literasi. Selain itu, UNESCO menyebutkan bahwa minat baca masyarakat Indonesia hanya 0,001 persen. Artinya dari 1.000 orang Indonesia hanya 1 orang yang gemar membaca. Fakta-fakta ini mencerminkan kebutuhan mendesak akan upaya-upaya yang lebih besar dalam meningkatkan literasi, terutama literasi digital, di kalangan masyarakat Indonesia. ReadNow hadir sebagai solusi inovatif yang bertujuan untuk mengatasi tantangan ini dengan menyediakan akses mudah ke berbagai koleksi buku dan memfasilitasi pengguna dalam meningkatkan literasi mereka, serta menjadi platform interaktif yang mendukung perkembangan minat literasi secara sosial.

## Manfaat ReadNow
1. Pengguna dapat dengan mudah mencari, mengakses, dan membaca berbagai buku dari berbagai genre dan topik, tanpa harus pergi ke perpustakaan fisik.
2. Membantu meningkatkan tingkat literasi, terutama literasi digital, dengan menyediakan akses ke sumber bacaan yang beragam.
3. Membantu menemukan buku-buku baru yang sesuai dengan minat dari pengguna.
4. Pengguna dapat dengan mudah berbagi buku atau rekomendasi dengan teman-teman mereka melalui forum.

---

## Daftar Modul
### ❤️ Modul Wishlist (_Favorite Books_) ❤️
Modul ini memungkinkan pengguna untuk menambahkan buku-buku ke dalam wishlist mereka. Fitur-fitur utama dari modul ini akan meliputi:
- Menambah buku ke dalam wishlist
- Menghapus buku dari wishlist
- Melihat daftar buku yang ada dalam wishlist pengguna

### 💡 Modul Rekomendasi Buku 💡
Modul ini akan memberikan rekomendasi buku kepada pengguna berdasarkan preferensi mereka dan buku-buku yang telah mereka favoritkan. Fitur-fitur utama dari modul ini akan meliputi:
- Memberikan rekomendasi buku berdasarkan buku-buku favorit pengguna atau buku yang sedang dilihat.
- Memperbarui rekomendasi saat pengguna menambah atau menghapus buku dari daftar keinginan.

### 📝 Modul Review Buku dan Forum 📝
Modul ini memungkinkan pengguna untuk menulis dan membagikan ulasan buku, serta dapat berdiskusi mengenai buku dengan pengguna lain. Fitur-fitur utama dari modul ini akan meliputi:
- Menulis ulasan buku
- Memberi peringkat buku
- Melihat ulasan dan peringkat buku oleh pengguna lain
- Berdiskusi dengan pengguna lain mengenai buku

### 📚 Modul Pinjam Buku 📚
Modul ini memungkinkan pengguna untuk meminjam buku dari daftar buku yang tersedia. Fitur-fitur utama dari modul ini akan meliputi:
- Meminjam buku-buku yang tersedia
- Mengembalikan buku yang dipinjam

---

## Sumber Dataset Katalog Buku
Dataset yang kami gunakan merupakan data informasi buku yang berasal dari website Goodreads. Data-data ini kami ambil dari platform Kaggle yang kemudian kami gabung menjadi satu file csv dan json. Berikut adalah link sumber datanya.
- [Kaggle - Goodreads Book Datasets 10M](https://www.kaggle.com/datasets/bahramjannesarr/goodreads-book-datasets-10m)
- [Kaggle - Goodreadsbooks](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks)
- [QuantEcon - Goodreads Books CSV](https://datascience.quantecon.org/assets/data/goodreads_books.csv)

---

## Role User
### 👤 Pengguna Tidak Log In 👤
Pengguna yang tidak masuk atau mendaftar ke dalam sistem tetap memiliki akses terbatas ke beberapa fitur dalam proyek ini. Fitur-fitur ini akan mencakup:
- `Menjelajahi Buku`: Pengguna dapat melihat daftar buku yang tersedia, membaca deskripsi, dan melihat peringkat buku tanpa perlu masuk.
- `Mengakses Detail Buku`: Pengguna dapat mengakses halaman detail buku untuk melihat informasi lebih lanjut tentang buku tertentu.
- `Mengakses Ulasan Publik`: Pengguna dapat membaca ulasan publik yang ditulis oleh pengguna lain.
- `Melakukan Pencarian Buku`: Pengguna dapat melakukan pencarian buku berdasarkan judul, penulis, atau kategori tanpa perlu masuk.
- `Melihat Rekomendasi Umum`: Pengguna dapat melihat rekomendasi buku umum berdasarkan buku-buku populer, tetapi rekomendasi yang lebih spesifik memerlukan masuk.

### 👨 Pengguna Log In 👨
Pengguna yang masuk ke dalam sistem memiliki akses lebih banyak fitur dan fungsi, termasuk:
- `Menambahkan Buku ke Wishlist`: Pengguna dapat menambahkan buku ke dalam wishlist mereka.
- `Menulis Ulasan atau Forum Buku`: Pengguna dapat menulis ulasan dan memberikan peringkat pada buku serta berdiskusi mengenai buku dengan pengguna lain.
- `Melakukan Peminjaman Buku:` Pengguna dapat meminjam buku dari daftar buku yang tersedia.
- `Melihat Rekomendasi Personal`: Pengguna dapat melihat rekomendasi buku yang disesuaikan berdasarkan preferensi mereka dan buku-buku yang telah mereka favoritkan.

### 👮‍♂️ Admin 👮‍♂️
Admin adalah pengguna khusus dengan hak istimewa tertentu. Admin memiliki akses ke semua aspek proyek dan dapat melakukan tugas administratif, seperti:
- `Mengelola Buku`: Admin dapat menambahkan, mengedit, dan menghapus buku dari sistem.
