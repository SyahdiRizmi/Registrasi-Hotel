import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Password",
  database="hotel_sofia"
)


def insert_data(db):
  nama_pemesan = input("Masukan nama: ")
  tanggal_pemesanan = input("Masukan tanggal: ")
  no_kamar = input("Masukkan nomor kamar: ")
  jenis_kamar = input("Masukkan jenis kamar: ")
  no_hp = input("Masukkan nomor handphone:")
  alamat_pemesan = input("Masukkan alamat:")
  metode_pembayaran = input("Pilih metode pembayaran: ")
  id_pelanggan = input("Masukkan id pelanggan: ")
  val = (nama_pemesan, tanggal_pemesanan, no_kamar, jenis_kamar, no_hp, alamat_pemesan, metode_pembayaran, id_pelanggan)
  cursor = db.cursor()
  sql = "INSERT INTO reservation (nama_pemesan, tanggal_pemesanan, no_kamar, jenis_kamar, no_hp, alamat_pemesan, metode_pembayaran, id_pelanggan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} pemesanan berhasil dilakukan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM reservation"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data pemesanan")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  id_pelanggan = input("pilih id pelanggan> ")
  nama_pemesan = input("Nama baru: ")
  tanggal_pemesanan = input("Tanggal baru: ")
  no_kamar = input("Nomor Kamar baru: ")
  jenis_kamar = input("Jenis kamar baru: ")
  no_hp = input("Nomor handphone baru:")
  alamat_pemesan = input("Alamat baru:")
  metode_pembayaran = input("Metode pembayaran baru: ")
  
  sql = "UPDATE reservation SET nama_pemesan =%s, tanggal_pemesanan=%s, no_kamar =%s, jenis_kamar =%s, no_hp= %s, alamat_pemesan= %s, metode_pembayaran= %s  WHERE id_pelanggan=%s"
  val = (nama_pemesan, tanggal_pemesanan, no_kamar, jenis_kamar, no_hp, alamat_pemesan, metode_pembayaran, id_pelanggan)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  id_pelanggan = input("pilih id pelanggan> ")
  sql = "DELETE FROM reservation WHERE id_pelanggan=%s"
  val = (id_pelanggan,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  tanggal_pemesanan = input("Pilih tanggal Pemesanan : ")
  sql = "SELECT * FROM reservation WHERE tanggal_pemesanan = %s"
  val = (tanggal_pemesanan,)
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Data tidak terdaftar")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APLIKASI PEMESANAN HOTEL SOFIA ===")
  print("1. Memasukkan Data Pemesanan")
  print("2. Tampilkan Data Pemesanan")
  print("3. Update Data Pemesanan")
  print("4. Hapus Data Pemesanan")
  print("5. Cari Data Berdasarkan Tanggal Pemesanan")
  print("0. Keluar Aplikasi")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)