import random
import string
import re
i = 0
generatedpass = ""

def generate(length):
    generatedpass = string.ascii_letters+ string.digits+ string.punctuation
    userPassword=''.join(random.choice(generatedpass) for x in range(int(length)))
    return userPassword


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
    return converttoword


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


userPreferNumber = int(input("Please Enter choose Length of password : "))

userPass = generate(userPreferNumber)
print("Password for user :",userPass)

encryptedPass = encrypt(userPass)
print("Encryped Password for user:",encryptedPass)

decryptedPass = decrypt(encryptedPass)

print("Decryped Password for user:",decryptedPass)


