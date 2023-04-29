# Deskripsi Program

Program yang dibuat adalah program e-commerce yang digunakan untuk membuat dan mengelola toko online dan memungkinkan pengguna untuk melakukan transaksi jual beli secara online. Dalam program e-commerce, pengguna mengatur daftar produk, mengelola persediaan, memproses pesanan, dan melakukan pembayaran secara online. 

Program tersebut menerapkan login multiuser yaitu login sebagai admin dan login sebagai pembeli atau customer. Program tersebut menggunakan konsep linked list sebagai struktur datanya.  Ada dua class dalam program tersebut yaitu class Barang dan class LinkedList. 

Class Barang digunakan untuk mendefinisikan atribut yang terdapat pada barang yang dijual pada sistem e-commerce tersebut. Atribut-atribut yang dimiliki adalah id_barang, merk_barang, nama_barang, harga, dan stok. Class LinkedList digunakan untuk mengelola data barang dalam bentuk linked list dan implementasi operasi-operasi yang tersedia pada sistem e-commerce. 

Pada menu login terdapat beberapa opsi yang tersedia yaitu login user, login admin, daftar akun, lihat menu, dan keluar dari program. Pada login dan daftar akun, data admin dan customer terhubung dengan database.

Pada menu admin, terdapat beberapa operasi yang dapat dilakukan yaitu menambah barang, menampilkan data barang, mengupdate barang, mencari barang dengan menggunakan algoritma fibonacci search, menghapus barang, mengurutkan data barang menggunakan algoritma shell sort, keluar dari menu admin, dan keluar dari program.

Menu_user akan menampilkan opsi untuk pengguna atau customer. Customer dapat memilih untuk membeli barang, melihat invoice, melihat saldo, menambah saldo, keluar dari pengguna, dan keluar dari program. 

# Fitur dan Fungsionalitas

Pada menu login terdapat beberapa fitur yang dapat diakses yaitu login user, login admin, daftar akun, lihat menu, dan keluar dari program.

•	Pada fitur login user, pengguna dapat login ke dalam akun pengguna dengan memasukkan username dan password yang telah terdaftar dalam database. Jika login berhasil, maka pengguna akan diarahkan ke menu pengguna (menu_user).

•	Pada fitur login admin:, admin dapat login ke dalam akun admin dengan memasukkan username dan password yang telah terdaftar dalam database. Jika login berhasil, maka admin akan diarahkan ke menu admin (menu_admin).

•	Pada fitur daftar akun, pengguna dapat membuat akun baru dengan memasukkan username, password, dan saldo awal. Akun baru ini akan disimpan ke dalam database.

•	Pada fitur lihat lihat menu, pengguna dapat melihat menu yang tersedia dalam program.

•	Pada fitur keluar dari program, program akan memanggil fungsi sys.exit() dan program akan dihentikan.

Pada menu admin terdapat beberapa fitur yang dapat diakses yaitu tambah barang, tampilkan barang, update barang, cari barang, hapus barang, sorting barang, keluar dari admin, dan keluar dari program.

•	Pada fitur tambah barang admin dapat menambahkan barang dengan memasukkan data Id barang, merk barang, nama barang, dan harga. Data barang baru akan ditambahkan ke dalam linked list. 

•	Pada fitur tampilkan barang program dapat menampilkan seluruh data barang yang tersimpan dalam linked list. Data barang akan ditampilkan dalam bentuk tabel menggunakan library prettytable.

•	Pada fitur update barang admin dapat memperbarui data barang dengan memasukkan Id barang yang akan diupdate, dan informasi baru yang akan diganti.

•	Pada fitur cari barang admin dapat mencari data barang dalam linked list dengan memasukkan nama barang yang dicari. Program akan mencari nama barang dalam linked list menggunakan algoritma fibonacci search.

•	Pada fitur hapus barang admin dapat menghapus data barang yang tersimpan dalam linked list dengan memasukkan Id barang yang akan dihapus.

•	Pada fitur  sorting barang program dapat mengurutkan data barang dalam linked list menggunakan algoritma shell sort.

•	Pada fitur keluar dari admin, program akan keluar dari menu admin dan kembali ke menu login.

•	Pada fitur keluar dari program, program akan memanggil fungsi sys.exit() untuk memberhentikan program.

Pada menu user terdapat beberapa fitur yang dapat diakses yaitu beli barang, invoice barang, lihat saldo, tambah saldo, keluar dari use, dan keluar dari program.

•	Pada fitur beli barang customer dapat membeli barang dari daftar barang yang tersedia.  Saldo pengguna akan otomatis berkurang jika pembelian berhasil. Informasi pembelian kemudian akan disimpan dalam file json.

•	Pada fitur invoice barang program akan menghasilkan invoice untuk semua barang yang telah dibeli. Invoice mencantumkan id barang, nama barang, harga barang, jumlah barang, dan harga total. Total harga dihitung dan dicetak di bagian bawah.

•	Pada fitur lihat saldo program akan menampilkan saldo customer saat ini.

•	Pada fitur tambah saldo customer dapat memasukkan sejumlah uang untuk ditambahkan ke saldo akun mereka.

•	Pada fitur keluar dari user, program akan keluar dari menu user dan kembali ke menu login.

•	Pada fitur keluar dari program, program akan memanggil fungsi sys.exit() untuk mengakhiri program.
