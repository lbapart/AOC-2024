
xmas = ['X', 'M', 'A', 'S']
matrix = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        matrix.append(list(line))
    except EOFError:
        break

def check_vertical_down(row, col):
    for i in range(4):
        if row + i >= len(matrix) or matrix[row + i][col] != xmas[i]:
            return 0
    return 1

def check_vertical_up(row, col):
    for i in range(4):
        if row - i < 0 or matrix[row - i][col] != xmas[i]:
            return 0
    return 1

def check_horizontal_right(row, col):
    for i in range(4):
        if col + i >= len(matrix[row]) or matrix[row][col + i] != xmas[i]:
            return 0
    return 1

def check_horizontal_left(row, col):
    for i in range(4):
        if col - i < 0 or matrix[row][col - i] != xmas[i]:
            return 0
    return 1


def check_diagonal_down_right(row, col):
    for i in range(4):
        if row + i >= len(matrix) or col + i >= len(matrix[row]) or matrix[row + i][col + i] != xmas[i]:
            return 0
    return 1

def check_diagonal_down_left(row, col):
    for i in range(4):
        if row + i >= len(matrix) or col - i < 0 or matrix[row + i][col - i] != xmas[i]:
            return 0
    return 1

def check_diagonal_up_right(row, col):
    for i in range(4):
        if row - i < 0 or col + i >= len(matrix[row]) or matrix[row - i][col + i] != xmas[i]:
            return 0
    return 1

def check_diagonal_up_left(row, col):
    for i in range(4):
        if row - i < 0 or col - i < 0 or matrix[row - i][col - i] != xmas[i]:
            return 0
    return 1

def check_all_directions(row, col):
    return (
        check_vertical_down(row, col) +
        check_vertical_up(row, col) +
        check_horizontal_right(row, col) +
        check_horizontal_left(row, col) +
        check_diagonal_down_right(row, col) +
        check_diagonal_down_left(row, col) +
        check_diagonal_up_right(row, col) +
        check_diagonal_up_left(row, col)
    )

def check_x_mas(row, col):
    try:
        resLeft = ''
        resRight = ''
        if matrix[row][col] == 'A':
            resLeft = matrix[row - 1][col - 1] + matrix[row][col] + matrix[row + 1][col + 1]
            resRight = matrix[row - 1][col + 1] + matrix[row][col] + matrix[row + 1][col - 1]
        if resLeft not in ['MAS', 'SAM']:
            return 0
        if resRight not in ['MAS', 'SAM']:
            return 0
        return 1
    except:
        return 0
                

def find_xmas():
    result = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            result += check_all_directions(row, col)
    return result

def find_x_mas():
    result = 0
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            result += check_x_mas(row, col)
    return result
# Star 1
print(find_xmas())

# Star 2
print(find_x_mas())
