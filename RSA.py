# Number Theory RSA Project
# Group 3
# Jack Trahan
# Marcin Karcz


# Basic RSA Encryption Implementation
# Top-Level Function is RSA()

# Note this RSA implementation does not validate keys


import os, sys, re

def RSA():
    # Top Level-RSA fuction

    # Prompt whether user wishes to encrypt or decrypt
    prompt = input("Are you encrypting, or decrypting text? (enter 'e' or 'd')? ").strip().lower()
    if prompt == "e":
        encrypt()
    elif prompt == "d":
        decrypt()
    else:
        print("Please enter either 'e' for encryption, or 'd' for decryption.")




def encrypt():
    # Encode a plain-text message

    #Load Keys m, k
    key_path = input("\n\nEnter path to file containing Public Key (m) and Auxiliary Key (k). Press 'enter' for default 'publickey.txt':   ")
    if key_path == '': key_path = 'publickey.txt'
    m, k = load_keys(key_path)
    print("Keys Loaded Successfully:")
    print("Public Key: ", m)
    print("Auxiliary Key: ", k)

    # Load Plain-Text File
    text_path = input("Enter PATH to the file you wish to encrypt or press 'enter' for 'plaintext.txt':  ")
    if text_path == '': text_path = 'plaintext.txt'
    plain_text = load_text(text_path)

    print("\n------------- Plain Text Message Below -----------")
    print(plain_text)
    print("--------------------------------------------------")


    # Convert Text-to-ASCII
    ascii_text = to_asc(plain_text)
    print("ASCII text = ", ascii_text)

    # Split text into m-1 sized chunks
    n = len(str(m))-1
    chunked_text = chunk(ascii_text, n)
    print("PRE-ENCODING = ", chunked_text)

    # Create the Cipher
    print("Encoding Message...")
    cipher_list = []
    for i in chunked_text:
        i = int(i)
        encoded = pow(i,k,m)
        cipher_list.append(encoded)
    print("\n------------- Encoded Message Below --------------")
    print(cipher_list)
    print("--------------------------------------------------")

    # Save the Cipher
    cipher_path = input("\nWhere would you like to save your ciphered message? Press enter for 'cipher.txt':   ")
    if cipher_path == '': cipher_path = 'cipher.txt'
    print("Saving Cipher to ", cipher_path, "........")
    try:
        with open(cipher_path, 'w') as f:
            for i in cipher_list:
                f.write(str(i))
                f.write("\n")
    except Exception as e:
        print("Unable to save Cipher.")
        print(e.with_traceback)
        sys.exit(1)

    print("Your message has been encoded. Goodbye!")


def decrypt():
    # De-Cipher an encoded message.

    # Load Keys m, k
    key_path = input("Enter path to file containing Public Key (m), Private Key (phi(m)), and Auxiliary Key (k). Press 'enter' for default 'privatekey.txt':   ")
    if key_path == '': key_path = 'privatekey.txt'
    m, phi, k = load_keys(key_path)
    print("Keys Loaded Successfully:")
    print("Public Key: ", m)
    print("Private Key: ", phi)
    print("Auxiliary Key: ", k)

    # Load Cipher File
    cipher_path = input("\nEnter PATH to file you wish to decrypt. Press 'enter' for cipher.txt:   ")
    if cipher_path == '': cipher_path = 'cipher.txt'
    cipher = load_cipher(cipher_path)
    print("Cipher Loading was Successful!")
    print("\n------------- Message to Decrypt -----------------")
    print(cipher)
    print("----------------------------------------------------")
    ######################
    ####### Start the deciphering Portion #######


    # De-Cipher message by chuck-size
    print("\nDeciphering Message...")
    chunksize = len(str(m))-1
    decoded = []
    for x in cipher:
        x = Kthrootmodm(k,int(x),m,phi)
        x = str(x)
        while len(x) < chunksize:
            x = '0'+x
        decoded.append(x)
    decoded = ''.join(decoded)


    # Now split into ASCII length strings and convert to PLain-Text
    asc_group = [int(decoded[i:i+3]) for i in range(0, len(decoded), 3)]

    plain_message = ''.join([chr(i) for i in asc_group])

    print("\n------------- Message -----------------")
    print(plain_message)
    print("----------------------------------------------------")

    # Save Message
    path = input("\nEnter PATH to a file where you wish to store the decrypted message ('enter' for plaintext.txt):   ")
    if path == '': path = 'plaintext.txt'
    try:
        with open(path, 'wt', encoding='utf-8') as f:
            f.write(plain_message)
    except IOError:
        print("Unable to store decryptd message. Exiting Program...")
        sys.exit(1)
    print("\nMessage Saved!\nGoodbye.")











##################### Math Functions ######################################

def Dioph(a,b, Trace=False, level=0):
    '''
    Recurrsive function that returns an initial integer solution (x,y) to
    the diophantine equation ax + by = c where c is the greatest common denominator of a and b.

    Parameters
    -----------
    a: integer
        value of a in ax+by=c
    b: integer
        value of b in ax+by=c
    Trace: boolen
        toggle printing of recussive steps
    level: dummy varible
        used to track recussion depth for Trace print formatting
    '''
    level += 1  # Used to track recussion depth to format print statements from Trace
    if a == 0:
        return(0,1)
    else:
        if Trace and b%a != 0: print("-"*level+">",a, b%a) # Print Extended Euclidean forward steps indended with '---->' corresponding to recussion depth
        x, y = Dioph(b%a, a, Trace, level)
        if Trace and level > 1: print("-"*level+"<", x, y - (b // a) * x) # Print Extended Euclidean backword steps indended with '----<' corresponding to recussion depth
        return (y - (b // a) * x, x)

# Solve x^k=b (mod m); phi=phi(m), avoiding the hard problem of factoring m
def Kthrootmodm(k,b,m,phi):
	u,v=Dioph(k,phi)			# find u,v: ku+phiv=1
	while u<0: u+=phi			# need positive u
	return pow(b,u,m)			# return solution b^u

##############################################################################
def load_keys(path):
    # Load keys from file
    print("------------------------------------")
    print("Loading Keys.....")
    key_list = []
    try:
        with open(path, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    pass
                else:
                    line = re.sub('[^0-9]','', line)
                    if line:
                        key_list.append(int(line))
    except FileNotFoundError:
        print("File Not Found! Verify PATH to file is correct. Exiting program...")
        sys.exit(1)

    return key_list

def load_text(path):
    # Load text from a file
    print("------------------------------------")
    print("Loading Text File.....")
    try:
        with open(path, 'r') as f:
            plain_text = f.readlines()
    except FileNotFoundError:
        print("File not found. Exiting Program...")
        sys.exit(1)

    print("File Loaded Successfully!")
    plain_text = ''.join(plain_text)
    return plain_text

def to_asc(text):
    # convert from Plain Text to ASCII text
    asc_text = []
    for c in text:
        asc = str(ord(c))
        if len(asc) == 1:
            asc = "00" + asc
        elif len(asc) == 2:
            asc = "0"+asc
        asc_text.append(asc)

    return ''.join(asc_text)

def chunk(text, n):
    # Divide text into n-sized chunks, return list of n-size chunks.
    chunked_list = [text[i:i + n] for i in range(0, len(text), n)]

    # Right-Pad last chuck until full size (m-1)
    while len(chunked_list[-1]) < n:
        chunked_list[-1] += '0'

    return chunked_list

def load_cipher(path):
    # Retrieve Cipher from file
    print("------------------------------------")
    print("Loading cipher from ", path, ".......")

    try:
        with open(path, 'r') as f:
            num = f.readlines()
            num = [x.strip() for x in num]
    except FileNotFoundError:
        print("Failed to load Cipher file. Verify PATH to file is correct. Exiting Program....")
        sys.exit(1)
    return num



