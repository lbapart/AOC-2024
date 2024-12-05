orders = dict()
updates = []
result = []
while True:
    line = input().strip()
    if not line:
        break
    num1, num2 = map(int, line.split('|'))
    if num1 in orders:
        orders[num1].add(num2)
    else:
        orders[num1] = set([num2])
        
while True:
    try:
        array = list(map(int, input().split(',')))
        updates.append(array)
    except EOFError:
        break

def is_printable(update):
    printed_pages = set()
    for j in range(len(update)):
        for page in printed_pages:
            if update[j] in orders and page in orders[update[j]]:
                return False
        printed_pages.add(update[j])
    return True


def is_printable_v2(update):
    printed_pages = []
    for j in range(0, len(update)):
        was_inserted = False
        for i in range(len(printed_pages)):
            if update[j] in orders and printed_pages[i] in orders[update[j]]:
                was_inserted = True
                printed_pages.insert(i, update[j])
                break
        if not was_inserted:
            printed_pages.append(update[j])
    return printed_pages[len(printed_pages) // 2]

# Star 1
for update in updates:
    if is_printable(update):
        result.append(update[len(update) // 2])
print(sum(result))

# Star 2
result = []
for update in updates:
    if not is_printable(update):
        result.append(is_printable_v2(update))
print(sum(result))