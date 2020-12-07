k = int(input())
count_dict = { }
count = 0

def handle_input(value):
    if value != '.':
        dict_values = count_dict.setdefault(value, 0)
        count_dict[value] = dict_values + 1

for _ in range(4):
    list(map(handle_input, list(input())))

for value in count_dict.values():
    if value <= k * 2:
        count += 1

print(count)
