# agnesia prawini thesalonika 068
import pwinput
import sys

from program import data1
from program import removeindex
from database import conn


def menu_admin():
    while True:
        print("===========================================".center(80))
        print("|          AL-YESSIIRR GROUP              |".center(80))
        print("|=========================================|".center(80))
        print("|========== 1.TAMBAH BARANG       ========|".center(80))
        print("|========== 2.TAMPILAN BARANG     ========|".center(80))
        print("|========== 3.UPDATE BARANG       ========|".center(80))
        print("|========== 4.CARI BARANG         ========|".center(80))
        print("|========== 5.HAPUS BARANG        ========|".center(80))
        print("|========== 6.SORTING BARANG      ========|".center(80))
        print("|========== 7.KELUAR DARI ADMIN   ========|".center(80))
        print("|========== 8.KELUAR DARI PROGRAM ========|".center(80))
        print("===========================================".center(80))
        pilih = input("masukan pilihan anda :")

        if pilih == "1":
            data1.tambah_barang()

        elif pilih == "2":
            data1.tampilan_barang()

        elif pilih == "3":
            data1.update_barang()

        elif pilih == "4":
            data1.tampilan_barang()
            data1.carii()

        elif pilih == "5":
            data1.hapus_barang(removeindex)

        elif pilih == "6":
            data1.sorting_barang()

        elif pilih == "7":
            break
        elif pilih == "8":
            sys.exit("program telah berhenti.")

def menu_user():
    while True :
        print('==========================================='.center(80))
        print('|          AL-YESSIIRR GROUP              |'.center(80))
        print('|=========================================|'.center(80))
        print('|========== 1.BELI BARANG         ========|'.center(80))
        print('|========== 2.LIAT SALDO          ========|'.center(80))
        print('|========== 3.TAMBAH SALDO        ========|'.center(80))
        print('|========== 4.KELUAR DARI USER    ========|'.center(80))
        print('|========== 5.KELUAR DARI PROGRAM ========|'.center(80))
        print('==========================================='.center(80))

        pilih1 = input("masukan  pilihan anda :")

        if pilih1 == "1":
            data1.beli_barang()


        elif pilih1 == "2":
            data1.liat_saldo()

        elif pilih1 == "3":
            data1.tambah_saldo()

        elif pilih1 == "4":
            break

        elif pilih1 == "5":
            sys.exit("program telah selesai.")


def user_login():
        username = input("Masukkan username: ")
        password = pwinput.pwinput(prompt="Masukkan password: ")
        query = "SELECT * FROM user WHERE username = %s AND password = %s"
        values = (username, password)
        cursor = conn.cursor()
        cursor.execute(query, values)
        user = cursor.fetchone()
        if user:
            querysaldo = "select saldo from user where username = %s and password = %s"
            valuessaldo =(username,password)
            cursor.execute(querysaldo,valuessaldo)
            result = cursor.fetchone()
            data1.saldo += result[0]
            print("Login berhasil. Selamat datang, {}!".format(user[0]))
            print("Saldo Anda: {}".format(user[2]))
            menu_user()
        else:
            print("Login gagal. Silakan coba lagi.")

def create_account(conn):
        cursor = conn.cursor()
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")
        saldo    = input("masukan saldo awal:")
        insert_query = "INSERT INTO user (username, password, saldo) VALUES (%s, %s , %s)"
        account_data = (username,password,saldo)
        cursor.execute(insert_query, account_data)
        conn.commit()
        print(f"Akun {username} berhasil dibuat!")
def admin_login():
        username = input("Masukkan username admin: ")
        password = pwinput.pwinput(prompt="Masukkan password admin: ")
        query = "SELECT * FROM admin WHERE username = %s AND password = %s"
        values = (username, password)
        cursorr = conn.cursor()
        cursorr.execute(query, values)
        admin = cursorr.fetchone()
        if admin:
            print("login berhasil. selamat datang, {}!". format(admin[0]))
            menu_admin()
        else:
            print("login gagal. silahkan coba lagi")

def menu_login():
        while True:
                print("Selamat datang di program login.")
                print("Pilih opsi:")
                print("1. Login user")
                print("2. Login admin")
                print("3. daftar akun")
                print("4. keluar dari program")

                choice = input("Masukkan pilihan: ")

                if choice == "1":
                    user_login()
                elif choice == "2":
                    admin_login()
                elif choice == "3":
                    create_account(conn)
                elif choice == "4 ":
                    sys.exit("Program telah berhenti.")
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
menu_login()
# selesai agnesia prawini thesalonika 068