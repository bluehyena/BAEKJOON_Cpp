import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))
result = []

def dfs(start):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(start, N):
        result.append(data[i])
        dfs(i)
        result.pop()

dfs(0)