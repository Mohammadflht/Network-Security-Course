from des import DesKey

def find_key_chars(ciphertext, plaintext, key):
    for G in range(256):
        for H in range(256):
            for I in range(256):
                for T in range(256):
                    test_key = key.format(G=G, H=H, I=I, T=T)
                    des_key = DesKey(test_key.encode())
                    decrypted = des_key.decrypt(ciphertext, padding=True).decode()
                    if decrypted == plaintext:
                        return test_key
    return None

Ciphertext = bytes.fromhex('xce0\xAek\x1bi\xe6\xalIi\x0e~M=>\xa4\xac\xb77x81HNx87x9b')
Plaintext = "des is not secure"
key = "x73\x6alx681x66x64\x67x{G}x{H}x{I}x{T}"

found_key = find_key_chars(Ciphertext, Plaintext, key)

if found_key:
    print("Found key:", found_key)
else:
    print("No key found.")