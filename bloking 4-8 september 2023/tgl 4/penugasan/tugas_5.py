string = ""
bar = 1

print("Segitiga Bintang Siku-siku3")
x = int(input("Masukkan Jumlah Baris :"))

while bar <= x:
	kol = bar

	while kol > 0:
		string = string + " * "
		kol = kol - 1
		
	string = string + "\n"
	bar = bar + 1
print (string)