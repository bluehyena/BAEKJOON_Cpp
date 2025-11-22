import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = []

def dfs(start):
    if len(result) == M:
        print(*result)
        return

    for i in range(start, len(data)):
        if not data[i] in result:
            result.append(data[i])
            dfs(i+1)
            result.pop()

dfs(0)