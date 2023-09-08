while True:
    score = int(input("Masukkan nilai Siswa: "))

    if score >= 75:
        print("Tuntas")
    else:
        print("belum tuntas")
        retake = input("Apakah Anda ingin mengulang? (y/n) ")
        if retake == "y":
            continue
        else:
            print("Selesai")
