import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tile = []

for _ in range(N):
    tile.append(list(input().rstrip()))

def dfs(x,y):
    if tile[x][y] == '-':
        tile[x][y] = 1	    # 해당 노드 방문처리
        for _y in [1,-1]:   # 양옆(좌우) 확인하기
            Y = y + _y
            # 좌우 노드가 주어진 범위를 벗어나지 않고 '-'모양이라면 재귀함수 호출
            if (0 < Y < M) and tile[x][Y] == '-':
                dfs(x,Y)
    if tile[x][y] == '|':
        tile[x][y] = 1	    # 해당 노드 방문처리
        for _x in [1,-1]:   # 상하(위아래) 확인하기
            X = x + _x  # 이동하기
            # 상하 노드가 주어진 범위를 벗어나지 않고 '|' 모양이라면 재귀함수 호출
            if (0 < X < N) and tile[X][y] == '|':
                dfs(X,y)
count = 0

for i in range(N):
    for j in range(M):
        if tile[i][j] == '-' or tile[i][j] == '|':
            dfs(i,j)    # 노드가 '-'이나 '|'일 경우에 재귀함수 호출
            count += 1
 
print(count)