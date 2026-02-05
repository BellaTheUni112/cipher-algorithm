import math

MASK = 0xFFFFFFFF

s = int(input("enter number: ")) & MASK

s ^= (s << 17) & MASK
s ^= (s << 34) & MASK

s ^= (s >> 7)
s ^= (s >> 14)
s ^= (s >> 28)

s ^= (s << 13) & MASK
s ^= (s << 26) & MASK

print(s & MASK)
