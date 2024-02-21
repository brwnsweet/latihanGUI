import tkinter as tk

def vol_kubus():
    s = int(entry_sisi.get())
    volume = s ** 3
    hasil.config(text=f"Volume Kubus : {volume}")

wdw = tk.Tk()
wdw.title("Hello - Nuril izza")

lbl_sisi = tk.Label(wdw, text="Input sisi kubus :", fg="black", bg="pink")
lbl_sisi.pack(pady=5)

entry_sisi = tk.Entry(wdw)
entry_sisi.pack(pady=5)

hitung = tk.Button(wdw, text="count", command=vol_kubus, bg="pink", fg="black")
hitung.pack(pady=6)

# hasil
hasil = tk.Label(wdw, text="", bg="pink", fg="black")
hasil.pack()
wdw.mainloop()
