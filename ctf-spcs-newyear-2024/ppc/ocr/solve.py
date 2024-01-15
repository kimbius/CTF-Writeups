import pwn

import base64
from io import BytesIO
from PIL import Image
import pytesseract
import json
import hashlib

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
    
    
readed_cache = {}
json_file_path = 'cache.json'

def load_cache():
    with open(json_file_path, 'r') as file:
        return json.load(file)
    
readed_cache = load_cache()

def md5sum(string):
    return hashlib.md5(string.encode()).hexdigest()

def read_qrcode_from_base64(base64_string):
    if md5sum(base64_string) in readed_cache:
        return readed_cache[md5sum(base64_string)], True
    try:
        decoded_data = base64.b64decode(base64_string)
        image = Image.open(BytesIO(decoded_data))
        text = pytesseract.image_to_string(image, config='--psm 6')

        return text.strip(), False
    except Exception as e:
        print(f"Error: {e}")
        return None, None
    
while True:
    readed_cache = load_cache()
    client = pwn.remote("ctf.mf.grsu.by", 9007)
    client.recvlines(4)
    try:
        for i in range(250):
            print("Round", i+1)
            client.recvuntil(b"b'")
            base64_encoded = client.recvline().decode()[:-2]
            result, cache = read_qrcode_from_base64(base64_encoded)
            result = result.replace("  ", " ").replace(" ", "_").replace("__", "_")
            if cache:
                print("=== cache ===")
            print("sending:", result)
            client.sendline(result.encode())
            
            serv_response = client.recvlines(2)[-1].decode()
            print(serv_response)
            token = md5sum(base64_encoded)
            readed_cache[token] = serv_response.split(": ")[1]
            if readed_cache[token].startswith("grodno{"):
                client.interactive()
                
    except Exception as e:
        if not client.closed:
            client.close()
        print(e)
            
    with open(json_file_path, 'w') as json_file:
        json.dump(readed_cache, json_file, indent=4)