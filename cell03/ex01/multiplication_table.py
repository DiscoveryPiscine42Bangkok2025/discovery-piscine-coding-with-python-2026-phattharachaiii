#!/usr/bin/env python3

print("Enter a number")
usr_input = int(input())

i = 0
for i in range(13):
    mul = str(usr_input*i)
    print(str(i)+" "+"x"+" "+str(usr_input)+" "+"="+" "+mul)
