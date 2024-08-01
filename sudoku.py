'''
puzzle
3 . 2 . 9 . . 5 .
. 5 . 7 . 4 . . .
9 . . . 6 3 4 . .
4 7 . . . 8 . . .
8 2 . 6 1 7 . 3 4
. . . 3 . . . 2 7
. . 5 4 3 . . . 9
. . . 1 . 2 . 6 .
. 3 . . 7 . 2 . 8
'''
initial_puzzle  = [
    [3, 0, 2, 0, 9, 0, 0, 5, 0],
    [0, 5, 0, 7, 0, 4, 0, 0, 0],
    [9, 0, 0, 0, 6, 3, 4, 0, 0],
    [4, 7, 0, 0, 0, 8, 0, 0, 0],
    [8, 2, 0, 6, 1, 7, 0, 3, 4],
    [0, 0, 0, 3, 0, 0, 0, 2, 7],
    [0, 0, 5, 4, 3, 0, 0, 0, 9],
    [0, 0, 0, 1, 0, 2, 0, 6, 0],
    [0, 3, 0, 0, 7, 0, 2, 0, 8]
]

# initially it has the same numbers
final_puzzle = list(initial_puzzle)

# Where You Can Put Numbers

# initially it has the all the positibilities
list_of_possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create the boolean matrix
boolean_matrix = []

# Iterate over each row in the original matrix
for i in initial_puzzle:
    # Create an empty list for the current row in the boolean matrix
    boolean_row = []
    
    # Iterate over each cell in the current row
    for j in i:
        # Append True if the cell is 0, otherwise append False
        boolean_row.append(j == 0)
    
    # Add the boolean row to the boolean matrix
    boolean_matrix.append(boolean_row)

# Print the boolean matrix
# for row in boolean_matrix:
#    print(row)

# print rows
initial_row = 0
last_row = 2
# Print rows from initial_row to last_row (inclusive)
for index in range(initial_row, last_row + 1):
    print(initial_puzzle[index])
print()

# print cols
initial_col = 0
last_col = 2
# Iterate over all rows.
# in python when we are doing 2d list iteration, row here is like matrix[i] in jave so
# matrix[i][initial_col:last_col + 1]
for row in initial_puzzle:
    # Slice the row to include only the desired columns
    sliced_row = row[initial_col:last_col + 1]
    # Print the sliced row
    print(sliced_row)
print()

def square(initial_puzzle, start_row, end_row, start_col, end_col):
    #set the initial submatrix
    submatrix = []
    for i in initial_puzzle [start_row:end_row]:
        submatrix_row = i[start_col:end_col]
        submatrix.append(submatrix_row)
    # print to check if you are extracting this right
        #for i in submatrix:
        #   print(i)
    
    # check the row of the submatrix against the same row of the initial_puzzle
    # to see if we can put any number in, if yes add it to a list of possibilites
    def row(initial_puzzle, start_row, end_row, submatrix):
        available_row_numbers = []
        proposed_row = []
        return row
    
    # check the col of the submatrix against the same col of the initial_puzzle
    # to see if we can put any number in, if yes add it to a list of possibilites
    def col(initial_puzzle,start_col, end_col, submatrix):
        available_col_numbers = []
        proposed_col = []
        return col
    
    return submatrix