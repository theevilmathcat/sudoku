from flask import Flask, render_template, request

app = Flask(__name__)

def get_possible_candidates(puzzle, row_index, col_index):
    list_of_possibilities = set(range(1, 10))
    submatrix_row_start = (row_index // 3) * 3
    submatrix_col_start = (col_index // 3) * 3
    present_numbers = set(puzzle[row_index])
    present_numbers |= set(puzzle[r][col_index] for r in range(9))
    for i in range(submatrix_row_start, submatrix_row_start + 3):
        for j in range(submatrix_col_start, submatrix_col_start + 3):
            present_numbers.add(puzzle[i][j])
    present_numbers.discard(0)
    possible_candidates = list_of_possibilities - present_numbers
    return possible_candidates

def solve_sudoku(puzzle):
    for row_index in range(9):
        for col_index in range(9):
            if puzzle[row_index][col_index] == 0:
                possible_candidates = get_possible_candidates(puzzle, row_index, col_index)
                for candidate in possible_candidates:
                    puzzle[row_index][col_index] = candidate
                    if solve_sudoku(puzzle):
                        return True
                    puzzle[row_index][col_index] = 0
                return False
    return True

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    puzzle = None
    solved = False

    if request.method == 'POST':
        if request.form.get('reset_button'):
            # Handle reset logic
            return render_template('index.html', puzzle=None, solved=False, message=None)
        
        # Initialize the puzzle with zeros
        puzzle = [[0] * 9 for _ in range(9)]
        
        # Check if any cell is filled
        any_filled = False
        for i in range(9):
            for j in range(9):
                value = request.form.get(f'cell_{i}_{j}', '')
                if value.isdigit():
                    puzzle[i][j] = int(value)
                    if int(value) > 0:
                        any_filled = True
        
        if any_filled:
            if solve_sudoku(puzzle):
                solved = True
            else:
                solved = False
        else:
            message = "Please input your Sudoku puzzle."

    return render_template('index.html', puzzle=puzzle, solved=solved, message=message)

if __name__ == '__main__':
    app.run(debug=True)
