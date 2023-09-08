from tkinter import *

root = Tk()
root.title("Cashier Program")

price_label = Label(root, text="Harga")
price_label.grid(row=0, column=0)
price_entry = Entry(root)
price_entry.grid(row=0, column=1)

quantity_label = Label(root, text="Kuantitas")
quantity_label.grid(row=1, column=0)
quantity_entry = Entry(root)
quantity_entry.grid(row=1, column=1)


def calculate_total():
    price = float(price_entry.get())
    quantity = int(quantity_entry.get())
    total = price * quantity
    total_label.config(text=f"Total: {total}")


calculate_button = Button(root, text="Hitung Total", command=calculate_total)
calculate_button.grid(row=2, column=0, columnspan=2)

total_label = Label(root, text="Total: ")
total_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
