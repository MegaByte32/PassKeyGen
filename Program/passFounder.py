import random

def passKeyGen():

    '''
    Name:        passFounder
    Purpose:     Password random generator (length 16)
    Author:      MegaByte
    Editor:      Soliman2020
    Created:     07/12/2021
    Updated:     09/12/2021
    Copyright:   (c) MegaByte 2021
    Licence:     <your licence>
    '''

    passW = ""

    for i in range(0, 16):
        tmp = random.randint(1, 4)  # using 1 instead of 0 to keep the output passW length 16.
        if tmp == 1:
            index = random.randint(0, len(txt_Lower)-1)   # length-1 to avoid IndexError: list index out of range
            passW = passW + (txt_Lower[index])
        if tmp == 2:
            index = random.randint(0, len(txt_Upper)-1)   # length-1 to avoid IndexError: list index out of range
            passW = passW + (txt_Upper[index])
        if tmp == 3:
            index = random.randint(0, len(txt_Int)-1)     # length-1 to avoid IndexError: list index out of range
            passW = passW + (txt_Int[index])
        if tmp == 4:
            index = random.randint(0, len(txt_Symbol)-1)  # length-1 to avoid IndexError: list index out of range
            passW = passW + (txt_Symbol[index])
    print("Your password is",passW)


txt_Lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
txt_Upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
txt_Int = ["0","1","2","3","4","5","6","7","8","9"]
txt_Symbol = ["£","$","%","^","&","*","(",")","_","-","+","=","[","]","{","}","'","@",":",";","#","~","?","|",".",","]
tmp = 0
index = 0

passKeyGen()
