from collections import deque

S = int(input())
visited = [[-1] * (S+1) for _ in range(S+1)]
queue = deque()
queue.append((1,0))
visited[1][0] = 0

while queue:
    screen, clip = queue.popleft()

    if screen == S:
        print(visited[screen][clip])
        break

    # screen -> clipboard
    if visited[screen][screen] == -1:
        visited[screen][screen] = visited[screen][clip] + 1
        queue.append((screen,screen))

    # clip -> screen
    if screen + clip <= S and visited[screen + clip][clip] == -1:
        visited[screen + clip][clip] = visited[screen][clip] + 1
        queue.append((screen + clip, clip))
    
    # delete emoji
    if screen - 1 >= 0 and visited[screen - 1][clip] == -1:
        visited[screen-1][clip] = visited[screen][clip] + 1
        queue.append((screen - 1, clip))
