from collections import deque

y, x= map(int, input().split(' '))
print(x, y)


ch_grid=list()

for h in range(y):
    ch_grid.append(list(map(int,input().split(' '))))
for i in ch_grid:
    print(i)

y, x= 13, 12

ch_grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
         [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
