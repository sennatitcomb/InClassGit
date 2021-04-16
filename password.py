from random import *
def password(a):
    for i in range (1, a):
        print(randint(1, 100))

password(int(input("Enter a number: ")))