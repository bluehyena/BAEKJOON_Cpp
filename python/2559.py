import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
each = 0

for i in range(k):
    each += lst[i]
maxv = each

for i in range(k, n):
    each += lst[i]
    each -= lst[i-k]
    maxv = max(maxv, each)

print(maxv)