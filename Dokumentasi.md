# Deskripsi Program

Program yang dibuat adalah program e-commerce yang digunakan untuk membuat dan mengelola toko online dan memungkinkan pengguna untuk melakukan transaksi jual beli secara online. Dalam program e-commerce, pengguna mengatur daftar produk, mengelola persediaan, memproses pesanan, dan melakukan pembayaran secara online. 

Program tersebut menerapkan login multiuser yaitu login sebagai admin dan login sebagai pembeli atau customer. Program tersebut menggunakan konsep linked list sebagai struktur datanya.  Ada dua class dalam program tersebut yaitu class Barang dan class LinkedList. 

Class Barang digunakan untuk mendefinisikan atribut yang terdapat pada barang yang dijual pada sistem e-commerce tersebut. Atribut-atribut yang dimiliki adalah id_barang, merk_barang, nama_barang, harga, dan stok. Class LinkedList digunakan untuk mengelola data barang dalam bentuk linked list dan implementasi operasi-operasi yang tersedia pada sistem e-commerce. 

Pada menu login terdapat beberapa opsi yang tersedia yaitu login user, login admin, daftar akun, lihat menu, dan keluar dari program. Pada login dan daftar akun, data admin dan customer terhubung dengan database.

Pada menu admin, terdapat beberapa operasi yang dapat dilakukan yaitu menambah barang, menampilkan data barang, mengupdate barang, mencari barang dengan menggunakan algoritma fibonacci search, menghapus barang, mengurutkan data barang menggunakan algoritma shell sort, keluar dari menu admin, dan keluar dari program.

Menu_user akan menampilkan opsi untuk pengguna atau customer. Customer dapat memilih untuk membeli barang, melihat invoice, melihat saldo, menambah saldo, keluar dari pengguna, dan keluar dari program. 

# Struktur Project

Modul

Daftar Modul python yang digunakan dalam program e-commerce,yaitu :
-  Prettytable yang berfungsi untuk membuat tabel pada output program supaya terlihat lebih rapi.
-  Mysql.connector yang berfungsi untuk menghubungkan program dengan database Mysql.
-  Pwinput berfungsi untuk input password tersembunyi secara aman tanpa memperlihatkan password yang diketik (disensor dengan bintang '*').
-  sys yang berfungsi untuk menghentikan program tersebut ketik memilih pilihan keluar dari menu.
-  json yang berfungsi untuk membaca dan menulis data barang dalam file json.
- from program import data1 yang berfungsi untuk mengimpor data1 dari program
- from program import removeindex yang berfungsi untuk mengimpor removeindex dari program
- from database import conn yang berfungsi untuk mengimpor conn dari database

Class Barang

Class ini berfungsi untuk menginisialisasi objek dengan atribut yaitu id_barang,merk_barang,nama_barang,harga,dan stock.

Class LinkedList

Pada Class ini terdapat berfungsi untuk membuat linked list dengan atribut seperti head,keranjang,data,data_json,dan saldo.Ada juga atribut index dan step yang berfungsi untuk membagi data barang tersebut menjadi beberapa blok index.

Class LinkedList terdapat beberapa method yang digunakan,yaitu :
- Def tambah_barang,ini berfungsi untuk menambahkan data barang  kedalam linkedlist dan file json.
- Def tampilan_barang,ini berfungsi untuk menampilkan suatu data barang yang tersimpan di data_barang.json dan linkedlist bentuk dalam tabel.
- Def cari_barang,ini berfungsi untuk mencari data barang yang berdasarkan id_barang tersebut.
- Def get_node_at_index_json,ini berfungsi untuk mendapatkan data barang tersebut pada index tertentu dari file json.
- Def update_barang,ini berfungsi untuk memperbarui atau mengupdate data barang tersebut di file json dan linkedlist.
- Def beli_barang,ini berfungsi untuk membeli suatu barang dan menambahkan barang tersebut ke dalam keranjang.
- Def generate_invoice,ini berfungsi untuk menghasilkan invoice pada keranjang.
- Def cari2,ini berfungsi untuk mencari data barang dalam keranjang dengan berdasarkan id_barang.
- Def tampilan_keranjang,ini berfungsi untuk melihat barang yang ada dikeranjang.
- Def shell_sort,ini berfungsi untuk mengurutkan data barang tersebut berdasarkan id_barang menggunakan algoritma shell sort.
- Def sorting_barang,ini berfungsi untuk mengurutkan dan menampilkan data barang yang telah disorting secara terurut 	berdasarkan id_barang.
- Def hapus_barang,berfungsi untuk ingin menghapus suatu data barang dengan menginput nomor barang.Jika berhasil data barang akan dihapus dari linkedlist dan data barang akan diperbarui di file json.
- Def cari,ini berfungsi untuk mencari barang dengan menggunakan algoritma fibonacci search yang berguna mencari data barang dalam linkedlist.
- Def cari1,ini berfungsi untuk mengembalikan nilai index dari barang yang mau dicari dengan menggunakan algoritma fibonacci search.
- Def to_array,berfungsi untuk mengembalikan barang yang tersimpan di linkedlist menjadi dalam bentuk array.
- Def getindex,ini berfungsi untuk mengembalikan node pada index tertentu tersebut didalam linkedlist.
- Def fibonacci_search,ini berfungsi untuk mencari data suatu barang dengan menggunakan algoritma fibonacci search.
- Def get_length,ini berfungsi untuk mendapatkan panjang pada linkedlist.
- Def get_node_at_index_json,ini berfungsi untuk mendapatkan node pada index tertentu tersebut.
- Def menu_admin,berfungsi untuk menampilkan pada menu admin dan opsi pilihan seperti tambah barang,tampilan barang,update barang,cari barang,hapus barang,sorting barang,keluar dari admin,dan keluar dari program.
- Def menu_user,berfungsi untuk menampilkan pada menu user dan opsi pilihan seperti beli barang,invoice barang,liat saldo,keluar dari user,dan keluar dari program.
- Def create_connection,ini berfungsi untuk membuat koneksi ke database mysql.
- Def user_login,ini berfungsi untuk membuat akun yang baru.Disini akan meminta masukkan username,password,dan saldo awal yang nanti 	ditambahkan ke database.
- Def admin_login,ini berfungsi untuk meminta username dan password admin berguna melakukan login.
- Def menu_login,ini berfungsi untuk menampilkan menu login dan opsi pilihan seperti login user,login admin,daftar akun,lihat menu,dan keluar dari program.

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

 # Cara Penggunaan
Pertama,program e-commerce akan menampilkan sebuah menu login.Pengguna akan diminta untuk memilih opsi pilihan sesuai yang di inginkan.

Jika memilih opsi '1' pengguna akan diminta untuk memasukkan username dan password yang benar.Jika berhasil,maka program akan menampilkan sebuah menu user yang memiliki pilihan opsi juga dan pengguna akan menginput salah satu opsi pilihan yang diinginkan.program akan memanggil fungsi user_login
- Jika memilih opsi '1' program akan memanggil fungsi data1.beli_barang
- Jika memilih opsi '2' program akan memanggil fungsi  generate_invoice
- Jika memilih opsi '3' program akan memanggil fungsi data1.saldo
- Jika memilih opsi '4' program akan meminta pengguna untuk memasukkan jumlah saldo yang ingin ditambah
- Jika memilih opsi '5' akan keluar dari menu user
- Jika memilih opsi '6' akan keluar dari program atau berhenti

Jika memilih opsi '2' pengguna akan diminta untuk memasukkan username admin dan password admin   yang benar.Jika berhasil,maka program akan menampilkan sebuah menu admin yang memiliki pilihan opsi juga dan pengguna akan memasukkan opsi yang diinginkan.program akan memanggil fungsi admin_login
- Jika memilih opsi '1' program akan memanggil fungsi data1.tambah_barang
- Jika memilih opsi '2' program akan memanggil fungsi data1.tampilan_barang
- Jika memilih opsi '3' program akan memanggil fungsi data1.update_barang
- Jika memilih opsi '4' program akan memanggil fungsi data1.tampilan_barang dan data1.cari_barang
- Jika memilih opsi '5' program akan memanggil fungsi data1.hapus_barang
- Jika memilih opsi '6' program akan memanggil fungsi data1.sorting_barang
- Jika memilih opsi '7' akan keluar dari menu admin
- Jika memilih opsi '8' akan keluar dari program atau berhenti

Jika memilih opsi '3' pengguna akan diminta untuk memasukkan username,password dan saldo awal untuk mendaftar akun.program akan memanggil fungsi create_account(conn)

Jika memilih opsi '4' program akan menampilkan sebuah menu admin.program akan memanggil fungsi menu_admin

Jika memilih opsi '5' program akan berhenti.


