
key = "MONARCHY"
text = input("Enter plaintext: ").upper().replace("J", "I")

letters = ""
for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch.isalpha() and ch not in letters:
        letters += ch

matrix = [list(letters[i:i+5]) for i in range(0, 25, 5)]

text = "".join(ch for ch in text if ch.isalpha())
pairs = []
i = 0

while i < len(text):
    a = text[i]
    if i + 1 == len(text):
        b = "X" if a != "X" else "Q"
        i += 1
    elif text[i] == text[i+1]:
        b = "X" if a != "X" else "Q"
        i += 1
    else:
        b = text[i+1]
        i += 2
    pairs.append((a, b))

result = ""

for a, b in pairs:
    r1, c1 = next((r, c) for r in range(5)
                  for c in range(5) if matrix[r][c] == a)
    r2, c2 = next((r, c) for r in range(5)
                  for c in range(5) if matrix[r][c] == b)

    if r1 == r2:
        result += matrix[r1][(c1+1) % 5]
        result += matrix[r2][(c2+1) % 5]
    elif c1 == c2:
        result += matrix[(r1+1) % 5][c1]
        result += matrix[(r2+1) % 5][c2]
    else:
        result += matrix[r1][c2]
        result += matrix[r2][c1]

print("Encrypted text:", result)
