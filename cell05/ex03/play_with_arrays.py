#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]

result = set()
for value in original:
    if value > 5:
        result.add(value + 2)

print(original)
print(result)
