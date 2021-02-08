numbers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
visited = [0, 0, 0, 0, 0, 0, 0, 0, 0]
x = 0


def visited_nodes(v, n, lenght):
    global numbers, x
    if lenght < 1:
        return 0

    newv = list(v)
    newv[n] = 1
    # print(newv)
    for i in range(9):
        if i != n and v[i] == 0:
            visited_nodes(newv, i, lenght-1)
    x += 1


visited_nodes(visited, 4, 2)
print("x: " + str(x))

