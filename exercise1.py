import sys

# put your definition of input_row() here



# this code simply tests input_row(). If it works, it will output
# Input row 1 of the matrix: (1.1, 2.3, 4.5)
# Input row 2 of the matrix: Enter a comma-separated list of numbers.
# Input row 2 of the matrix: Wrong number of columns! Try again.
# Input row 2 of the matrix: Wrong number of columns! Try again.
# Input row 2 of the matrix: Enter a comma-separated list of numbers.
# Input row 2 of the matrix: (1.9, 2.8, 3.7)

if __name__ == "__main__":
    # redirect standard input so it comes from input1.txt
    sys.stdin = open('lab3/inputs1.txt','r')
    print(input_row(0,"Input row 1 of the matrix: "))
    print(input_row(3,"Input row 2 of the matrix: "))
    sys.stdin.close()
