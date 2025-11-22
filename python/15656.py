import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = list(map(int, input().split()))
result.sort()
out = []

def dfs():
    if len(out) == M:
        print(*out)
        return
    
    for i in range(N):
        out.append(result[i])
        dfs()
        out.pop()

dfs()