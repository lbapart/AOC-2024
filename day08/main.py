field = []

while True:
    try:
        field.append(list(input()))
    except EOFError:
        break


def get_antennas(field):
    antennas = {}
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j].isdigit() or field[i][j].isalpha():
                antennas.setdefault(field[i][j], []).append((i, j))
    return antennas

def calculate_antinodes(antennas, n, m):
    result = 0
    antinodes = set()
    for key, value in antennas.items():
        if len(value) == 1:
            continue
        for i in range(len(value)):
            for j in range(i+1, len(value)):
                x1, y1 = value[i]
                x2, y2 = value[j]
                diff_node = (x2 - x1, y2 - y1)
                x3, y3 = x2 + diff_node[0], y2 + diff_node[1]
                x4, y4 = x1 - diff_node[0], y1 - diff_node[1]
                if x3 >= 0 and x3 < n and y3 >= 0 and y3 < m:
                    antinodes.add((x3, y3))
                if x4 >= 0 and x4 < n and y4 >= 0 and y4 < m:
                    antinodes.add((x4, y4))
    return len(antinodes)

def calculate_antinodes_v2(antennas, n, m):
    result = 0
    antinodes = set()
    for key, value in antennas.items():
        if len(value) == 1:
            continue
        for i in range(len(value)):
            for j in range(i+1, len(value)):
                x1, y1 = value[i]
                x2, y2 = value[j]
                antinodes.add((x1, y1))
                antinodes.add((x2, y2))
                diff_node = (x2 - x1, y2 - y1)
                x3, y3 = x2 + diff_node[0], y2 + diff_node[1]
                x4, y4 = x1 - diff_node[0], y1 - diff_node[1]
                while x3 >= 0 and x3 < n and y3 >= 0 and y3 < m:
                    antinodes.add((x3, y3))
                    x3 += diff_node[0]
                    y3 += diff_node[1]
                while x4 >= 0 and x4 < n and y4 >= 0 and y4 < m:
                    antinodes.add((x4, y4))
                    x4 -= diff_node[0]
                    y4 -= diff_node[1]
    return len(antinodes)


antennas = get_antennas(field)
n, m = len(field), len(field[0])
# Star 1
print(calculate_antinodes(antennas, n, m))

# Star 2
print(calculate_antinodes_v2(antennas, n, m))