numbers = list(input().split())


from functools import cache

@cache
def solve(number, blinks):
    if blinks == 0:
        return 1
    elif number == "0":
        return solve("1", blinks - 1)
    elif len(number) % 2 == 0:
        return solve(str(int(number[:len(number) // 2])), blinks - 1) + solve(str(int(number[len(number) // 2:])), blinks - 1)
    else:
        return solve(str(int(number) * 2024), blinks - 1)

result = 0
for i in range(len(numbers)):
    result += solve(numbers[i], 25)
          
print(result)

result = 0
for i in range(len(numbers)):
    result += solve(numbers[i], 75)
    
print(result)