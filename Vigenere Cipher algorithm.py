def generate_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
def cipher_text(string, key):
    cipher_text = []
    for i in range(len(string)):
        if string[i].isalpha():
            shift = ord(key[i].lower()) - ord('a')
            if string[i].isupper():
                x = (ord(string[i]) + shift - ord('A')) % 26 + ord('A')
            else:
                x = (ord(string[i]) + shift - ord('a')) % 26 + ord('a')
            cipher_text.append(chr(x))
        else:
            cipher_text.append(string[i])
    return("" . join(cipher_text))
     
def original_text(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = ord(key[i].lower()) - ord('a')
            if cipher_text[i].isupper():
                x = (ord(cipher_text[i]) - shift - ord('A')) % 26 + ord('A')
            else:
                x = (ord(cipher_text[i]) - shift - ord('a')) % 26 + ord('a')
            orig_text.append(chr(x))
        else:
            orig_text.append(cipher_text[i])
    return("" . join(orig_text))
     
myText = "Everyone suggests other than the person lack motivation, or directly suggests the person remain motivated. But, no one ever tells what is the motivation of how one can stay motivated. Motivation means to face the obstacle and find an inspiration that helps you to go through tough times. In addition, it helps you to move further in life."
myKey = "motivation"
 
key = generate_key(myText, myKey)
cipher_text = cipher_text(myText, key)
print("Ciphertext: ", cipher_text)
print("Original/Decrypted Text: ", original_text(cipher_text, key))