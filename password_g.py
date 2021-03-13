import random
import hashlib

lines = open('words.txt').read().splitlines()


f = open("passwords.txt","w+")

for x in range(12): #feel free to change number to get more words as password
    myline = random.choice(lines)
    print(myline)
    f.write(myline + ' ')
    

print("Passwords saved in file passwords.txt")
