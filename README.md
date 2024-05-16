This program can read matrix script from external file, for example 'encode.txt'.
Then the matrix script will changed into decoded script, so we need to read each column from top to bottom from the leftmost column and select only the alphanumeric characters and connect them. If there are symbols or spaces between two alphanumeric characters of the matrix script, it will replaced as a single space ' ' for better readability.

OUTPUT\
The matrix script: \
7 3 \
Tsi \
h%x \
i # \
sM  \
$a  \
#t% \
ir! 

Decoded text: This is Matrix#  %!

-------------------------------------------------------------------------------------------------------------------------------\
If you want to try with another matrix script, here is the matrix format and constraint that can decoded by this program.

MATRIX FORMAT\
The first line contains space-separated integers N(rows) and M(columns) respectively.
The next  lines contain the row elements of the matrix script.

CONSTRAINT\
0 < N, M < 100
