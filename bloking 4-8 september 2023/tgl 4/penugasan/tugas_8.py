umur = int(input("Masukkan umur Anda: "))

if umur < 10:
    print("Anda masih anak-anak.")
elif umur < 18:
    print("Anda masih remaja.")
elif umur < 35:
    print("Anda sudah dewasa.")
elif umur < 65:
    print("Anda sudah paruhbaya.")
else:
    print("Anda sudah tua.")
