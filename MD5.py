import itertools
import hashlib

hashes = [
    "8AA3B7CAB2EBF4D21C25F5E38F8C30DC",
    "7F077FD9780DBF3666A11781EA262E60",
    "C89D5B32C6D3F3B62FD5F8F362A921B7",
    "7AB1EE87F6F1873A24E864D8FAD3B1D2"
]

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

for length in range(1, 6):
    for pwd_tuple in itertools.product(chars, repeat=length):
        pwd = ''.join(pwd_tuple)
        pwd_hash = hashlib.md5(pwd.encode()).hexdigest().upper()
        if pwd_hash in hashes:
            print(f'Found password: {pwd} for hash: {pwd_hash}')
