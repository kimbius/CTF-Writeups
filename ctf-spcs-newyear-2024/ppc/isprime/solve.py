import pwn

def isNotPrime(Number):
    return 2 not in [Number,2**Number%Number]

client = pwn.remote("ctf.mf.grsu.by", 9000)
for i in range(50):
    client.recvuntil(b"/50").decode()
    number = int(client.recv().decode())
    isprime = "NO" if isNotPrime(number) else "YES"
    client.sendline(isprime.encode())
client.interactive()