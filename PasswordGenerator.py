import random
import string
import re
from tkinter import *

i = 0
generatedpass = ""

def generate():
    length = mylabelBox.get()
    generatedpass = string.ascii_letters+ string.digits+ string.punctuation
    userPassword=''.join(random.choice(generatedpass) for x in range(int(length)))
    # myLabel = Label(root,text=str(userPassword))
    # myLabel.pack()
    mylabelBox2 = Entry(root,textvariable=str(userPassword))
    mylabelBox2.pack()


AsciiPattern = '[a-zA-Z]'

def encrypt(words):
    convert = 0
    converttoword =''
    for x in words:
        if re.match(AsciiPattern,x):
            convert= ord(x)+4
            converttoword = converttoword+ chr(convert)
        else:
            convert = ord(x)+4
            converttoword = converttoword+ chr(convert)
    # return converttoword
    myLabel = Label(root,text=str(converttoword))
    myLabel.pack()

def decrypt(words):
    convert = 0
    converttoword =''
    for x in words:
        if re.match(AsciiPattern,x):
            convert= ord(x)-4
            converttoword = converttoword+ chr(convert)
        else:
            convert = ord(x)-4
            converttoword = converttoword+ chr(convert)
    return converttoword

root = Tk()
myLabel = Label(root,text="Please Enter choose Length of Password:  ")
myLabel.pack()
mylabelBox = Entry(root)
mylabelBox.pack()
myButton = Button(root,text="Generate",command=generate)
myButton.pack()
myButton1 = Button(root,text="Encrypt",command=encrypt)
myButton1.pack()
myButton2 = Button(root,text="Decrypt",command=decrypt)
mylabelBox2 = Entry(root)
mylabelBox2.pack()

# userPreferNumber = int(input("Please Enter choose Length of password : "))





# userPass = generate(userPreferNumber)
# print(userPass)

# encryptedPass = encrypt(userPass)
# print(encryptedPass)

# decryptedPass = decrypt(encryptedPass)

# print(decryptedPass)


root.mainloop()