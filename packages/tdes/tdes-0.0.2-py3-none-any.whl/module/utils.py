import random,string
from Cryptodome.Cipher import DES


def desEncrypt(file:bytes, key: bytes):
    cipher = DES.new(key=key, mode=DES.MODE_CFB,iv=key)
    return cipher.encrypt(file)


def desDecncrypt(file: str, key: bytes):
     cipher = DES.new(key=key, mode=DES.MODE_CFB,iv=key)
     return cipher.decrypt(file)



def generateKey():
    key1="".join(random.choices(string.ascii_letters+string.digits,k=8))
    key2="".join(random.choices(string.ascii_letters+string.digits,k=8))
    return key1.encode(),key2.encode()



def checkKey(key:bytes):
    return len(key)>=8
