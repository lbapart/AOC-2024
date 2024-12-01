leftlist , rightlist = [], []

while True:
    try:
        numbers = input().split()
    except:
        break
    leftlist.append(int(numbers[0]))
    rightlist.append(int(numbers[1]))

# First star
leftlist.sort()
rightlist.sort()

result = 0
for i in range(len(leftlist)):
    result += abs(leftlist[i] - rightlist[i])

print(result)

# Second star
from collections import Counter
rightCounter = Counter(rightlist)
result = 0
for item in leftlist:
    if item in rightCounter:
        result += item * rightCounter[item]

print(result)