# bagian Angelina Surachkaryadi 055
import json
from prettytable import PrettyTable

class Barang:
    def __init__(self, id_barang, merk_barang, nama_barang, harga, stok):
        self.id_barang = id_barang
        self.merk_barang = merk_barang
        self.nama_barang = nama_barang
        self.harga = harga
        self.stok = stok
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.keranjang = []
        self.data = []
        self.data_json = ""
        self.saldo = 0

        self.index = []
        self.step = 10  # jumlah data per indeks
        for i in range(0, len(self.data), self.step):
            self.index.append(self.data[i]["id_barang"])

        try:
            with open('data_barang.json') as f:
                self.data = json.load(f)
                self.data_json = json.dumps(self.data)
        except FileNotFoundError:
            ("file data tidak ditemukan")

    def tambah_barang(self):
        id_barang = input("Masukkan ID barang: ")
        merk_barang = input("Masukkan merk barang: ")
        nama_barang = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok barang: "))

        data = {
            "id_barang": id_barang,
            "merk_barang": merk_barang,
            "nama_barang": nama_barang,
            "harga": harga,
            "stok": stok
        }
        
        self.data.append(data)
        self.data_json = json.dumps(self.data)

        with open('data_barang.json', 'w') as f:
            json.dump(self.data, f)
        print("data berhasil ditambahkan")
        new_barang = Barang(id_barang, merk_barang, nama_barang, harga, stok)
        if not self.head:
            self.head = new_barang
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_barang


    def tampilan_barang(self):
        if not self.data:
            print("Tidak ada data barang yang terdaftar.")
        else:
            table = PrettyTable(["NO", "ID Barang", "Merk Barang", "Nama Barang", "Harga", "Stok"])
            for index, item in enumerate(self.data, start=1):
                table.add_row([index, item["id_barang"], item["merk_barang"], item["nama_barang"], item["harga"], item["stok"]])
            print(table)

    def cari_barang(self, id_barang):
        # cari indeks yang tepat
        n = len(self.index)
        jump = int(n ** 0.5)  # besar loncatan
        left, right = 0, n - 1
        while left <= right:
            mid = left + jump
            if mid <= right and self.index[mid] <= id_barang:
                left = mid
            else:   
                right = mid - 1
            jump = int(jump ** 0.5)
        # lakukan pencarian linear pada blok indeks yang tepat
        start = left * self.step
        end = min(start + self.step, len(self.data))
        for i in range(start, end):
            if self.data[i]["id_barang"] == id_barang:
                return i
        return None

    def get_node_at_index_json(self, index):
        if index < 0 or index >= len(self.data):
            return None
        return self.data[index]
# selesai Angelina Surachkaryadi 055

# bagian Dzaki Nurtauriq Mirawan 088
    def update_barang(self):
        self.tampilan_barang()
        while True:
            try:
                index = int(input("Masukkan nomor barang yang ingin diupdate: "))
                if index < 1 or index > len(self.data):
                    raise ValueError()
                break
            except ValueError:
                print("Nomor barang tidak valid. Silakan coba lagi.")

        barang = self.data[index-1]

        while True:
            new_id_barang = input("Masukkan id_barang baru: ")
            if not new_id_barang:
                print("ID Barang tidak boleh kosong!")
            elif any(b['id_barang'] == new_id_barang and b != barang for b in self.data):
                print("ID Barang sudah terdaftar!")
            else:
                break

        while True:
            new_merk_barang = input("Masukkan merk_barang baru: ")
            if not new_merk_barang:
                print("Merk Barang tidak boleh kosong!")
            else:
                break

        while True:
            new_nama_barang = input("Masukkan nama_barang baru: ")
            if not new_nama_barang:
                print("Nama Barang tidak boleh kosong!")
            else:
                break

        while True:
            new_harga = input("Masukkan harga baru: ")
            if not new_harga:
                new_harga = barang['harga']
                break
            try:
                new_harga = float(new_harga)
                break
            except ValueError:
                print("Harga harus berupa angka!")

        while True:
            new_stok = input("Masukkan stok baru: ")
            if not new_stok:
                new_stok = barang['stok']
                break
            try:
                new_stok = int(new_stok)
                if new_stok < 0:
                    print("Stok tidak boleh negatif!")
                else:
                    break
            except ValueError:
                print("Stok harus berupa angka!")

        # update barang pada indeks yang sudah ditemukan
        self.data[index - 1]['id_barang'] = new_id_barang
        self.data[index - 1]['merk_barang'] = new_merk_barang
        self.data[index - 1]['nama_barang'] = new_nama_barang
        self.data[index - 1]['harga'] = new_harga
        self.data[index - 1]['stok'] = new_stok

        # tulis ulang file JSON
        with open('data_barang.json', 'w') as f:
            json.dump(self.data, f)

        print("Data barang berhasil diupdate")
# selesai Dzaki Nurtauriq Mirawan 088

# bagian Muhammad Fandi Perdana 094
    def beli_barang(self):
        data1.tampilan_barang()
        index = int(input("Masukkan NO barang yang ingin dibeli: "))
        try:
            barang = self.data[index-1]
        except IndexError:
            print("Barang dengan NO", index, "tidak ditemukan.")
            return

        if not barang["stok"]:
            print("Maaf, stok barang habis.")
            return

        while True:
            jumlah_str = input("Masukkan jumlah barang yang ingin dibeli: ")
            try:
                jumlah = int(jumlah_str)
                if jumlah <= 0:
                    print("Jumlah barang harus lebih dari 0.")
                elif jumlah > int(barang["stok"]):
                    print("Stok barang tidak mencukupi.")
                else:
                    break
            except ValueError:
                print("Jumlah barang harus berupa angka.")

        harga_total = float(barang["harga"]) * jumlah
        if self.saldo < harga_total:
            print("maaf saldo anda tidak mencukupi. ")
            return

        keranjang_item = f"{barang['id_barang']},{barang['merk_barang']},{barang['nama_barang']},{barang['harga']},{jumlah}"

        self.keranjang.append(keranjang_item)

        while True:
            konfirmasi = input("Apakah anda ingin membeli barang ini? (y/n) ")
            if konfirmasi.lower() == "y":
                self.keranjang.append(barang)
                barang["stok"] = int(barang["stok"]) - jumlah
                with open('data_barang.json', 'w') as f:
                    json.dump(self.data, f)
                    for barang in self.data:
                        barang["stok"] = int(barang["stok"])
                print("Barang telah berhasil dibeli!")
                self.saldo -= harga_total
                print(f"Sisa saldo anda: {self.saldo:.2f}")

                # Generate invoice
                invoice = f"{'-'*30}\n{'ID Barang':<10}{'Merk':<15}{'Nama Barang':<20}{'Harga Satuan':<15}{'Jumlah':<10}\n{'-'*30}\n"
                invoice += f"{barang['id_barang']:<10}{barang['merk_barang']:<15}{barang['nama_barang']:<20}{barang['harga']:<15.2f}{jumlah:<10}\n"
                invoice += f"{'-'*30}\n{'Total Harga:':<25}{'Rp. ' + str(harga_total):>15}\n{'-'*30}\n"

                # Write purchased item and invoice to file
                with open('data_beli.txt', 'a') as file:
                    file.write(f"{invoice}\n")
                break
            elif konfirmasi.lower() == "n":
                print("Pembelian barang dibatalkan.")
                break
            else:
                print("Masukkan pilihan yang valid.")

    def cari2(self, id_barang):
        current = self.head
        while current:
            if current.id_barang == id_barang:
                return current
            current = current.next

    def tampilan_keranjang(self):
        if not self.keranjang:
            print("Keranjang masih kosong.")
        else:
            with open('data_beli.json', 'r') as f:
                data_barang = json.load(f)
            table = PrettyTable(["NO", "ID Barang", "Merk Barang", "Nama Barang", "Harga", "Jumlah", "Subtotal"])
            for index, item in enumerate(self.keranjang, start=1):
                index_barang = item.get("index_barang")
                if index_barang is not None:
                    barang = data_barang[index_barang]
                    subtotal = item["jumlah"] * barang["harga"]
                    table.add_row([index, barang["id_barang"], barang["merk_barang"], barang["nama_barang"], barang["harga"], item["jumlah"], subtotal])
                else:
                    print(f"Item {index} does not have the 'index_barang' key.")
            print(table)

    def shell_sort(self):
        n = len(self.data)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.data[i]
                j = i
                while j >= gap and self.data[j - gap]["id_barang"] > temp["id_barang"]:
                    self.data[j] = self.data[j - gap]
                    j -= gap
                self.data[j] = temp
            gap //= 2
        return self.data

    def sorting_barang(self):
        if not self.data:
            print("Tidak ada data barang yang terdaftar.")
        else:
            self.data = self.shell_sort()
            with open('data_barang.json', 'w') as f:
                json.dump(self.data, f)
            print("Data barang berhasil diurutkan!")

    def hapus_barang(self, index):
        data1.tampilan_barang()
        index = int(input("masukan no barang jika ingin menghapus data barang :"))
        if index <1 or index>  len(self.data):
            print("Indeks barang tidak valid.")
            return
        else:
            self.data.pop(index -1)
            with open('data_barang.json', 'w') as f:
                json.dump(self.data, f)
            print("Barang dengan no", index, "berhasil dihapus.")

    def cari(self):
        cari1 = input("masukan barang yang ingin dicari")
        hasil = data1.fibonacci_search(cari1)
        if hasil == -1:
            print(f"barang {cari1} tidak ditemukan.")
        else:
            print(f"barang {cari1} ditemukan pada index {hasil} barang ")
    def cari1(self,index):
        return self.fibonacci_search(index)
    def to_array(self):
        array = []
        current_node = self.head
        while current_node is not None:
            array.append(current_node.id_barang)
            current_node = current_node.next
        return array
    def getindex(self, index):
        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_index == index:
                return current_node

            current_node = current_node.next
            current_index += 1

    def get_length(self):
        current_node = self.data
        count = 0
        while current_node:
            count += 1
            current_node = self.data
        return count

    def get_node_at_index_json(self, index):
        current_node = self.head
        count = 0
        while current_node:
            if count == index:
                return current_node
            count += 1
            current_node = current_node.next
        return None

    def carii(self):
        cari = input("masukan data yang ingin dicari : ")
        hasil = data1.cari_barang(cari)
        if hasil ==-1:
            print(f"data {cari} tidak ditemukan ")
        else:
            print(f"data {cari} ditemukan pada index {hasil} barang:")

    def tambah_saldo():
        inputsaldo = int(input("masukan jumlah saldo :"))
        data1.saldo += inputsaldo

    def liat_saldo():
        print("saldo anda :",data1.saldo)

removeindex = 0
data1 = LinkedList()
# selesai Muhammad Fandi Perdana 094