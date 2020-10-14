# Program 5

import tkinter as tk

top = tk.Tk()

def Palindrome(stringIn):
    sAwal = ""
    sReverse = ""
    sProses = stringIn.lower() #lowercase input
    # get only alphabet char
    for char in sProses:
        if ord(char) >= 97 and ord(char) <= 122:
            sAwal = sAwal + char

    sReverse = sAwal[::-1] #reverse string
    #check palindrome
    palindrome = True if sReverse == sAwal else False
    return palindrome

def onClick():
    stringIn = E1.get()
    result = Palindrome(stringIn)
    if result == True:
        var.set("Palindrome")
    else:
        var.set("Bukan Palindrome")

# input box
E1 = tk.Entry(top, bd =5)
E1.pack()

# button palindrome
B1 = tk.Button(top, text ="Palindrome Check", command = onClick)
B1.pack()

# label
var = tk.StringVar()
label1 = tk.Label(top, textvariable=var)
var.set("")
label1.pack()

top.mainloop()
