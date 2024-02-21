import tkinter as tk

def cetak_output():
    nama_depan = e1.get()
    nama_belakang = e2.get()
    output_label.config(text=f" {nama_depan} {nama_belakang}")

master = tk.Tk()
master.title("Input Nama")

tk.Label(master, text="Nama Depan").grid(row=0)
tk.Label(master, text="Nama Belakang").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

output_label = tk.Label(master, text="")
output_label.grid(row=2, columnspan=2)

tombol_cetak = tk.Button(master, text="Cetak", command=cetak_output)
tombol_cetak.grid(row=3, columnspan=2)

master.mainloop()
