import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# List untuk menyimpan data nasabah
data_nasabah = []

def hitung_saldo():
    try:
        nama = entry_nama.get().strip()
        norek = entry_norek.get().strip()
        saldo_awal = float(entry_saldo.get())
        setor = float(entry_setor.get())
        tarik = float(entry_tarik.get())
        tanggal = entry_tanggal.get().strip()

        # Validasi input wajib
        if not nama or not norek or not tanggal:
            messagebox.showwarning("Peringatan", "Semua kolom wajib diisi!")
            return

        # Validasi format tanggal
        try:
            datetime.strptime(tanggal, "%d-%m-%Y")
        except ValueError:
            messagebox.showerror("Error", "Format tanggal salah! Gunakan dd-mm-yyyy.")
            return

        if setor < 0 or tarik < 0 or saldo_awal < 0:
            messagebox.showerror("Error", "Nilai tidak boleh negatif!")
            return

        if tarik > saldo_awal + setor:
            messagebox.showerror("Error", "Penarikan melebihi saldo yang tersedia!")
            return

        # Cek duplikasi no rekening
        for nasabah in data_nasabah:
            if nasabah['norek'] == norek:
                messagebox.showerror("Error", "No. rekening sudah terdaftar!")
                return

        saldo_akhir = saldo_awal + setor - tarik

        # Simpan data ke list
        nasabah = {
            "nama": nama.lower(),
            "norek": norek,
            "tanggal": tanggal,
            "saldo_awal": saldo_awal,
            "setor": setor,
            "tarik": tarik,
            "saldo_akhir": saldo_akhir
        }
        data_nasabah.append(nasabah)

        # Tampilkan hasil
        hasil = (
            f"Nama: {nama}\n"
            f"No. Rekening: {norek}\n"
            f"Tanggal Transaksi: {tanggal}\n"
            f"Saldo Awal: Rp {saldo_awal:,.2f}\n"
            f"Setoran: Rp {setor:,.2f}\n"
            f"Penarikan: Rp {tarik:,.2f}\n"
            f"Saldo Akhir: Rp {saldo_akhir:,.2f}"
        )

        messagebox.showinfo("Informasi Rekening", hasil)

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid pada saldo, setoran, dan tarikan!")

def cari_nasabah():
    keyword = entry_cari.get().lower().strip()
    if not keyword:
        messagebox.showwarning("Peringatan", "Masukkan nama atau no. rekening yang ingin dicari!")
        return

    hasil_cari = None
    for nasabah in data_nasabah:
        if keyword == nasabah['nama'] or keyword == nasabah['norek']:
            hasil_cari = nasabah
            break

    if hasil_cari:
        info = (
            f"Nama: {hasil_cari['nama'].title()}\n"
            f"No. Rekening: {hasil_cari['norek']}\n"
            f"Tanggal: {hasil_cari['tanggal']}\n"
            f"Saldo Akhir: Rp {hasil_cari['saldo_akhir']:,.2f}"
        )
        messagebox.showinfo("Data Ditemukan", info)
    else:
        messagebox.showerror("Tidak Ditemukan", "Data nasabah tidak ditemukan!")

def tampilkan_semua_nasabah():
    if not data_nasabah:
        messagebox.showinfo("Info", "Belum ada data nasabah.")
        return

    info = ""
    for i, n in enumerate(data_nasabah, start=1):
        info += (
            f"{i}. {n['nama'].title()} | No Rek: {n['norek']} | "
            f"Saldo Akhir: Rp {n['saldo_akhir']:,.2f}\n"
        )
    messagebox.showinfo("Daftar Nasabah", info)

# --- GUI ---
root = tk.Tk()
root.title("TabunganKu – Simulasi Rekening Sederhana")

# Form Input Data
tk.Label(root, text="Nama Nasabah:").grid(row=0, column=0, sticky="w")
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

tk.Label(root, text="No. Rekening:").grid(row=1, column=0, sticky="w")
entry_norek = tk.Entry(root)
entry_norek.grid(row=1, column=1)

tk.Label(root, text="Saldo Awal (Rp):").grid(row=2, column=0, sticky="w")
entry_saldo = tk.Entry(root)
entry_saldo.grid(row=2, column=1)

tk.Label(root, text="Jumlah Setoran (Rp):").grid(row=3, column=0, sticky="w")
entry_setor = tk.Entry(root)
entry_setor.grid(row=3, column=1)

tk.Label(root, text="Jumlah Tarikan (Rp):").grid(row=4, column=0, sticky="w")
entry_tarik = tk.Entry(root)
entry_tarik.grid(row=4, column=1)

tk.Label(root, text="Tanggal Transaksi (dd-mm-yyyy):").grid(row=5, column=0, sticky="w")
entry_tanggal = tk.Entry(root)
entry_tanggal.grid(row=5, column=1)

btn = tk.Button(root, text="Hitung Saldo", command=hitung_saldo)
btn.grid(row=6, column=0, columnspan=2, pady=10)

# Form Cari Data
tk.Label(root, text="Cari (Nama / No. Rekening):").grid(row=7, column=0, sticky="w")
entry_cari = tk.Entry(root)
entry_cari.grid(row=7, column=1)

btn_cari = tk.Button(root, text="Cari Nasabah", command=cari_nasabah)
btn_cari.grid(row=8, column=0, columnspan=2, pady=5)

# Tombol tampil semua data
btn_semua = tk.Button(root, text="Tampilkan Semua Nasabah", command=tampilkan_semua_nasabah)
btn_semua.grid(row=9, column=0, columnspan=2, pady=5)

root.mainloop()
