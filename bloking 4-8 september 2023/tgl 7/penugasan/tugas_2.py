# Mengimpor modul tkinter
import tkinter as tk

# Membuat jendela utama
window = tk.Tk()
window.title("Program Hitung Parkir")
window.geometry("400x300")

# Membuat label dan entry untuk waktu masuk, no polisi, dan waktu keluar
tk.Label(window, text="Waktu Masuk (format: HH)").grid(
    row=0, column=0, padx=10, pady=10
)
entry_masuk = tk.Entry(window)
entry_masuk.grid(row=0, column=1)

tk.Label(window, text="No Polisi").grid(row=1, column=0, padx=10, pady=10)
entry_polisi = tk.Entry(window)
entry_polisi.grid(row=1, column=1)

tk.Label(window, text="Waktu Keluar (format: HH)").grid(
    row=2, column=0, padx=10, pady=10
)
entry_keluar = tk.Entry(window)
entry_keluar.grid(row=2, column=1)


# Membuat fungsi untuk menghitung biaya parkir
def hitung_parkir():
    # Mendapatkan input dari entry
    masuk = entry_masuk.get()
    polisi = entry_polisi.get()
    keluar = entry_keluar.get()

    # Memeriksa apakah input valid
    if not masuk or not polisi or not keluar:
        output.config(text="Harap isi semua data")
        return

    # Mengubah input menjadi jam
    try:
        jam_masuk = int(masuk)
        jam_keluar = int(keluar)
    except ValueError:
        output.config(text="Format waktu salah")
        return

    # Memeriksa apakah jam valid
    if not (0 <= jam_masuk <= 23 and 0 <= jam_keluar <= 23):
        output.config(text="Jam tidak valid")
        return

    # Menghitung lama parkir dalam menit
    lama_parkir = (jam_keluar - jam_masuk) * 60

    # Memeriksa apakah lama parkir positif
    if lama_parkir <= 0:
        output.config(text="Waktu keluar harus lebih besar dari waktu masuk")
        return

    # Menghitung biaya parkir dengan harga yang sudah ditentukan
    harga_parkir = 2000  # Harga parkir per jam
    biaya_parkir = (
        lama_parkir // 60 + 1
    ) * harga_parkir  # Biaya parkir dibulatkan ke atas per jam

    # Menampilkan hasil perhitungan biaya parkir
    output.config(
        text=f"No Polisi: {polisi}\nLama Parkir: {lama_parkir} menit\nBiaya Parkir: Rp {biaya_parkir}"
    )


# Membuat tombol untuk menjalankan fungsi hitung parkir
button = tk.Button(window, text="Hitung", command=hitung_parkir)
button.grid(row=3, columnspan=2, padx=10, pady=10)

# Membuat label untuk menampilkan output
output = tk.Label(window, text="")
output.grid(row=4, columnspan=2, padx=10, pady=10)

# Menjalankan program
window.mainloop()
