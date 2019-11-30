from pip._vendor.distlib.compat import raw_input


def encryptChar(val1, val2):
    if val1.isalpha():
        return chr(ord("A") + ((ord(val1) - ord("A") + val2) % 26))
    return val1

def cipherize(str, ky):
    if ky < 0:
        ky = 26 - (-key % 26)
    result = ""
    ky = int(ky)
    for i in str:
        result += encryptChar(i, ky)
    return result


print("This is a Caeser Cipher")
message = "Hello, bro! wassup"                         #raw_input("Enter Encryption Message")
key = 3                                   #raw_input("Enter an Encryption Key (Int)")
cipher = cipherize(message, key)
print(f"The Cipher is: {cipher}")
new_plain = cipherize(cipher, -key)
print(f"I hope your original string was: {new_plain}")
