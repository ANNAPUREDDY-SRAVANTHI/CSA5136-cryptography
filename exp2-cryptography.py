text = input("Enter plaintext: ")
key = "QWERTYUIOPASDFGHJKLZXCVBNM"
result = ""
for ch in text:
    if ch.isupper():
        result += key[ord(ch) - ord('A')]
    elif ch.islower():
        result += key[ord(ch) - ord('a')].lower()
    else:
        result += ch

print("Encrypted text:", result)
