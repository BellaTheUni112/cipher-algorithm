MASK = 0xFFFFFFFF

def xorshift32(s):
    s &= MASK
    s ^= (s << 13) & MASK
    s ^= (s >> 7)
    s ^= (s << 17) & MASK
    return s & MASK

nums = list(map(int, input("enter numbers (space separated): ").split()))

state = 0x12345678

for n in nums:
    state ^= n & MASK
    state = xorshift32(state)

digits = ""
while len(digits) < 40:
    state = xorshift32(state)
    digits += f"{state:010d}"

result = digits[:40]
print(result)
