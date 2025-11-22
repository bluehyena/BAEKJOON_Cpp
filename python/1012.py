import sys
input = sys.stdin.readline

# 테스틐 케이스
T = int(input())

# 방향
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

# bfs
def bfs(y, x):
    # q에 넣고 방문처리
    q = [(y,x)]
    napa[y][x] = 0

    # q가 비지 않는한
    while q:
        y,x = q.pop(0)
        # bfs 수행
        for i in range(4):
            # 다음 좌표
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖이면 패스
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            # 배추가 있으면 q에 할당 후 0으로 변환
            if napa[ny][nx] == 1:
                q.append((ny, nx))
                napa[ny][nx] = 0
  
for _ in range(T):
    # 인풋받고, napa 초기화 
    M,N,K = map(int, input().split())
    cnt = 0
    napa = [[0] * M for _ in range(N)]

    # napa 좌표따라 심기기
    for _ in range(K):
        x, y = map(int, input().split())
        napa[y][x] = 1


    for j in range(N):
        for i in range(M):
            if napa[j][i] == 1:
                bfs(j, i)
                cnt += 1

    print(cnt)