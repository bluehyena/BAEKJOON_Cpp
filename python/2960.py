N, K = map(int, input().split())  
cnt = 0  
nums = [True] * (N+1)  

for i in range(2, N+2):  
    for j in range(i, N+1, i):  
        if nums[j] == True:  
            nums[j] = False  
            cnt += 1  
            if cnt == K:  
                print(j)  
                break