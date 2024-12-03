import os
import csv
import pandas as pd
TEMPLATE = {
    "pasien": "pasien.csv",
    "dokter":"dokter.csv",
    "ruang": "ruang.csv",
    "antrian": "antrian.csv ",
    "resep": "resep.csv",
    "dokter": "dokter.csv",
    "admin": "admin.csv",
    "pengguna": "pengguna.csv"
}

def init_csv():
    for key, file in TEMPLATE.items():
        if not os.path.exists(file):
            with open(file, "w", newline="") as f:
                writer = csv.writer(f)
                if key == "pasien":
                    writer.writerow(["Nama", "Umur", "Alamat", "Poli", "Keluhan", "Ruangan", "Obat"])
                elif key == "ruang":
                    writer.writerow(["Ruangan", "Nama Pasien"])
                elif key == "antrian":
                    writer.writerow(["Poli", "Nama Pasien"])
                elif key == "resep":
                    writer.writerow(["Nama Pasien", "Obat"])
                elif key == "dokter":
                    writer.writerow(["Poli", "Dokter"])
                elif key == "admin":
                    writer.writerow(["Email", "Password"])
                elif key == "pengguna":
                    writer.writerow(["Email", "Password"])

def clear():
    os.system('cls'if os.name =='nt'else "clear")

def kembali_keMenu():
    print("\n")
    input("Tekan enter untuk kembali")
    menu()

def kembali_keAdmin():
    print("\n")
    input("Tekan enter untuk kembali")
    menu_admin()

def kembali_kePengguna():
    print("\n")
    input("Tekan enter untuk kembali")
    menu_pengguna()

def daftar_pengguna():
    clear()
    print("=" * 53)
    print("|", " " * 12, "DAFTAR PENGGUNA", " " * 20, "|")
    print("=" * 53)
    try:
        # Memuat data dari admin.csv
        data = pd.read_csv(TEMPLATE["pengguna"])
        # Input email dan password baru
        email = input("Masukkan email baru: ")
        if email in data["Email"].values:
            print("\nEmail sudah terdaftar. Gunakan email lain.\n")
            return

        password = input("Masukkan password baru: ")
        confirm_password = input("Konfirmasi password baru: ")

        if password != confirm_password:
            print("\nPassword tidak cocok. Silakan coba lagi.\n")
            return
        # Menambahkan data baru ke file admin.csv
        with open(TEMPLATE["pengguna"], "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([email, password])
        print("Pengguna berhasil ditambahkan!")
        kembali_keMenu()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def pengguna():
    clear()
    print("=" * 53)
    print("|", " " * 10, "PENGGUNA LOGIN", " " * 23, "|")
    print("=" * 53)

    try:
        # Membuka file CSV dengan mode 'r' (read)
        with open(TEMPLATE["pengguna"], 'r') as file:
            reader = csv.reader(file)

            # Skip header (jika ada)
            next(reader)

            # Variabel untuk menghitung jumlah percobaan
            maks_percobaan = 3
            attempts = 0

            # Input email dan password
            while attempts < maks_percobaan:
                email = input("Masukkan email: ").strip()  # Menghapus spasi tambahan
                password = input("Masukkan password: ").strip()  # Menghapus spasi tambahan

                # Membaca setiap baris dalam CSV untuk memeriksa kecocokan email dan password
                login_berhasil = False  # Variabel penanda jika login berhasil
                for row in reader:
                    # Periksa kecocokan email dan password
                    if row[0].strip() == email and row[1].strip() == password:
                        login_berhasil = True
                        break
                if login_berhasil:
                    menu_pengguna()  # Memanggil menu() jika login berhasil
                    return  # Keluar dari fungsi setelah login berhasil
                else:
                    attempts += 1
                    print(f"\nPassword atau email salah. Percobaan ke-{attempts} dari {maks_percobaan}.\n")
                    file.seek(0)  # Mengembalikan ke awal file CSV untuk percakapan berikutnya
                    next(reader)  # Lewati header lagi

            # Jika gagal 3 kali, panggil fungsi daftar_admin
            print("\nAnda telah gagal login sebanyak 3 kali.")
            print("Silakan daftar pengguna baru.")
            daftar_pengguna()

    except FileNotFoundError:
        print("File pengguna.csv tidak ditemukan. Silahkan buat file pengguna.csv terlebih dahulu.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def daftar_admin():
    clear()
    print("=" * 50)
    print("|", " " * 12, "DAFTAR ADMIN", " " * 20, "|")
    print("=" * 50)
    try:
        # Memuat data dari admin.csv
        data = pd.read_csv(TEMPLATE["admin"])


        # Input email dan password baru
        email = input("Masukkan email baru: ")
        if email in data["Email"].values:
            print("\nEmail sudah terdaftar. Gunakan email lain.\n")
            return

        password = input("Masukkan password baru: ")
        confirm_password = input("Konfirmasi password baru: ")

        if password != confirm_password:
            print("\nPassword tidak cocok. Silakan coba lagi.\n")
            return

        # Menambahkan data baru ke file admin.csv
        with open(TEMPLATE["admin"], "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([email, password])
        print("Admin berhasil ditambahkan!")
        kembali_keMenu()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def admin():
    clear()
    print("=" * 50)
    print("|", " " * 10, "ADMIN LOGIN", " " * 23, "|")
    print("=" * 50)

    try:
        # Membuka file CSV dengan mode 'r' (read)
        with open(TEMPLATE["admin"], 'r') as file:
            reader = csv.reader(file)

            # Skip header (jika ada)
            next(reader)

            # Variabel untuk menghitung jumlah percobaan
            max_attempts = 3
            attempts = 0

            # Input email dan password
            while attempts < max_attempts:
                email = input("Masukkan email: ").strip()  # Menghapus spasi tambahan
                password = input("Masukkan password: ").strip()  # Menghapus spasi tambahan

                # Membaca setiap baris dalam CSV untuk memeriksa kecocokan email dan password
                login_berhasil = False  # Variabel penanda jika login berhasil
                for row in reader:
                    # Periksa kecocokan email dan password
                    if row[0].strip() == email and row[1].strip() == password:
                        login_berhasil = True
                        break

                if login_berhasil:
                    print("\nLogin berhasil!\n")
                    menu_admin()  # Memanggil menu() jika login berhasil
                    return  # Keluar dari fungsi setelah login berhasil
                else:
                    attempts += 1
                    print(f"\nPassword atau email salah. Percobaan ke-{attempts} dari {max_attempts}.\n")
                    file.seek(0)  # Mengembalikan ke awal file CSV untuk percakapan berikutnya
                    next(reader)  # Lewati header lagi

            # Jika gagal 3 kali, panggil fungsi daftar_admin
            print("\nAnda telah gagal login sebanyak 3 kali.")
            print("Silakan daftar admin baru.")
            daftar_admin()

    except FileNotFoundError:
        print("File admin.csv tidak ditemukan. Silahkan buat file admin.csv terlebih dahulu.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def edit_pasien():
    clear()
    print("="*84)
    print("|"," "*30,"UPDATE DATA PASIEN"," "*30,"|")
    print("="*84)
    try:
        # Memuat data dari pasien.csv
        data = pd.read_csv(TEMPLATE["pasien"])
        data.index = range(1, len(data) + 1)  # Mengatur indeks mulai dari 1
        print(data)

        # Memilih indeks pasien yang ingin diedit
        while True:
            try:
                pilih_pasien = int(input("Masukkan nomor pasien yang ingin diedit: "))
                if 1 <= pilih_pasien <= len(data):
                    break
                else:
                    print("Indeks tidak valid, coba lagi!")
            except ValueError:
                print("Masukkan angka yang valid!")

        # Menampilkan data pasien yang dipilih
        print("\nData pasien yang dipilih:")
        print(data.loc[pilih_pasien])

        # Simpan nama lama untuk pembaruan antrian
        nama_lama = data.loc[pilih_pasien, 'Nama']

        # Input data baru
        print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
        nama = input(f"Nama ({data.loc[pilih_pasien, 'Nama']}): ") or data.loc[pilih_pasien, 'Nama']
        while True:
            try:
                umur = input(f"Umur ({data.loc[pilih_pasien, 'Umur']}): ")
                umur = int(umur) if umur else data.loc[pilih_pasien, 'Umur']
                break
            except ValueError:
                print("Umur harus berupa angka!")

        alamat = input(f"Alamat ({data.loc[pilih_pasien, 'Alamat']}): ") or data.loc[pilih_pasien, 'Alamat']

        # Poli, Keluhan, dan Obat tidak berubah
        poli = data.loc[pilih_pasien, 'Poli']
        keluhan = data.loc[pilih_pasien, 'Keluhan']
        ruangan = data.loc[pilih_pasien, 'Ruangan']
        obat = data.loc[pilih_pasien, 'Obat']

        # Memperbarui data
        data.loc[pilih_pasien] = [nama, umur, alamat, poli, keluhan, ruangan, obat]

        # Menyimpan data kembali ke pasien.csv
        data.to_csv(TEMPLATE["pasien"], index=False)

        # Perbarui nama di file antrian.csv
        antrian_data = pd.read_csv(TEMPLATE["antrian"])
        antrian_data['Nama Pasien'] = antrian_data['Nama Pasien'].replace(nama_lama, nama)
        antrian_data.to_csv(TEMPLATE["antrian"], index=False)

        print("\nData pasien berhasil diperbarui!")
    except FileNotFoundError:
        print("File pasien.csv tidak ditemukan.")
    kembali_keAdmin()


def hapus_pasien():
    try:
            print("\n"+"="*100)
            print("|", " "*40,"DELETE PASIEN"," "*39, "|")
            print("="*100)
            data = pd.read_csv(TEMPLATE["pasien"])
            data.index = range(1, len(data) + 1)  # Mengatur indeks mulai dari 1
            print(data)

            while True:
                try:
                    indeks = int(input("Masukkan nomor pasien yang ingin dihapus: "))
                    if 1 <= indeks <= len(data):
                        break
                    else:
                        print("Indeks tidak valid, coba lagi!")
                except ValueError:
                    print("Masukkan angka yang valid!")

            # Menampilkan data dokter yang dipilih untuk dihapus
            print("\nData pasien yang dipilih untuk dihapus:")
            print(data.loc[indeks])

            # Konfirmasi penghapusan
            konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ").lower()
            if konfirmasi == 'y':
                # Hapus data berdasarkan indeks
                data = data.drop(index=indeks)
                data.index = range(1, len(data) + 1)  # Mengatur ulang indeks
                data.to_csv(TEMPLATE["pasien"], index=False)  # Menyimpan kembali ke file
                print("\nData pasien berhasil dihapus!")
            else:
                print("\nPenghapusan dibatalkan.")
    except FileNotFoundError:
            print("File pasien.csv tidak ditemukan.")
    except pd.errors.EmptyDataError:
            print("File pasien.csv kosong.")
    except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    kembali_keAdmin()

def antrian():
    clear()
    print("="*50)
    print("|"," "*10,"ANTRIAN PASIEN"," "*20,"|")
    print("="*50)
    data = pd.read_csv('antrian.csv')
    # Mengatur indeks mulai dari 1
    data.index = range(1, len(data) + 1)
    # Menampilkan data
    print(data)
    print("\n"+"="*50)
    kembali_keAdmin()  


def riwayat_penyakit():
    clear()
    print("=" * 50)
    print("|", " " * 10, "RIWAYAT PENYAKIT PASIEN", " " * 15, "|")
    print("=" * 50)
    
    try:
        # Memuat data dari pasien.csv
        data = pd.read_csv(TEMPLATE["pasien"])
        data.index = range(1, len(data) + 1)  # Mengatur indeks mulai dari 1
        
        # Menampilkan data riwayat penyakit
        print(data[['Nama', 'Poli', 'Keluhan']])  # Menampilkan nama, poli, dan keluhan
        print("=" * 50)
        
        kembali_kePengguna()  # Kembali ke menu pengguna
    except FileNotFoundError:
        print("File pasien.csv tidak ditemukan.")
        kembali_kePengguna()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        kembali_kePengguna()

###tambah pasien dari admin###
def tambah_pasien1():
    clear()
    print("="*54)
    print("|"," "*15,"TAMBAH PASIEN", " "*20,"|")
    print("="*54)
    nama = input("Masukkan nama: ")
    while True:
        try:
            umur = int(input("Masukkan umur: "))
            break
        except ValueError:
            print("Umur harus berupa angka!")

    alamat = input("Masukkan alamat: ")
    print("=" * 5, "Pilihan Poli", "=" * 5)
    print("1. GIGI")
    print("2. MATA")
    print("3. THT")
    print("4. UMUM")

    poli_dict = {
        "1": ("GIGI", ["Gigi berlubang", "Sariawan", "Plak gigi"]),
        "2": ("MATA", ["Mata kering", "Katarak", "Bintitan"]),
        "3": ("THT", ["Infeksi telinga", "Alergi", "Radang amandel"]),
        "4": ("UMUM", ["Demam", "Flu", "Diare"]),
    }

    while True:
        poli = input("Pilih poli (1/2/3/4): ")
        if poli in poli_dict:
            poli_name, keluhan_list = poli_dict[poli]
            break
        else:
            print("Pilihan poli tidak valid!")

    clear()
    print(f"=====POLI {poli_name.upper()}=====")
    for i, keluhan_item in enumerate(keluhan_list, start=1):
        print(f"{i}. {keluhan_item}")

    while True:
        try:
            pilih_keluhan = int(input("Masukkan pilihan keluhan (1/2/3): ")) - 1
            keluhan = keluhan_list[pilih_keluhan]
            break
        except (ValueError, IndexError):
            print("Pilihan harus benar!")

    obat_resep = {
        "Gigi berlubang": "Ibuprofen",
        "Sariawan": "Antibiotik",
        "Plak gigi": "Antiseptik",
        "Mata kering": "Insto Cool",
        "Katarak": "Lanosterol",
        "Bintitan": "Chloramphenicol",
        "Infeksi telinga": "Santadex Ear",
        "Alergi": "Antihistamin",
        "Radang amandel": "Amoxicillin",
        "Demam": "Paracetamol",
        "Flu": "Demacolin",
        "Diare": "Oralit",
    }

    obat = obat_resep.get(keluhan, "Tidak diketahui")

    # Menanyakan apakah pasien membutuhkan rawat inap
    print("\nApakah pasien membutuhkan rawat inap?")
    print("1. Ya")
    print("2. Tidak")
    rawat_inap = input("Pilih opsi (1/2): ")

    ruang = "Tidak membutuhkan rawat inap"
    if rawat_inap == "1":
        clear()
        daftar_ruang = ["Ruang A", "Ruang B", "Ruang C", "Ruang D"]
        print("===== DAFTAR RUANG RAWAT INAP =====")
        for i, r in enumerate(daftar_ruang, start=1):
            print(f"{i}. {r}")

        while True:
            try:
                pilih_ruang = int(input("Pilih ruangan (1/2/3/4): ")) - 1
                ruang = daftar_ruang[pilih_ruang]
                break
            except (ValueError, IndexError):
                print("Pilihan tidak valid!")

        # Menyimpan informasi ke ruang.csv
        with open(TEMPLATE["ruang"], "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([ruang, nama])
    elif rawat_inap == "2":
        ruang = "Tidak membutuhkan rawat inap"
    else:
        print("Pilihan tidak valid, dianggap tidak membutuhkan rawat inap.")

    # Menambahkan ke file CSV
    with open(TEMPLATE["pasien"], "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([nama, umur, alamat, poli_name, keluhan, ruang, obat])

    # Menambahkan pasien ke antrean
    with open(TEMPLATE["antrian"], "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([poli_name, nama])

    # Menyimpan resep obat berdasarkan keluhan
    with open(TEMPLATE["resep"], "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([nama, obat])

    print("Pasien berhasil ditambahkan!")
    kembali_keAdmin()

    ###tambah pasien dari pengguna###
def tambah_pasien2():
    clear()
    print("="*54)
    print("|"," "*15,"TAMBAH PASIEN", " "*20,"|")
    print("="*54)
    nama = input("Masukkan nama: ")
    while True:
        try:
            umur = int(input("Masukkan umur: "))
            break
        except ValueError:
            print("Umur harus berupa angka!")

    alamat = input("Masukkan alamat: ")
    print("=" * 5, "Pilihan Poli", "=" * 5)
    print("1. GIGI")
    print("2. MATA")
    print("3. THT")
    print("4. UMUM")

    poli_dict = {
        "1": ("GIGI", ["Gigi berlubang", "Sariawan", "Plak gigi"]),
        "2": ("MATA", ["Mata kering", "Katarak", "Bintitan"]),
        "3": ("THT", ["Infeksi telinga", "Alergi", "Radang amandel"]),
        "4": ("UMUM", ["Demam", "Flu", "Diare"]),
    }

    while True:
        poli = input("Pilih poli (1/2/3/4): ")
        if poli in poli_dict:
            poli_name, keluhan_list = poli_dict[poli]
            break
        else:
            print("Pilihan poli tidak valid!")

    clear()
    print(f"=====POLI {poli_name.upper()}=====")
    for i, keluhan_item in enumerate(keluhan_list, start=1):
        print(f"{i}. {keluhan_item}")

    while True:
        try:
            pilih_keluhan = int(input("Masukkan pilihan keluhan (1/2/3): ")) - 1
            keluhan = keluhan_list[pilih_keluhan]
            break
        except (ValueError, IndexError):
            print("Pilihan harus benar!")

    obat_resep = {
        "Gigi berlubang": "Ibuprofen",
        "Sariawan": "Antibiotik",
        "Plak gigi": "Antiseptik",
        "Mata kering": "Insto Cool",
        "Katarak": "Lanosterol",
        "Bintitan": "Chloramphenicol",
        "Infeksi telinga": "Santadex Ear",
        "Alergi": "Antihistamin",
        "Radang amandel": "Amoxicillin",
        "Demam": "Paracetamol",
        "Flu": "Demacolin",
        "Diare": "Oralit",
    }

    obat = obat_resep.get(keluhan, "Tidak diketahui")

    # Menanyakan apakah pasien membutuhkan rawat inap
    print("\nApakah pasien membutuhkan rawat inap?")
    print("1. Ya")
    print("2. Tidak")
    rawat_inap = input("Pilih opsi (1/2): ")

    ruang = "Tidak membutuhkan rawat inap"
    if rawat_inap == "1":
        clear()
        daftar_ruang = ["Ruang A", "Ruang B", "Ruang C", "Ruang D"]
        print("===== DAFTAR RUANG RAWAT INAP =====")
        for i, r in enumerate(daftar_ruang, start=1):
            print(f"{i}. {r}")

        while True:
            try:
                pilih_ruang = int(input("Pilih ruangan (1/2/3/4): ")) - 1
                ruang = daftar_ruang[pilih_ruang]
                break
            except (ValueError, IndexError):
                print("Pilihan tidak valid!")

        # Menyimpan informasi ke ruang.csv
        with open(TEMPLATE["ruang"], "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([ruang, nama])
    elif rawat_inap == "2":
        ruang = "Tidak membutuhkan rawat inap"
    else:
        print("Pilihan tidak valid, dianggap tidak membutuhkan rawat inap.")

    # Menambahkan ke file CSV
    with open(TEMPLATE["pasien"], "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([nama, umur, alamat, poli_name, keluhan, ruang, obat])

    # Menambahkan pasien ke antrean
    with open(TEMPLATE["antrian"], "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([poli_name, nama])

    # Menyimpan resep obat berdasarkan keluhan
    with open(TEMPLATE["resep"], "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([nama, obat])

    print("Pasien berhasil ditambahkan!")
    kembali_kePengguna()


def daftar_pasien():
    clear()
    print("\n"+"="*100)
    print("|", " "*40,"CRUD PASIEN"," "*43, "|")
    print("="*100)
    data = pd.read_csv('pasien.csv')
    # Mengatur indeks mulai dari 1
    data.index = range(1, len(data) + 1)
    # Menampilkan data
    print(data)
    print("\n"+"="*100)
    print("1. Tambah pasien")
    print("2. Edit pasien")
    print("3. Hapus pasien")
    print("4. Kembali")
    print("5. Keluar")

    opsi = input("\nPilih opsi: ")
    for i in opsi:
        if i =="1":
            tambah_pasien1()
        elif i == "2":
            edit_pasien()
        elif i == "3":
            hapus_pasien()
        elif i =="4":
            menu_admin()
        elif opsi =="5":
            menu()
        else:
            print("Pilihan tidak valid")


#################################-------DOKTER------###############################################

def daftar_dokter():
    clear()
    # dokter()
    print("\n"+"="*101)
    print("|", " "*40,"CRUD DOKTER"," "*44, "|")
    print("="*101)
    data = pd.read_csv('dokter.csv')
    # Mengatur indeks mulai dari 1
    data.index = range(1, len(data) + 1)
    # Menampilkan data
    print(data)
    print("=" * 101)
    print("1. Tambah Dokter")
    print("2. Edit Dokter")
    print("3. Hapus Dokter")
    print("4. Kembali")


    opsi = input("\nPilih opsi (1/2/3/4): ")
    if opsi == "1":
        tambah_dokter()
    elif opsi == "2":
        edit_dokter()
    elif opsi == "3":
        hapus_dokter()
    elif opsi == "4":
        menu_admin()
    else:
        print("Pilihan tidak valid!")
        daftar_dokter()
        # dokter()

def tambah_dokter():
    clear()
    print("\n"+"="*100)
    print("|", " "*40,"TAMBAH DOKTER"," "*41, "|")
    print("="*100)
    try:
        # Daftar poli sebagai list
        daftar_poli = ["GIGI", "MATA", "THT", "UMUM"]

        # Menampilkan daftar poli
        print("Pilih Poli:")
        for index, poli in enumerate(daftar_poli, start=1):
            print(f"{index}. {poli}")

        # Meminta input pengguna untuk memilih poli
        while True:
            try:
                pilihan = int(input("Masukkan nomor poli (1/2/3/4): ")) - 1
                if 0 <= pilihan < len(daftar_poli):
                    poli = daftar_poli[pilihan]
                    break
                else:
                    print("Pilihan tidak valid! Harap masukkan nomor yang sesuai.")
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")

        # Input nama dokter
        dokter = input("Masukkan nama Dokter: ").strip()

        if dokter:
            # Menyimpan data dokter baru ke file CSV
            with open(TEMPLATE["dokter"], "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([poli, dokter])
            print("\nDokter berhasil ditambahkan!")
        else:
            print("\nNama dokter tidak boleh kosong!")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    kembali_keAdmin()

def edit_dokter():
    clear()
    print("\n"+"="*100)
    print("|", " "*40,"UPDATE DOKTER"," "*40, "|")
    print("="*100)
    try:
        data = pd.read_csv(TEMPLATE["dokter"])
        data.index = range(1, len(data) + 1)  # Mengatur indeks mulai dari 1
        print(data)

        while True:
            try:
                pilih_dokter = int(input("Masukkan nomor dokter yang ingin diedit: "))
                if 1 <= pilih_dokter <= len(data):
                    break
                else:
                    print("Indeks tidak valid, coba lagi!")
            except ValueError:
                print("Masukkan angka yang valid!")

        # Menampilkan data dokter yang dipilih
        print("\nData dokter yang dipilih:")
        print(data.loc[pilih_dokter])

        # Input data baru
        print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
        poli = input(f"Poli ({data.loc[pilih_dokter, 'Poli']}): ") or data.loc[pilih_dokter, 'Poli']
        dokter = input(f"Dokter ({data.loc[pilih_dokter, 'Dokter']}): ") or data.loc[pilih_dokter, 'Dokter']

        # Memperbarui data
        data.loc[pilih_dokter] = [poli, dokter]

        # Menyimpan data kembali ke dokter.csv
        data.to_csv(TEMPLATE["dokter"], index=False)
        print("\nData dokter berhasil diperbarui!")
    except FileNotFoundError:
        print("File dokter.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    kembali_keAdmin()

def hapus_dokter():
    clear()
    try:
            print("\n"+"="*100)
            print("|", " "*40,"DELETE DOKTER"," "*40, "|")
            print("="*100)
            data = pd.read_csv(TEMPLATE["dokter"])
            data.index = range(1, len(data) + 1)  # Mengatur indeks mulai dari 1
            print(data)
            while True:
                try:
                    indeks = int(input("Masukkan nomor dokter yang ingin dihapus: "))
                    if 1 <= indeks <= len(data):
                        break
                    else:
                        print("Indeks tidak valid, coba lagi!")
                except ValueError:
                    print("Masukkan angka yang valid!")

            # Menampilkan data dokter yang dipilih untuk dihapus
            print("\nData dokter yang dipilih untuk dihapus:")
            print(data.loc[indeks])

            # Konfirmasi penghapusan
            konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ").lower()
            if konfirmasi == 'y':
                # Hapus data berdasarkan indeks
                data = data.drop(index=indeks)
                data.index = range(1, len(data) + 1)  # Mengatur ulang indeks
                data.to_csv(TEMPLATE["dokter"], index=False)  # Menyimpan kembali ke file
                print("\nData dokter berhasil dihapus!")
            else:
                print("\nPenghapusan dibatalkan.")
    except FileNotFoundError:
            print("File dokter.csv tidak ditemukan.")
    except pd.errors.EmptyDataError:
            print("File dokter.csv kosong.")
    except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    kembali_keAdmin()


def menu_admin():
    clear()
    init_csv()
    print("Login berhasil!\n")
    print("="*110)
    print("|"," "*45,"SELAMAT DATANG"," "*45,"|")
    print("|"," "*48,"MENU ADMIN"," "*46,"|")
    print("="*110)
    print("|1. DAFTAR PASIEN"," "*90,"|")
    print("|2. DATA DOKTER"," "*92,"|")
    print("|3. ANTRIAN"," "*96,"|")
    print("|4. RIWAYAT PASIEN"," "*89,"|")
    print("|5. KEMBALI", " "*96, "|")
    print("|6. KELUAR"," "*97,"|")
    print("="*110)
    # print("\nSilahkan pilih menu: ")
    opsi_menu = (input("Pilih menu (1/2/3/4/5/6): "))
    for i in opsi_menu:
        # os.system("cls")
        if i == '1':
            daftar_pasien()
        elif i == '2':  
            daftar_dokter()        
        elif i == "3":
            antrian()
        elif i =="4":
            riwayat_penyakit()
        elif i == "5":
            menu()
        elif i == "6": 
            break
        else:
            menu_admin()

def menu_pengguna():
    clear()
    init_csv()
    print("="*110)
    print("|"," "*45,"SELAMAT DATANG"," "*45,"|")
    print("|"," "*46,"MENU PENGGUNA"," "*45,"|")
    print("="*110)
    print("|1. DAFTAR PASIEN"," "*90,"|")
    print("|2. RIWAYAT PENYAKIT"," "*87,"|")
    print("|3. KEMBALI"," "*96,"|")
    print("|4. KELUAR"," "*97,"|")
    print("="*110)
    print("\nSilahkan pilih menu: ")
    opsi_menu = (input("Pilih menu (1/2/3/4): "))
    for i in opsi_menu:
        if i == '1':
            tambah_pasien2()
        elif i == '2':  
            riwayat_penyakit()       
        elif i == '3':  
            menu()        
        elif i == "4": 
                break
        else:
            menu_pengguna()

def menu():
    clear()
    init_csv()
    print("="*110)
    print("|"," "*45,"SELAMAT DATANG"," "*45,"|")
    print("="*110)
    print("|1. LOGIN ADMIN"," "*92,"|")
    print("|2. LOGIN PENGGUNA"," "*89,"|")
    print("|3. DAFTAR ADMIN"," "*91,"|")
    print("|4. DAFTAR PENGGUNA"," "*88,"|")
    print("|5. KELUAR"," "*97,"|")
    print("="*110)
    print("\nSilahkan pilih menu: ")
    opsi_menu = (input("Pilih menu (1/2/3/4/5): "))
    for i in opsi_menu:
        # os.system("cls")
        if i == '1':
            admin()
        elif i == '2':  
            pengguna()
        elif i == '3':
            daftar_admin()
        elif i == "4":
            daftar_pengguna()        
        elif i == "5": 
                break
        else:
            menu()
menu()
