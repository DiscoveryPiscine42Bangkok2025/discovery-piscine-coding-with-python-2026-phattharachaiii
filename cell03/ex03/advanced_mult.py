#!/usr/bin/env python3

num = 10
index = 12
i = 0
while i <= num:
    x = 0
    print("Table de "+str(i)+": ",end="")
    while x <= index :
        print(str(x*i),end=" ")
        x+=1
    print()
    i+=1


