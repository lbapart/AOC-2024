grid = []
while True:
    try:
        grid.append(list(input()))
    except EOFError:
        break

def calculate_square_and_perimeter(grid, x, y, symbol):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return 0, 1
    if grid[x][y] == '-' + symbol:
        return 0, 0
    if grid[x][y] != symbol:
        return 0, 1
    grid[x][y] = '-' + symbol
    res1 = calculate_square_and_perimeter(grid, x + 1, y, symbol)
    res2 = calculate_square_and_perimeter(grid, x - 1, y, symbol)
    res3 = calculate_square_and_perimeter(grid, x, y + 1, symbol)
    res4 = calculate_square_and_perimeter(grid, x, y - 1, symbol)
    return 1 + res1[0] + res2[0] + res3[0] + res4[0], res1[1] + res2[1] + res3[1] + res4[1]

out_of_bounds_coordinates = dict()
def calculate_square(grid, x, y, symbol):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        out_of_bounds_coordinates.setdefault((x, y), 0)
        out_of_bounds_coordinates[(x, y)] += 1
        return 0
    if grid[x][y] == '-' + symbol:
        return 0
    if grid[x][y] != symbol:
        out_of_bounds_coordinates.setdefault((x, y), 0)
        out_of_bounds_coordinates[(x, y)] += 1
        return 0
    grid[x][y] = '-' + symbol
    res1 = calculate_square(grid, x + 1, y, symbol)
    res2 = calculate_square(grid, x - 1, y, symbol)
    res3 = calculate_square(grid, x, y + 1, symbol)
    res4 = calculate_square(grid, x, y - 1, symbol)
    return 1 + res1 + res2 + res3 + res4

def calculate_sides():
    sides = 0
    while len(out_of_bounds_coordinates) > 0:
        cur_key = list(out_of_bounds_coordinates.keys())[0]
        out_of_bounds_coordinates[cur_key] -= 1
        if out_of_bounds_coordinates[cur_key] == 0:
            del out_of_bounds_coordinates[cur_key]
        x, y = cur_key
        sides += 1
        cur_x = x - 1
        was_in = False
        while (cur_x, y) in out_of_bounds_coordinates:
            out_of_bounds_coordinates[cur_x, y] -= 1
            if out_of_bounds_coordinates[cur_x, y] == 0:
                del out_of_bounds_coordinates[cur_x, y]
            cur_x -= 1
            was_in = True
        cur_x = x + 1
        while (cur_x, y) in out_of_bounds_coordinates:
            out_of_bounds_coordinates[cur_x, y] -= 1
            if out_of_bounds_coordinates[cur_x, y] == 0:
                del out_of_bounds_coordinates[cur_x, y]
            cur_x += 1
            was_in = True
        if was_in:
            continue
        cur_y = y - 1
        while (x, cur_y) in out_of_bounds_coordinates:
            out_of_bounds_coordinates[x, cur_y] -= 1
            if out_of_bounds_coordinates[x, cur_y] == 0:
                del out_of_bounds_coordinates[x, cur_y]
            cur_y -= 1
        cur_y = y + 1
        while (x, cur_y) in out_of_bounds_coordinates:
            out_of_bounds_coordinates[x, cur_y] -= 1
            if out_of_bounds_coordinates[x, cur_y] == 0:
                del out_of_bounds_coordinates[x, cur_y]
            cur_y += 1
    return sides

from copy import deepcopy
# Star 1
result = 0
new_grid = deepcopy(grid)
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if new_grid[row][col][0] != '-':
            cur_res = calculate_square_and_perimeter(new_grid, row, col, grid[row][col])
            result += cur_res[0] * cur_res[1]

print(result)

# Star 2 (does not work properly, have no idea why)
result = 0
new_grid = deepcopy(grid)
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if new_grid[row][col][0] != '-':
            out_of_bounds_coordinates.clear()
            cur_res = calculate_square(new_grid, row, col, grid[row][col])
            sides = calculate_sides()
            print(cur_res, sides)
            result += cur_res * sides

print(result)