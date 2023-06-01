#Program GUI untuk voting pilpres

import tkinter as tk

def hitung_klik_1():
    global counter_1
    counter_1 += 1
    label_1["text"] = "Jumlah pemilih : " + str(counter_1)

def hitung_klik_2():
    global counter_2
    counter_2 += 1
    label_2["text"] = "Jumlah pemilih : " + str(counter_2)

counter_1 = 0
counter_2 = 0

window = tk.Tk()
window.title("Aplikasi Voting")

question_label = tk.Label(window, text="Tentukan presiden yang ingin anda pilih!")
question_label.pack()

button_1 = tk.Button(window, text="Ganjar", command=hitung_klik_1)
button_1.pack()

label_1 = tk.Label(window, text="Jumlah pemilih : 0")
label_1.pack()

button_2 = tk.Button(window, text="Prabowo", command=hitung_klik_2)
button_2.pack()

label_2 = tk.Label(window, text="Jumlah pemilih : 0")
label_2.pack()

window.mainloop()
