import re

print("Matrix script:")
with open("encode.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  

rows, cols = map(int, lines[0].split())
matrix = [list(line.strip()) for line in lines[1:]]
transposed_matrix = ["".join(row) for row in zip(*matrix[:cols])]
transposed_text = "".join(transposed_matrix)
decoded_text = re.sub(r'[^a-zA-Z]', ' ', transposed_text)

print("Decoded text:", decoded_text)
