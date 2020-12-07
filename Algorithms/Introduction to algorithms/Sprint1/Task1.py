array_length = int(input())
source = [int(x) for x in input().split()]

def find_neighbors():
    previous_zero_index = -1
    count = 0
    result = []
    for index, value in enumerate(source):
        count += 1

        if value == 0:
            if index == 0:
                previous_zero_index = 0
                count = 0
                result.append(0)
                continue

            if previous_zero_index == -1:
                result[0: index] = reversed(result[0:index])
                previous_zero_index = index
                count = 0
                result.append(0)
                continue

            result.append(0)
            diff = (index - previous_zero_index) // 2
            result[index - diff: index] = reversed(result[previous_zero_index + 1: previous_zero_index + 1 + diff])

            previous_zero_index = index
            count = 0
            continue

        result.append(count)
    for i in result:
        print(i, end=" ")

find_neighbors()
