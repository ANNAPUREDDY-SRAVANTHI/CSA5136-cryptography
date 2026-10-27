text = input("Enter plaintext: ").replace(" ", "").upper()
key = input("Enter column key (e.g. 3142): ")
cols = len(key)
rows = (len(text) + cols - 1) // cols
text += "X" * (rows * cols - len(text))
matrix = [text[i:i + cols] for i in range(0, len(text), cols)]
result = ""
for digit in sorted(key):
    col = key.index(digit)
    for row in matrix:
        result += row[col]

print("Encrypted text:", result)
