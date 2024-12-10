in_map = []

while True:
    try:
        in_line = [int(x) for x in input().strip()]
    except EOFError:
        break
    in_map.append(in_line)
    

nines_set = set()
def check_trails(prev_height, i, j, in_map):
    if i < 0 or i >= len(in_map) or j < 0 or j >= len(in_map[i]):
        return 0
    if in_map[i][j] == 9 and prev_height == 8:
        nines_set.add((i, j))
        return 1
    if prev_height + 1 != in_map[i][j]:
        return 0
    
    return (
        check_trails(in_map[i][j], i + 1, j, in_map) +
        check_trails(in_map[i][j], i, j + 1, in_map) +
        check_trails(in_map[i][j], i - 1, j, in_map) +
        check_trails(in_map[i][j], i, j - 1, in_map)
    )
    
# Star1
result = 0
for i in range(len(in_map)):
    for j in range(len(in_map[i])):
        if in_map[i][j] == 0:
            nines_set.clear()
            check = check_trails(-1, i, j, in_map)
            result += len(nines_set)
print(result)

result = 0
for i in range(len(in_map)):
    for j in range(len(in_map[i])):
        if in_map[i][j] == 0:
            nines_set.clear()
            check = check_trails(-1, i, j, in_map)
            result += check
print(result)