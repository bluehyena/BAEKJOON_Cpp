import sys
input = sys.stdin.readline
N, M = map(int, input().split())

idx_name = {}
name_idx = {}

for i in range(1, N+1):
    name = input().rstrip()
    idx_name[i] = name
    name_idx[name] = i 

for _ in range(M):
    query = input().rstrip()
    if query.isdigit():
        print(idx_name[int(query)])
    else:
        print(name_idx[query])
