disk_map = [int(x) for x in input().strip()]

def create_dict(disk_map):
    space_dict = {}
    for space_id in range(0, len(disk_map), 2):
        space_dict[space_id // 2] = disk_map[space_id]
        free_space_id = -1 * space_id // 2 - 1
        if space_id + 1 < len(disk_map):
            space_dict[free_space_id] = disk_map[space_id + 1]
    return space_dict

def create_data_structures(disk_map):
    space_dict = {}
    free_space_dict = {}
    for space_id in range(0, len(disk_map), 2):
        space_dict[space_id // 2] = [space_id // 2 for _ in range(0, disk_map[space_id])]
        free_space_id = -1 * space_id // 2 - 1
        if space_id + 1 < len(disk_map):
            free_space_dict[free_space_id] = [0 for _ in range(0, disk_map[space_id + 1])]
    return space_dict, free_space_dict

def calculate_checksum(space_dict, biggest_space_id):
    checksum = 0
    cell_id = 0
    for space_id in range(0, biggest_space_id + 1):
        if space_id not in space_dict:
            break
        while space_dict[space_id] > 0:
            checksum += cell_id * space_id
            cell_id += 1
            space_dict[space_id] -= 1
        free_space_id = -1 * space_id - 1
        while space_dict[free_space_id] > 0:
            while space_dict[biggest_space_id] == 0:
                space_dict.pop(biggest_space_id)
                biggest_space_id -= 1
            if biggest_space_id not in space_dict or biggest_space_id < 0:
                break
            checksum += cell_id * biggest_space_id
            cell_id += 1
            space_dict[free_space_id] -= 1
            space_dict[biggest_space_id] -= 1
    return checksum

def calculate_checksum_v2(space_dict, free_space_dict, biggest_space_id):
    for space_id in range(biggest_space_id, 0, -1):
        free_space_id = -1
        while abs(free_space_id) < space_id and free_space_id in free_space_dict and free_space_dict[free_space_id].count(0) < sum(x != 0 for x in space_dict[space_id]):
            free_space_id -= 1
        if free_space_id not in free_space_dict or free_space_dict[free_space_id].count(0) < sum(x != 0 for x in space_dict[space_id]):
            continue
        j = free_space_dict[free_space_id].index(0)
        for i in range(0, len(space_dict[space_id])):
            free_space_dict[free_space_id][j] = space_dict[space_id][i]
            space_dict[space_id][i] = 0
            j += 1
    
    cell_id = 0
    checksum = 0
    for space_id in range(0, biggest_space_id + 1):
        for i in range(0, len(space_dict[space_id])):
            checksum += cell_id * space_dict[space_id][i]
            cell_id += 1
        free_space_id = -1 * space_id - 1
        if free_space_id not in free_space_dict:
            continue
        for i in range(0, len(free_space_dict[free_space_id])):
            checksum += cell_id * free_space_dict[free_space_id][i]
            cell_id += 1
    return checksum

space_dict = create_dict(disk_map)
biggest_space_id = len(disk_map) // 2
# Star 1
print(calculate_checksum(space_dict, biggest_space_id))
# Star 2
biggest_space_id = len(disk_map) // 2
space_dict, free_space_dict = create_data_structures(disk_map)
print(calculate_checksum_v2(space_dict, free_space_dict, biggest_space_id))
