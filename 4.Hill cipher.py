text = input("Enter plaintext: ").upper()
if len(text) % 2 != 0:
    text += "X"
key = [[3, 3], [2, 5]]
result = ""
for i in range(0, len(text), 2):
    a = ord(text[i]) - ord('A')
    b = ord(text[i + 1]) - ord('A')
    c1 = (key[0][0] * a + key[0][1] * b) % 26
    c2 = (key[1][0] * a + key[1][1] * b) % 26
    result += chr(c1 + ord('A'))
    result += chr(c2 + ord('A'))
print("Encrypted text:", result)
