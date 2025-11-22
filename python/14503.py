import sys
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while True:
    if map[y][x] == 0:   
        map[y][x] = 2
        cnt += 1
    sw = False
    for i in range(1,5):
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 0:
                d = d - i
                y = ny
                x = nx
                break

    if sw == False:
        ny = y - dy[d]
        nx = x - dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx
        else:
            break

print(cnt)
