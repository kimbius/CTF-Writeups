import pwn

real_password = "RPC@_CYB3RC10B"
A = ['c', 'J', 'i', 'Z', 'x', 'a', 'K', 'N', 'Y', 'y', 'S', 'L', 'E', 'n', 'h', 'o', 'j', 'G', 'q', 'O', 'f', 'U', 'g', 'C', 'k', 'I', 'p', 'T', 'P', 'w', 'l', 's', 'V', 'm', 'b', 'M', 'u', 'D', 't', 'B', 'e', 'r', 'A', 'H', 'd', 'X', 'W', 'Q', 'R', 'F', 'z', 'v']
B = ['4', '*', '1', '@', '%', '#', '!', '5', '6', '-', '$', '9', '7', '_', '^', '0', '8', '&', '3', '2']

for x in real_password:
    if x in A:
        print("a" + str(-(len(A) - A.index(x))))
    elif x in B:
        print("b" + str(-(len(B) - B.index(x))))

# io = pwn.remote("rpca2.rpca.ac.th", 38012)
# io.interactive()