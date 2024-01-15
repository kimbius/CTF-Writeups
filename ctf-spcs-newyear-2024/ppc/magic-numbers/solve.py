import pwn
import json

json_file_path = 'final.json'
with open(json_file_path, 'r') as file:
    data = json.load(file)
    for key in data:
        if type(data[key]) == str:
            data[key] = [data[key]]
    
client = pwn.remote("ctf.mf.grsu.by", 9010)
for i in range(50):
    print(f"Round {i+1}")
    client.recvuntil(b"/50\n\n")
    file_header = client.recvline().decode()[:-1]
    key_collected = ""
    for key in data:
        if any([file_header.startswith(_) for _ in data[key]]):
            key_collected = key
            break
    client.sendline(key_collected.encode())
    client.recvlines(2)
    
client.interactive()