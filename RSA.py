# RSA Project

import os

def RSA():
    # Top Level-RSA fuction
    
    # Promt whether user wishes to encrypt or decrypt
    while True:
        prompt = input("Are you encrypting, or decrypting text? (enter 'e' or 'd')?").strip().lower()
        if prompt == "e" or prompt == "d":
            break
        else:
            print("Please enter either 'e' for encryption, or 'd' for decryption.")
    
    read_public_key()
    
    
    

def read_Public_Key():
    # Read pubic keys
    path_to_public_keys = ''
    while not os.path.isfile(path_to_public_keys):
        
        
    


####################################
def encrypt(text):
    ascii_digits = to_asc(text)

def to_asc(text):
    # convert from Plain Text to ASCII text
    asc_text = []
    for c in text:
        asc = str(ord(c))
        if len(asc) == 1:
            asc = "00"+asc
        elif len(asc) == 2:
            asc = "0"+asc        
            asc_text.append(asc)
    return asc_text
        
