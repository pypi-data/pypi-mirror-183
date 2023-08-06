import random
import base64

def create_key():
    key = "1234567890-=qwertyuiop[]asdfghjkl;'\zxcvbnm,./!@#$%^&*()_+"
    after = "1234567890-=qwertyuiop[]asdfghjkl;'\zxcvbnm,./!@#$%^&*()_+"
    jump = random.randint(2, 10)
    after = "".join(key[key.index(letter) + jump if key.index(letter) + 1>len(key) else key.index(letter) - jump] if letter in key else letter for letter in after)
    #returns key and jump
    return f"{after}L{jump}"

def get_key_from_key_string(key):
    spli = key.split("L")
    try:
        return spli[0]
    except Exception:
        return "Please put the key you got from the create_key() function."

def get_jump_from_key_string(key):
    spli = key.split("L")
    try:
        return spli[1]
    except Exception:
        return "Please put the key you got from the create_key() function."

def secure(message, key, jump):
    key = key
    message = "".join(key[key.index(letter) + jump if key.index(letter) + 1 > len(key) else key.index(letter) - jump] if letter in key else letter for letter in message)
    return base64.b32encode(bytearray(str(message), 'ascii')).decode('utf-8')

def decode(message, key, jump):
    message = base64.b32decode(bytearray(str(message), 'ascii')).decode('utf-8')
    try:
        message = "".join(key[key.index(letter) - jump if key.index(letter) + 1 > len(key) else key.index(letter) + jump] if letter in key else letter for letter in message)
        return message
    except Exception:
        return "Failed to decode. try to create a new key."