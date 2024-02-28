shopping_list_set = set()
shopping_list_items = []
shopping_list = {}
total = 0

# raw_list.txt read
with open('raw_list.txt') as file:
    raw_list = file.readlines()

# raw_list.txt parsed
for i in raw_list:
    if len(i.split(' - ')) == 2 :
        shopping_list_set.add(i.replace(' g\n', '').split(' - ')[0])
        shopping_list_items.append(i.replace(' g\n', '').split(' - '))

# items compared and values summed
for j in shopping_list_set:
    for item in shopping_list_items:
        if j in item:
            total += int(item[1])
        shopping_list[j] = total
    total = 0

print(shopping_list)