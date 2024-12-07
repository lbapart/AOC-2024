to_solve = []

while True:
    try:
        result, numbers = input().split(': ')
    except EOFError:
        break
    numbers = list(map(int, numbers.split(' ')))
    result = int(result)
    to_solve.append((result, numbers))

from functools import reduce
from operator import mul
from itertools import product

def solve(result, numbers):
    n = len(numbers)
    operator_combinations = product(['+', '*'], repeat=n-1)
    
    for operator in operator_combinations:
        cur_result = numbers[0]
        for i in range(1, n):
            if operator[i-1] == '+':
                cur_result += numbers[i]
            else:
                cur_result *= numbers[i]
        if cur_result == result:
            return True
    return False

def solve_v2(result, numbers):
    n = len(numbers)
    operator_combinations = product(['+', '*', '|'], repeat=n-1)
    
    for operator in operator_combinations:
        cur_result = numbers[0]
        for i in range(1, n):
            if operator[i-1] == '+':
                cur_result += numbers[i]
            elif operator[i-1] == '*':
                cur_result *= numbers[i]
            else:
                cur_result = int(str(cur_result) + str(numbers[i]))
        if cur_result == result:
            return True
    return False

res_array = []

for result, numbers in to_solve:
    if solve(result, numbers):
        res_array.append(result)

print(sum(res_array))


res_array = []

for result, numbers in to_solve:
    if solve_v2(result, numbers):
        res_array.append(result)

print(sum(res_array))
    