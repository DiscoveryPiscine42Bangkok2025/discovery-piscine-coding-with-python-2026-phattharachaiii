#!/usr/bin/env python3

def add_one(number):
    number += 1
    print("Inside method:", number)

value = 10
print("Before method:", value)
add_one(value)
print("After method:", value)
