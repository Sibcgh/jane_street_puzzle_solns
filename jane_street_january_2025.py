import math

# Original Sudoku puzzle
sudoku = [
    [".", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "5"],
    [".", "2", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "0", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "2", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "0", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "5", ".", "."]
]

# Convert Sudoku grid to a list of lists for easier manipulation
grid = [list(row) for row in sudoku]


def is_valid(grid, row, col, num):
    # Check if the number is not present in the current row
    if num in grid[row]:
        return False
    # Check if the number is not present in the current column
    if num in [grid[r][col] for r in range(9)]:
        return False
    # Check if the number is not present in the current 3x3 box
    box_row = 3 * (row // 3)
    box_col = 3 * (col // 3)
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == num:
                return False
    return True


def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == ".":
                for num in "012345678":
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = "."
                return False
    return True


def calculate_gcd(grid):
    row_numbers = []
    for row in grid:
        row_num = int("".join(row))
        row_numbers.append(row_num)
    current_gcd = row_numbers[0]
    for num in row_numbers[1:]:
        current_gcd = math.gcd(current_gcd, num)
    return current_gcd


# Solve the Sudoku puzzle
solve_sudoku(grid)

for r in grid:
    print(*r, sep="\t")

# Calculate the GCD of the row numbers
gcd = calculate_gcd(grid)

# Output the middle row and the GCD
middle_row = "".join(grid[4])
print(f"Middle Row: {middle_row}")
print(f"GCD: {gcd}")