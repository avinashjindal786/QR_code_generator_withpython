
from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

window = Tk()
window.title("QR Generator")

# coed generator

def generator():
    if len(subject.get()) !=0:
        global  myQr
        myQr = pyqrcode.create(subject.get())
        qrImage = myQr.xbm(scale=6)
        global  photo
        photo = BitmapImage(data=qrImage)
    else:
        messagebox.showinfo("Error!","Please Enter the Subject")
    try:
        showCode()
    except:
        pass


# code showing

def showCode():
    global photo
    notificationLabel.config(image = photo)
    subLabel.config(text = "Showing Qr code" + subject.get())

def save():

    dir = path1 = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) !=0:
            qrImage = myQr.png(os.path.join(dir,name.get()+".png"),scale =6)
        else:
            messagebox.showinfo("Error!","File name can not be empty!")
    except:
        messagebox.showinfo("Error!","please generate code first")

lab1 = Label(window,text="enter subject", font =("Helvetica,12"))
lab1.grid(row=0,column=0,sticky =N + S+ E +W)

lab2 = Label(window,text="enter file name", font =("Helvetica,12"))
lab2.grid(row=1,column=0,sticky =N + S+ E +W)

subject = StringVar()
subjectEntry = Entry(window, textvariable=subject, font =("Helvetica,12"))
subjectEntry.grid(row=0,column=1,sticky =N + S+ E +W)

name = StringVar()
nameEntry = Entry(window, textvariable =name, font =("Helvetica,12"))
nameEntry.grid(row=1,column=1,sticky =N + S+ E +W)

createButton = Button(window, text ="create QR code", font =("Helvetica,12"), width = 15, command = generator )
createButton.grid(row=0,column=3,sticky =N + S+ E +W)

notificationLabel = Label(window)
notificationLabel.grid(row=2,column=1,sticky =N + S+ E +W)

subLabel = Label(window, text = "")
subLabel.grid(row=3,column=1,sticky =N + S+ E +W)

showButton = Button(window, text = "save in png", font =("Helvetica,12"), width = 15, command = save )
showButton.grid(row=1,column=3,sticky =N + S+ E +W)

totalRows = 3
totalcols = 3

for row in range(totalRows+1):
    window.grid_rowconfigure(row,weight=1)
for cols in range(totalcols+1):
    window.grid_columnconfigure(cols,weight=1)

window.mainloop()