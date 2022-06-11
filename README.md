# Kelompok 7
1.	Ahmad Syahdi Al-Khawarizmi (2107733)
2.	Debri Yanti Safitri Santoso (2104174)
3.	Nabila Nur Banafsyah (2109471)

# Hotel Sofia WebApp
Respository ini diajukan untuk memenuhi Ujian Akhir Semester mata kuliah Basis Data dan Sistem Basis Data program studi Mekatronika dan Kecerdasan Buatan Universitas Pendidikan Indonesia tahun 2022.

## _Problem_
Sektor pariwisata merupakan salah satu sektor berbasis jasa yang potensial dan strategis dalam pengembangan perekonomian baik nasional maupun daerah. Semakin terkenal dan berkembangnya pariwisata pada suatu daerah, maka semakin banyak juga yang mengunjungi daerah tersebut baik turis lokal maupun internasional. 
Karena berasal dari luar daerah, maka para turis pun membutuhkan tempat untuk beristirahat saat sedang berwisata. Hotel merupakan tempat yang biasanya dipilih turis untuk beristirahat.  Semakin banyak tempat pariwisata pada suatu daerah, maka semakin banyak juga hotel yang dibangun pada daerah tersebut.
Tidak semua hotel memiliki aplikasi pemesanan kamar, bahkan terdapat hotel yang masih memasukan data pemesanan secara manual.  Maka dari itu dibutuhkan aplikasi yang dapat membantu pemasukan data pemesanan  agar lebih mudah dan cepat.

## _Solution_
Karena masih terdapat hotel yang masih memasukan data pemesanan kamar secara manual. Maka, kami membuat aplikasi pemesanan hotel yaitu Hotel Sofia WebApp.   
Hotel Sofia WebApp adalah aplikasi perhotelan untuk menginput data pemesanan hotel. Aplikasi ini ditujukan untuk membantu admin hotel agar waktu pemesanan hotel lebih mudah dan lebih cepat. Admin hotel dapat memasukan nama pemesan, tanggal pemesanan, nomor kamar, dan jenis kamar untuk tiap pemesanan kamar. Selain itu, admin hotel dapat mencari atau menampilkan data pemesanan kamar berdasarkan tanggal pemesanan.

## _Flowchart_
![uas basdat (3)](https://user-images.githubusercontent.com/106594179/173189960-076b1955-84ca-4ea9-a293-186b9850bf57.png)

## _Panduan Menggunakan Aplikasi_
- download semua file beserta aplikasi yang diperlukan seperti vs code, mysql workbench
- open file sql dan file python dengan ekstensi.py
- jalankan program python tadi dengan mengklik run code

## _Demo_
![Screenshot (21)](https://user-images.githubusercontent.com/106594179/173196817-ab43f0f0-4dc1-498e-8aa2-d64fd8ce2935.png)
- run code python yang sudah dibuat

![Screenshot (18)](https://user-images.githubusercontent.com/106594179/173196120-68d0419b-a619-46c1-9837-2a543479bea2.png)
- pilih menu yang akan dijalankan berdasarkan nomor menu

![Screenshot (13)](https://user-images.githubusercontent.com/106594179/173196206-e63951fc-fe4f-4b2d-a600-4179e45cbc68.png)
- jika pilih menu 1, maka akan muncul menu pemesanan hotel
- kemudian anda diminta untuk mengisi nama_pemesan, tanggal_pemesanan, no_kamar, jenis_kamar, no_hp, alamat_pemesan, metode_pembayaran,  dan id_pelanggan
- setelah itu akan masuk ke menu utama

![Screenshot (14)](https://user-images.githubusercontent.com/106594179/173196339-1a0c82c9-522e-4f35-8073-16b3f05a03f5.png)
- jika pilih menu 2, maka akan muncul data pemesanan yang telah di-input
- setelah itu akan masuk ke menu utama

![Screenshot (15)](https://user-images.githubusercontent.com/106594179/173196409-809a5acc-99b2-4463-9565-49c6723bf3c4.png)
- jika pilih menu 3, maka akan muncul menu meng-update data berdasarkan id yang dimasukkan
- anda diminta memasukkan id dan data-data baru lainnya
- setelah itu akan masuk ke menu utama

![Screenshot (16)](https://user-images.githubusercontent.com/106594179/173196499-098bad85-7d25-42e4-9f73-a931436aea33.png)
- jika pilih menu 4, maka akan muncul menu menghapus data berdasarkan id yang dimasukkan
- masukkan id data pelanggan yang akan dihapus
- semua data pelanggan dengan id tersebut akan terhapus
- setelah itu akan masuk ke menu utama

![Screenshot (17)](https://user-images.githubusercontent.com/106594179/173196560-6398566a-09fc-45e6-b6b1-3520c8681ee2.png)
- jika pilih menu 5, maka akan dijalankan menu mencari data berdasarkan data tanggal pemesanan
- masukkan data pemesanan yang akan dicari
- maka akan muncul data pelanggan berdasarkan tanggal pemesanan
- setelah itu akan masuk ke menu utama

![Screenshot (18)](https://user-images.githubusercontent.com/106594179/173196665-cdd7650e-e5e1-4301-84d3-7f1fbaf77525.png)
- jika pilih menu selain yang ada pada daftar menu maka akan muncul tulisan "Menu Salah!"
- setelah itu akan masuk ke menu utama

![Screenshot (19)](https://user-images.githubusercontent.com/106594179/173196722-d91cfe31-7d0a-49f4-af63-749e26ce0f19.png)
- jika pilih menu 0, maka anda akan keluar Aplikasi Pemesanan Hotel Sofia

Berikut adalah gambar dari database yang didapatkan di Mysql Workbench
![Screenshot (20)](https://user-images.githubusercontent.com/106594179/173196757-4251bbeb-5a12-4fe3-9017-12a5fb6f6d8f.png)

## _References_
[freecodecamp.org](https://wwww.freecodecamp.org/news/the-python-guide-for-beginners/) - referensi untuk belajar coding python

