from bisect import bisect_left, bisect_right

area = []

directions = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

while True:
    try:
        line = list(input())
        area.append(line)
    except EOFError:
        break
    

def get_guard_position(area):
    for row in range(len(area)):
        for col in range(len(area[row])):
            if area[row][col] in directions:
                return (row, col)
            
def switch_direction(direction):
    if direction == '^':
        return '>'
    if direction == '>':
        return 'v'
    if direction == 'v':
        return '<'
    if direction == '<':
        return '^'
    
def get_next_position(position, direction):
    try:
        next_cell = area[position[0] + directions[direction][0]][position[1] + directions[direction][1]]
        if next_cell == '#':
            return 0
        return 1
    except IndexError:
        return -1

def simulate(area_in):
    position = get_guard_position(area_in)
    direction = area_in[position[0]][position[1]]
    # row: [cols]
    obstacles_rows = dict()
    # col: [rows]
    obstacles_cols = dict()
    visited = 1
    while True:
        if area_in[position[0]][position[1]] == '.':
            visited += 1
        area_in[position[0]][position[1]] = 'X'
        next_position = get_next_position(position, direction)
        if next_position == -1:
            break
        if next_position == 0:
            obstacles_rows.setdefault(position[0] + directions[direction][0], []).append(position[1] + directions[direction][1])
            obstacles_cols.setdefault(position[1] + directions[direction][1], []).append(position[0] + directions[direction][0])
            direction = switch_direction(direction)
        position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
    for key, value in obstacles_rows.items():
        obstacles_rows[key] = sorted(value)
    for key, value in obstacles_cols.items():
        obstacles_cols[key] = sorted(value)
    return visited, obstacles_rows, obstacles_cols

def get_next_obstacle(position, direction, obstacles_rows, obstacles_cols):
    col_obstacles = obstacles_cols.get(position[1], [])
    row_obstacles = obstacles_rows.get(position[0], [])
    next_direction = switch_direction(direction)
    if direction == '^' and col_obstacles:
        next_obstacle = bisect_right(col_obstacles, position[0])
        if next_obstacle == 0:
            return None, None, None
        next_position = (col_obstacles[next_obstacle - 1] + 1, position[1])
        return next_direction, next_position, (col_obstacles[next_obstacle - 1], position[1])
    if direction == 'v' and col_obstacles:
        next_obstacle = bisect_left(col_obstacles, position[0])
        if next_obstacle == len(col_obstacles):
            return None, None, None
        next_position = (col_obstacles[next_obstacle] - 1, position[1])
        return next_direction, next_position, (col_obstacles[next_obstacle], position[1])
    if direction == '>' and row_obstacles:
        next_obstacle = bisect_left(row_obstacles, position[1])
        if next_obstacle == len(row_obstacles):
            return None, None, None
        next_position = (position[0], row_obstacles[next_obstacle] - 1)
        return next_direction, next_position, (position[0], row_obstacles[next_obstacle])
    if direction == '<' and row_obstacles:
        next_obstacle = bisect_right(row_obstacles, position[1])
        if next_obstacle == 0:
            return None, None, None
        next_position = (position[0], row_obstacles[next_obstacle - 1] + 1)
        return next_direction, next_position, (position[0], row_obstacles[next_obstacle - 1])
    return None, None, None
        

def simulate_v2(area_in):
    start_position = get_guard_position(area_in)
    direction = area_in[start_position[0]][start_position[1]]
    position = start_position
    _, obstacles_rows, obstacles_cols = simulate(area_in)
    count = set()
    while True:
        next_position = get_next_position(position, direction)
        if next_position == -1:
            break
        if next_position == 0:
            direction = switch_direction(direction)
            continue
        next_position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
        obstacles_rows.setdefault(next_position[0], []).insert(bisect_left(obstacles_rows.get(next_position[0], []), next_position[1]), next_position[1])
        obstacles_cols.setdefault(next_position[1], []).insert(bisect_left(obstacles_cols.get(next_position[1], []), next_position[0]), next_position[0])
        area_in[next_position[0]][next_position[1]] = '#'
        new_position = position
        new_direction = direction
        visited_obstacles = set()
        while True and (next_position[0] != start_position[0] or next_position[1] != start_position[1]):
            new_direction, new_position, new_obstacle = get_next_obstacle(new_position, new_direction, obstacles_rows, obstacles_cols)
            if new_position is None:
                break
            if new_obstacle in visited_obstacles:
                count.add((next_position[0], next_position[1], position[0], position[1]))
                break
            visited_obstacles.add(new_obstacle)
        obstacles_cols[next_position[1]].remove(next_position[0])
        obstacles_rows[next_position[0]].remove(next_position[1])
        area_in[next_position[0]][next_position[1]] = 'X'
        position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
    return len(count)
        

import copy
area_copy = copy.deepcopy(area)
# Star 1
result = simulate(area_copy)
print(result[0])

# Star 2
area_copy = copy.deepcopy(area)
result = simulate_v2(area_copy)
print(result)
