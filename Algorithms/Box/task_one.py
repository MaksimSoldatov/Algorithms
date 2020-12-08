def generateMatrix(n):
    array = [[0]*n for i in range(n)]

    values = n * n
    direction = -1
    steps = 0
    last_arr = 0
    last_index = 0

    for index, value in enumerate(range(1, n + 1)):
        array[0][index] = value
        values -= 1
        steps += 1
        last_index = index
    n -= 1

    while values != 0:

        # Up/Down
        for i in range(steps + 1, steps + n + 1):
            steps += 1
            values -= 1
            # Down
            if direction < 0:
                last_arr += 1
                array[last_arr][last_index] = i
            # Up
            else:
                last_arr -= 1
                array[last_arr][last_index] = i

        #Right/left
        for i in range(steps + 1, steps + n + 1):
            steps += 1
            values -= 1
            # Left
            if direction < 0:
                last_index -= 1
                array[last_arr][last_index] = i
            # Right
            else:
                last_index += 1
                array[last_arr][last_index] = i

        direction *= -1
        n -= 1

    print(array)