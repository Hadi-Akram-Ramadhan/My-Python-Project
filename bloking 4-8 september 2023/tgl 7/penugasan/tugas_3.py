import tkinter as tk

window = tk.Tk()
window.title("Data Siswa Baru")
window.configure(bg="green")

title_label = tk.Label(text="DATA SISWA BARU", font=("Arial", 20))
title_label.pack()

# Name
name_label = tk.Label(text="Nama Lengkap:")
name_label.pack()
name_entry = tk.Entry()
name_entry.pack()

# Date of Birth
dob_label = tk.Label(text="Tanggal Lahir:")
dob_label.pack()
dob_entry = tk.Entry()
dob_entry.pack()

# School
school_label = tk.Label(text="Asal Sekolah:")
school_label.pack()
school_entry = tk.Entry()
school_entry.pack()

# Father's Name
father_label = tk.Label(text="NISN:")
father_label.pack()
father_entry = tk.Entry()
father_entry.pack()

# Mother's Name
mother_label = tk.Label(text="Nama Ayah:")
mother_label.pack()
mother_entry = tk.Entry()
mother_entry.pack()

# Phone Number
phone_label = tk.Label(text="Nomor Telepon Ibu:")
phone_label.pack()
phone_entry = tk.Entry()
phone_entry.pack()

# Address
address_label = tk.Label(text="Alamat:")
address_label.pack()
address_entry = tk.Entry(width="80")
address_entry.pack()


def save_data():
    name = name_entry.get()
    dob = dob_entry.get()
    school = school_entry.get()
    father_name = father_entry.get()
    mother_name = mother_entry.get()
    phone_number = phone_entry.get()
    address = address_entry.get()

    # Save data to database or file

    data_label.config(
        text=f"Data yang telah disimpan:\n\nNama: {name}\nTanggal Lahir: {dob}\nAsal Sekolah: {school}\nNISN: {father_name}\nNama Ayah: {mother_name}\nNomor Telepon Ibu: {phone_number}\nAlamat: {address}"
    )


save_button = tk.Button(text="Simpan", command=save_data)
save_button.pack()


def delete_data():
    name_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    school_entry.delete(0, tk.END)
    father_entry.delete(0, tk.END)
    mother_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

    data_label.config(text="")


delete_button = tk.Button(text="Hapus", command=delete_data)
delete_button.pack()

data_label = tk.Label(text="")
data_label.pack()

window.mainloop()
