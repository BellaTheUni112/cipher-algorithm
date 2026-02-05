import math

MASK = 0xFFFFFFFF

s = int(input("enter number: ")) & MASK

s ^= (s << 13) & MASK
s ^= (s >> 7)
s ^= (s << 17) & MASK

print(s & MASK)
