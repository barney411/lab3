import sys


# copy your definition of input_row() from exercise1.py here



# put your definition of input_matrix() here




# this code simply tests input_matrix(). If it works, it will output
# Input row 1 of the matrix: Input row 2 of the matrix: ...
# Input row 3 of the matrix: Input row 4 of the matrix: ...
# Enter a comma-separated list of numbers.
# Input row 4 of the matrix: 
# [[3.1 4.1 5.9 2.6]
#  [5.3 5.8 9.7 7.8]
#  [3.2 2.3 3.8 8.4]
#  [6.2 6.4 4.3 3.4]]

if __name__ == "__main__":
    # redirect standard input so it comes from input2.txt
    sys.stdin = open('lab3/inputs2.txt','r')
    m = np.array(input_matrix())
    print()
    print(m)
    sys.stdin.close()

