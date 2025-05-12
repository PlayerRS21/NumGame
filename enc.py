import random

import time

import os

random_characters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",",",'"',"'",".",";",":","<",">","?","/","[","]","{","}","|","-","_","+","="]

subsituation = [")","!","@","#","$","%","^","&","*","(",")"]

def decrypt(word):

    for i in range(0,len(word)):

        if word[i] in random_characters:

            # print("Enter Correct Code to Decode it...")

            print("Error")
            
        else:

            lv1_word = ""

            for i in range(0,len(word)):

                lv1_word = lv1_word + str(subsituation.index(word[i]))

            # print(lv1_word)  # lv3_word  =  4644 {23 08 13 20 37} 1235

            lv2_word = ""

            for i in range(4,len(lv1_word)-4):

                lv2_word = lv2_word + lv1_word[i]

            # print(lv2_word) #Trimmed Word 23 08 13 20 37

            lv3_word = [lv2_word[i:i+2] for i in range(0, len(lv2_word),2)]

            # print(lv3_word)

            lv4_word=""

            for i in range(0,len(lv3_word)): #  ['23', '08', '13', '20', '37']

                if int(lv3_word[i][0]) == 0:

                    lv4_word += random_characters[int(lv3_word[i][1])]

                else:

                    lv4_word += random_characters[int(lv3_word[i])]

            # print(lv4_word)

            lv5_word = ""

            lv5_word += lv4_word[-1]

            for i in range(1,len(lv4_word)-1):

                lv5_word += lv4_word[i]

            lv5_word += lv4_word[0]

            return lv5_word


def encrypt(word):

    for i in range(0,len(word)):

        if word[i] in subsituation:

            print("Error")

        else:

            lv1_word = ""

            lv1_word = word[-1]

            for i in range(1,len(word)-1):

                lv1_word = lv1_word+word[i]

            lv1_word = lv1_word + word[0]

            # print(lv1_word)

            lv2_word = f"{random.choice(random_characters)}{random.choice(random_characters)}{lv1_word}{random.choice(random_characters)}{random.choice(random_characters)}"

            # print(lv2_word)

            lv3_word = ""

            for i in range(0,len(lv2_word)):

                if lv2_word[i] in random_characters:

                    if random_characters.index(lv2_word[i])<10:

                        lv3_word = lv3_word +"0"+ str(random_characters.index(lv2_word[i]))

                    else:

                        lv3_word = lv3_word + str(random_characters.index(lv2_word[i]))

            # return lv3_word

            lv4_word = ""

            for i in range (0,len(lv3_word)):

                value=int(lv3_word[i])

                lv4_word = f"{lv4_word}{subsituation[value]}"

            return lv4_word

pswd ="&)!(!&!*)$@)@($)"

ps="^@!!!&!*)$@)!@)%"

# user = "user"

# print(encrypt(user))

print(decrypt(pswd))

print(decrypt(ps))