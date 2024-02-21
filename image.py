import tkinter as tk

window = tk.Tk()
window.title("Hello - Nuril Izza")
salam = tk.Label(text="Anyeong yeorobun", fg="black", bg="pink") 
logo = tk.PhotoImage(file="songkang.gif") 
WLableImage = tk.Label(image=logo)
salam.pack()
WLableImage.pack()

window.mainloop()