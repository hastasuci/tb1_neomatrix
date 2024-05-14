import re

def decode_matrix(file_name):
    print("Matrix script:")
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

    rows, cols = map(int, lines[0].split())
    matrix = [list(line.strip()) for line in lines[1:]]
    matrix = [row + [' '] * (cols - len(row)) for row in matrix]

    transposed_matrix = list(zip(*matrix))
    transposed_text = "".join("".join(row) for row in transposed_matrix)
    
    decoded_text = re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', transposed_text)
    print("Decoded text:", decoded_text)

decode_matrix("encode.txt")
