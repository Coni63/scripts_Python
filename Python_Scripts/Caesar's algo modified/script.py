string = "Test004 passed with success ^_^"
key = 11

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encrypt(mot, k):
    encrypted_string = ""

    for char in mot:
        if char in alphabet:
            if char.isupper():
                prev_key = ord(char) - ord("A") + 1
                next_index = ord(char) + k
                if next_index > ord("Z"):
                    next_index = (next_index % (ord("Z") + 1)) + ord("A")
                encrypted_string += chr(next_index)
            else:
                prev_key = ord(char) - ord("a") + 1
                next_index = ord(char) + k
                if next_index > ord("z"):
                    next_index = (next_index % (ord("z") + 1)) + ord("a")
                encrypted_string += chr(next_index)

            k = prev_key
        else:
            encrypted_string+= char

    return encrypted_string


def decrypt(code, k):
    decrypted_string = ""
    for char in code:
        if char in alphabet:
            if char.isupper():
                original_index = ord(char) - k
                if original_index < ord("A"):
                    original_index = ord("Z")  - ord("A") + original_index + 1
                decrypted_string += chr(original_index)
                k = original_index - ord("A") + 1
            else:
                original_index = ord(char) - k
                if original_index < ord("a"):
                    original_index = ord("z") - ord("a") + original_index + 1
                decrypted_string += chr(original_index)
                k = original_index - ord("a") + 1
        else:
            decrypted_string += char

    return decrypted_string

key = key % 26

string_converted = encrypt(string, key)
print(string_converted)

string_init = decrypt(string_converted, key)
print(string_init)

