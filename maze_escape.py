from collections import deque

n, m= map(int, input().split())

a_map=list()

for _ in range(n):
    a_map.append(list(map(int, input())))

# n, m= 5, 6

# a_map=[[1,0,1,0,1,0],
#        [1,1,1,1,1,1],
#        [0,0,0,0,0,1],
#        [1,1,1,1,1,1],
#        [1,1,1,1,1,1]]


deq=deque()

count=0

deq.append((0,0))

while deq:

    x, y=deq.popleft()# x상하 y 좌우

    # 상
    if x-1 >= 0 and a_map[x-1][y]==1:
        deq.append((x-1, y))
        a_map[x-1][y]+=a_map[x][y]
    # 우
    if y+1 < m and a_map[x][y+1]==1:
        deq.append((x, y+1))
        a_map[x][y+1]+=a_map[x][y]
    # 하
    if x+1 < n and a_map[x+1][y]==1:
        deq.append((x+1, y))
        a_map[x+1][y]+=a_map[x][y]
    # 좌
    if y-1 >= 0 and a_map[x][y-1]==1:
        deq.append((x, y-1))
        a_map[x][y-1]+=a_map[x][y]

print(a_map[n-1][m-1])