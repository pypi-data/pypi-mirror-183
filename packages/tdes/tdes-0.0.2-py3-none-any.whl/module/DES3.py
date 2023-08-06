from module.utils import * 
import click,os



def DES3_encrypt(mpath:str):
    if os.path.exists(mpath):
        key1,key2=generateKey()
        click.echo("Save your keys to use them in decryption... \nkey1= "+str(key1)+"\n key2= "+str(key2))
        with open(mpath, 'rb') as input_file:
            fileByte = input_file.read()
            output=desEncrypt(fileByte,key1)
            output= desDecncrypt(output,key2)
            output= desEncrypt(output,key1)
            with open(mpath, 'wb') as output_file:
                output_file.write(output)
                output_file.close()
        click.echo("File "+mpath.split("\\")[-1]+" encrypted successfully")


def DES3_encrypt2k(mpath:str,key1:bytes,key2:bytes):
    if checkKey(key1) and checkKey(key2):
        with open(mpath, 'rb') as input_file:
                fileByte = input_file.read()
                output=desEncrypt(fileByte,key1)
                output= desDecncrypt(output,key2)
                output= desEncrypt(output,key1)
                with open(mpath, 'wb') as output_file:
                    output_file.write(output)
                    output_file.close()
        click.echo("File "+mpath.split("\\")[-1]+" encrypted successfully")
    else: click.echo("Error! key must be at least 8 character")


def DES3_encrypt3k(mpath:str,key1:bytes,key2:bytes,key3:bytes):
    if checkKey(key1) and checkKey(key2) and checkKey(key3):
        with open(mpath, 'rb') as input_file:
                fileByte = input_file.read()
                output=desEncrypt(fileByte,key1)
                output= desDecncrypt(output,key2)
                output= desEncrypt(output,key3)
                with open(mpath, 'wb') as output_file:
                    output_file.write(output)
                    output_file.close()
        click.echo("File "+mpath.split("\\")[-1]+" encrypted successfully")
    else: click.echo("Error! key must be at least 8 character")


def DES3_decrypt2k(mpath:str,key1:bytes,key2:bytes):
    if checkKey(key1) and checkKey(key2):
        with open(mpath, 'rb') as input_file:
                fileByte = input_file.read()
                output=desDecncrypt(fileByte,key1)
                output= desEncrypt(output,key2)
                output= desDecncrypt(output,key1)
                with open(mpath, 'wb') as output_file:
                    output_file.write(output)
                    output_file.close()
        click.echo("File "+mpath.split("\\")[-1]+" decrypted successfully")
    else: click.echo("Error! key must be at least 8 character")


def DES3_decrypt3k(mpath:str,key1:bytes,key2:bytes,key3:bytes):
    if checkKey(key1) and checkKey(key2) and checkKey(key3):
        with open(mpath, 'rb') as input_file:
                fileByte = input_file.read()
                output=desDecncrypt(fileByte,key3)
                output= desEncrypt(output,key2)
                output= desDecncrypt(output,key1)
                with open(mpath, 'wb') as output_file:
                    output_file.write(output)
                    output_file.close()
        click.echo("File "+mpath.split("\\")[-1]+" decrypted successfully")
    else: click.echo("Error! key must be at least 8 character")


def DES3_encrypt_all(mpath:str):
    if os.path.exists(mpath):
        key1,key2=generateKey()
        click.echo("Save your keys to use them in decryption... \nkey1= "+str(key1)+"\n key2= "+str(key2))
        for dirpath, dirnames, filenames in os.walk(mpath):
            for file in filenames:
                DES3_encrypt2k(os.path.join(dirpath,file),key1=key1,key2=key2)
    else: click.echo("Error! Directory Not Found")       



def DES3_encrypt_all2k(mpath:str,key1:bytes,key2:bytes):
    if checkKey(key1) and checkKey(key2):
        if os.path.exists(mpath):
            for dirpath, dirnames, filenames in os.walk(mpath):
                for file in filenames:
                    DES3_encrypt2k(os.path.join(dirpath,file),key1=key1,key2=key2)
        else: click.echo("Error! Directory Not Found")   
    else: click.echo("Error! key must be at least 8 character")
 


def DES3_encrypt_all3k(mpath:str,key1:bytes,key2:bytes,key3:bytes):
    if checkKey(key1) and checkKey(key2) and checkKey(key3):
        if os.path.exists(mpath):
            for dirpath, dirnames, filenames in os.walk(mpath):
                for file in filenames:
                    DES3_encrypt3k(os.path.join(dirpath,file),key1=key1,key2=key2,key3=key3)
        else: click.echo("Error! Directory Not Found")   
    else: click.echo("Error! key must be at least 8 character")




def DES3_decrypt_all2k(mpath:str,key1:bytes,key2:bytes):
    if checkKey(key1) and checkKey(key2):
        if os.path.exists(mpath):
            for dirpath, dirnames, filenames in os.walk(mpath):
                for file in filenames:
                    DES3_decrypt2k(os.path.join(dirpath,file),key1=key1,key2=key2)
        else: click.echo("Error! Directory Not Found")
    else: click.echo("Error! key must be at least 8 character")



def DES3_decrypt_all3K(mpath:str,key1:bytes,key2:bytes,key3:bytes):
    if checkKey(key1) and checkKey(key2) and checkKey(key3):
        if os.path.exists(mpath):
            for dirpath, dirnames, filenames in os.walk(mpath):
                for file in filenames:
                    DES3_decrypt3k(os.path.join(dirpath,file),key1=key1,key2=key2,key3=key3)
        else: click.echo("Error! Directory Not Found")
    else: click.echo("Error! key must be at least 8 character")
