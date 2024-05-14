flag_encrypted = b'&":\x1e+`4\x1f\x10\x16AfZ\x03\x11\\FGKjYQ@\x06@CLo\r\x05KQC\x10\x1blY\x02BU\t'

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

print(
    xor(flag_encrypted, xor(flag_encrypted, b"RPCACTF{") * 6).decode()
)