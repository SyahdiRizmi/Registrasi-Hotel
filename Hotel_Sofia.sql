CREATE SCHEMA hotel_sofia;
USE hotel_sofia;

CREATE TABLE reservation
(nama_pemesan varchar(50), 
tanggal_pemesanan date,
no_kamar integer,
jenis_kamar varchar(50),
no_hp varchar(100),
alamat_pemesan varchar(50),
metode_pembayaran varchar(50),
id_pelanggan varchar(50)
);
