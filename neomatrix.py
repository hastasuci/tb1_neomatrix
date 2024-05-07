import re
import os 
os.system("cls")

print("Enter the matrix script:")

def read_matrix():
    return [tuple(row) for row in iter(input, "")]

transposed_matrix = list(zip(*read_matrix()))
output = ""
for row in transposed_matrix:
    output += " ".join(re.findall(r'[a-zA-Z]+', "".join(row))) + ""

print("Decode:", output.strip())