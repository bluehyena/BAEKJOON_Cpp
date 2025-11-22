import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort()

def search(st, en, target):
    if st == en:
        if nums[st] == target:
            print(1)
        else:
            print(0)
        return
    
    mid = (st + en) // 2

    if nums[mid] < target:
        search(mid + 1, en , target)
    else:
        search(st, mid, target)

for each_target in target_list:
    search(0, N-1, each_target)