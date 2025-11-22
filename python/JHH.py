def print_arr(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            print(f"{arr[i][j]:<3}", end=" ")
        print()
    print()


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_arr(arr)

arr_90 = list(map(list, zip(*arr[::-1])))
arr_180 = [a[::-1] for a in arr[::-1]]
arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]

print_arr(arr_90)
print_arr(arr_180)
print_arr(arr_270)

rec = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print_arr(rec)

n, m = len(rec), len(rec[0])
rec_90 = [[0] * n for _ in range(m)]
rec_180 = [[0] * m for _ in range(n)]
rec_270 = [[0] * n for _ in range(m)]

for i in range(n):
    for j in range(m):
        rec_90[j][n - 1 - i] = rec[i][j]
        rec_180[n - 1 - i][m - 1 - j] = rec[i][j]
        rec_270[m - 1 - j][i] = rec[i][j]

print_arr(rec_90)
print_arr(rec_180)
print_arr(rec_270)

arr = [[7 * i + j for j in range(1, 8)] for i in range(7)]
print_arr(arr)

start_y, start_x = 2, 2
length = 3


def rotation_90(start_y, start_x, length):
    n, m = len(arr), len(arr[0])
    new_arr = [[0] * m for _ in range(n)]

    for y in range(start_y, start_y + length):
        for x in range(start_x, start_x + length):
            oy, ox = y - start_y, x - start_x
            ry, rx = ox, length - 1 - oy
            new_arr[ry + start_y][rx + start_x] = arr[y][x]

    for y in range(start_y, start_y + length):
        for x in range(start_x, start_x + length):
            arr[y][x] = new_arr[y][x]


rotation_90(start_y, start_x, length)
print_arr(arr)


graph = [
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 0],
]
print("Origianl Graph")
print_arr(graph)


from collections import deque


def shortest_path(start_y, start_x, end_y, end_x, graph):
    n, m = len(graph), len(graph[0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = set([(start_y, start_x)])
    queue = deque([(start_y, start_x, [(start_y, start_x)])])

    while queue:
        y, x, path = queue.popleft()
        if y == end_y and x == end_x:
            return path

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append((ny, nx, path + [(ny, nx)]))

    return []


def shortest_dist(start_y, start_x, end_y, end_x, graph):
    n, m = len(graph), len(graph[0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = set([(start_y, start_x)])
    queue = deque([(start_y, start_x, 1)])

    while queue:
        y, x, dist = queue.popleft()
        if y == end_y and x == end_x:
            return dist

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append((ny, nx, dist + 1))

    return -1


path = shortest_path(2, 0, 0, 2, graph)
dist = shortest_dist(2, 0, 0, 2, graph)

print(f"Path : {path}")
print(f"Distance : {dist}")


def connection(start_y, start_x, graph, visited):
    n, m = len(graph), len(graph[0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited[start_y][start_x] = True
    queue = deque([(start_y, start_x)])
    component = []

    while queue:
        y, x = queue.popleft()
        component.append((y, x))

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

    return component


def connection_solution(graph):
    n, m = len(graph), len(graph[0])

    visited = [[False] * m for _ in range(n)]
    answer = []

    for y in range(n):
        for x in range(m):
            if graph[y][x] and not visited[y][x]:
                answer.append(connection(y, x, graph, visited))

    return answer


def flood_fill(start_y, start_x, graph, visited, new_color):
    n, m = len(graph), len(graph[0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited[start_y][start_x] = True
    queue = deque([(start_y, start_x)])
    base_color = graph[start_y][start_x]

    while queue:
        y, x = queue.popleft()
        graph[y][x] = new_color

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == base_color and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))


def flood_fill_solution(graph):
    n, m = len(graph), len(graph[0])
    visited = [[False] * m for _ in range(n)]

    new_color = -1

    for y in range(n):
        for x in range(m):
            if graph[y][x] and not visited[y][x]:
                flood_fill(y, x, graph, visited, new_color)
                new_color -= 1


answer = connection_solution(graph)
print()
print("Connection Component")
for a in answer:
    print(a)
print()


flood_fill_solution(graph)
print_arr(graph)


print("====================")
print("확률 관련 함수")
arr = [1, 2, 3, 4]
visited = [0] * len(arr)


def permutation(n, new_arr):
    global arr, visited
    if len(new_arr) == n:
        print(new_arr)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            permutation(n, new_arr + [arr[i]])
            visited[i] = False


def production(n, new_arr):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return

    for i in range(len(arr)):
        production(n, new_arr + [arr[i]])


def combination(n, new_arr, c):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return

    for i in range(c, len(arr)):
        combination(n, new_arr + [arr[i]], i + 1)


def combination_with_replacement(n, new_arr, c):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return

    for i in range(c, len(arr)):
        combination_with_replacement(n, new_arr + [arr[i]], i)


print("permutation")
permutation(2, [])
print("production")
production(2, [])
print("combination")
combination(2, [], 0)
print("combination_with_replacement")
combination_with_replacement(2, [], 0)


print("=========================")
print("Gravity")
arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]
print("Gravity 이전 Array")
print_arr(arr)


def gravity():
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            p = i - 1
            while p >= 0 and arr[p][j] == 1 and arr[p + 1][j] == 0:
                arr[p][j], arr[p + 1][j] = arr[p + 1][j], arr[p][j]
                p -= 1


gravity()
print("gravity 이후 Array")
print_arr(arr)
