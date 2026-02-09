#!/usr/bin/env python3

print("Enter the first number:")
st_num = int(input())
print("Enter the second number:")
nd_num = int(input())
mul = st_num * nd_num
print(str(st_num)+" "+"x"+" "+str(nd_num)+" "+"="+" "+str(mul))
if(mul>0):
    print("The result is positive")
elif(mul<0):
    print("The result is negative")
else:
    print("The result is positive and negative")
