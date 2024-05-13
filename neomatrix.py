import re

print("Matrix script:")
with open("encode.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip()) 

rows, cols = map(int, lines[0].split())

matrix = [list(line.strip()) for line in lines[1:]]
matrix = [row + [' '] * (cols - len(row)) for row in matrix]

transposed_matrix = list(zip(*matrix))
transposed_text = "".join("".join(row) for row in transposed_matrix)
decoded_text = re.sub(r'[^a-zA-Z]', ' ', transposed_text)

print("Decoded text:", decoded_text)


