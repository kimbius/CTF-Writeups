import pwn

import cv2
import numpy as np
import base64
from qreader import QReader

qreader = QReader()
def read_qrcode_from_base64(base64_string):
    image_data = base64.b64decode(base64_string)
    nparr = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    decoded_text, = qreader.detect_and_decode(image=image)
    return decoded_text

client = pwn.remote("ctf.mf.grsu.by", 9011)
max_rounds = 0
i = 1
while True:
    if max_rounds > 0 and i > max_rounds:
        break
    print(f"Round {i}")
    client.recvuntil(b"/")
    get_max_rounds = int(client.recvline().decode()[:-1])
    if max_rounds == 0:
        max_rounds = get_max_rounds
        print(f"=== set-rounds to {get_max_rounds} ===")

    base64_encoded = client.recvline().decode()
    result = read_qrcode_from_base64(base64_encoded)
        
    print("sending:", result)
    client.sendline(result.encode())
    i += 1
client.interactive()