import string
alphabets = list(string.ascii_letters)
alphabets.append(" ")

def encrypt(msg,key):
    text = ""
    for i in msg:
        ind = (alphabets.index(i))
        ind = (ind + key)%53
        text += alphabets[ind]
    return text   

def decrypt(msg,key):
    text = ""
    for i in msg:
        ind = (alphabets.index(i))
        ind = (ind - key + 53)%53
        text += alphabets[ind]
    return text  
flag = 1
while flag!=0:
    a = int(input("Choose 1 to Encrypt, 2 to Decrypt, other number to exit: "))
    if a!=1 and a!=2:
        break
    msg = input("Type your message: ")
    key = int(input("Type your key number: "))
    if a == 1:
        print(f"Encrypted text is {encrypt(msg,key)}")
    elif a == 2:
        print(f"Decrypted text is {decrypt(msg,key)}")

