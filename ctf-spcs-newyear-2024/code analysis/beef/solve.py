b = bytearray(b"a30feqcb:x")

for i in range(10):
   b[i] = (b[i] ^ i) + 1

print(f"Good BEEF! grodno{{{b.decode()}}}") # grodno{b33fbuff3r}