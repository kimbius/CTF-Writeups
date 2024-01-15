import pwn
import json

file_headers = {}
already_count = {}

for i in range(50):
    client = pwn.remote("ctf.mf.grsu.by", 9010)
    client.recvuntil(b"/50\n\n")
    file_header = client.recvline().decode()[:-1]
    client.sendline(b"biu2")
    client.recvline()
    correct_mime_type = client.recv().decode().split(": ")[1][:-1]
    if correct_mime_type not in file_headers:
        file_headers[correct_mime_type] = []
        already_count[correct_mime_type] = 0
    else:
        already_count[correct_mime_type] += 1
    file_headers[correct_mime_type].append(file_header)
    client.close()
    
print(f"{already_count=}")
file_path = "output.json"

with open(file_path, 'w') as json_file:
    json.dump(file_headers, json_file, indent=4)

print(f"JSON data has been written to {file_path}")