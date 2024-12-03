in_str = open("input").read().strip()
muls = []

def check_right_part(in_str, i):
    i += 1
    if i == len(in_str) or not in_str[i].isdigit():
        return 0
    str_num = ""
    while i < len(in_str) and in_str[i].isdigit():
        str_num += in_str[i]
        i += 1
    if i == len(in_str) or in_str[i] != ')':
        return 0
    return int(str_num)

def check_left_part(in_str, i):
    i -= 1
    if i == -1 or not in_str[i].isdigit():
        return 0
    str_num = ""
    while i >= 0 and in_str[i].isdigit():
        str_num = in_str[i] + str_num
        i -= 1
    if i == -1 or in_str[i] != '(':
        return 0
    if in_str[i - 3: i] != "mul":
        return 0
    return int(str_num)

def check_dont(in_str, i):
    if in_str[i - 5: i] == "don't" and i + 1 < len(in_str) and in_str[i + 1] == ')':
        return True
    return False

def check_do(in_str, i):
    if in_str[i - 2: i] == "do" and i + 1 < len(in_str) and in_str[i + 1] == ')':
        return True
    return False

def check_and_append_mul():
    for i in range(len(in_str)):
        if in_str[i] == ',':
            result = check_right_part(in_str, i) * check_left_part(in_str, i)
            if result != 0:
                muls.append(result)
    return

def check_and_append_mul_v2():
    do = True
    for i in range(len(in_str)):
        if in_str[i] == ',' and do:
            result = check_right_part(in_str, i) * check_left_part(in_str, i)
            if result != 0:
                muls.append(result)
        if in_str[i] == '(':
            if check_do(in_str, i):
                do = True
            elif check_dont(in_str, i):
                do = False
    return
# Star 1
check_and_append_mul()
print(sum(muls))

# Star 2
muls = []
check_and_append_mul_v2()
print(sum(muls))