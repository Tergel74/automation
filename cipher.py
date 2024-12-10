from sys import argv


def encrypt(msg, key):
    encrypted_msg = ""
    for letter in msg:
        encrypted_msg += chr(ord(letter) + key)

    return encrypted_msg


def decrypt(msg, key):
    decrypted_msg = ""
    for letter in msg:
        decrypted_msg += chr(ord(letter) - key)

    return decrypted_msg


try:
    command = argv[1]
    text = argv[2]
    key = argv[3]

    if command in ['-e', '-E']:
        out = encrypt(text, int(key))
    elif command in ['-d', '-D']:
        out = decrypt(text, int(key))
    print(out)
except:
    if command in ['-h', '-H']:
        err = """
    Available Commands:
        -e or -E for encrypting
        -d or -D for decrypting
    """
    else:
        err = 'Error'
    print(err)
