import click
from module import DES3 as des3



@click.group() 
def cli():
    '''
    tdes is a tool for encryption and decryption files that use triple Data Encryption Standard aka 3DES
    '''
    pass



@cli.command()
@click.option('--path',  help='path of the file you want to encrypt',required=True)
@click.option('--key1',  help='The First key to use in 3DES encryption make sure to save it for decryption and enter it in the same order',required=False)
@click.option('--key2',  help='The second key to use in 3DES encryption make sure to save it for decryption and enter it in the same order',required=False)
@click.option('--key3',  help='The third key to use in 3DES encryption make sure to save it for decryption and enter it in the same order.',required=False)
def encrypt(path,key1=None,key2=None,key3=None):
    '''
    encrypt one file by given its path [required] and keys for encryption [optional]
    '''
    if key1 and key2 and key3:
        des3.DES3_encrypt3k(path,key1.encode(),key2.encode(), key3.encode())
    elif key1 and key2:
        des3.DES3_encrypt2k(path,key1.encode(),key2.encode())
    else:
        des3.DES3_encrypt(path)


@cli.command()
@click.option('--path',  help='path of the file you want to decrypt',required=True)
@click.option('--key1',  help='The First key to use in 3DES decryption make sure to enter it in the same order of encryption',required=True)
@click.option('--key2',  help='The second key to use in 3DES decryption make sure to enter it in the same order of encryption.',required=True)
@click.option('--key3',  help='The third key to use in 3DES decryption make sure to enter it in the same order of encryption.',required=False)
def decrypt(path,key1,key2,key3=None):
    '''
    decrypt one file by given its path [required] and keys for encryption [optional]
    '''
    if key3:
        des3.DES3_decrypt3k(path,key1=key1.encode(),key2=key2.encode(),key3=key3.encode())
    else:
        des3.DES3_decrypt2k(path,key1=key1.encode(),key2=key2.encode())
  

@cli.command()
@click.option('--path',  help='path of the directory you want to encrypt it\'s files',required=True) 
@click.option('--key1',  help='The First key to use in 3DES encryption make sure to save it for decryption and enter it in the same order',required=False)
@click.option('--key2',  help='The second key to use in 3DES encryption make sure to save it for decryption and enter it in the same order',required=False)
@click.option('--key3',  help='The third key to use in 3DES encryption make sure to save it for decryption and enter it in the same order.',required=False)
def encryptall(path,key1=None,key2=None,key3=None):
    '''
    encrypt all files in a directory by given its path [required] and keys for encryption [optional]
    '''
    if key1 and key2 and key3:
        des3.DES3_encrypt_all3k(path,key1.encode(),key2.encode(), key3.encode())
    elif key1 and key2:
        des3.DES3_encrypt_all2k(path,key1.encode(),key2.encode())
    else:
        des3.DES3_encrypt_all(path)


@cli.command()
@click.option('--path',  help='path of the directory you want to encrypt it\'s files',required=True) 
@click.option('--key1',  help='The First key to use in 3DES encryption make sure to save it for decryption and enter it in the same order',required=True)
@click.option('--key2',  help='The second key to use in 3DES encryption make sure to save it for decryption and enter it in the same order',required=True)
@click.option('--key3',  help='The third key to use in 3DES encryption make sure to save it for decryption and enter it in the same order.',required=False)
def decryptall(path,key1,key2,key3=None):
    '''
    decrypt all files in a directory by given its path [required] and keys for encryption [optional]
    '''
    if key3:
        des3.DES3_decrypt_all3K(path,key1.encode(),key2.encode(), key3.encode())
    else :
        des3.DES3_decrypt_all2k(path,key1.encode(),key2.encode())


if __name__=='__main__':
    cli()

