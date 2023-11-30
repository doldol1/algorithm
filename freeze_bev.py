import sys

m, n= map(int, input().split())

grid=list()

for _ in range(m):
    grid.append(list(map(int, input())))

# m, n= 4, 5
# grid=[[0,0,1,1,0],
#       [0,0,0,1,1],
#       [1,1,1,1,1],
#       [0,0,0,0,0]]

tf=[[False]*n for _ in range(m)]

def dfs(grid, i, j, tf):
    tf[i][j]=True
    # 상단
    if (i-1 > -1 and j > -1) and (i < m and j < n) and grid[i-1][j]==0 and tf[i-1][j]==False:
        dfs(grid, i-1, j, tf)
    # 좌측
    if (i > -1 and j-1 > -1) and (i < m and j < n) and grid[i][j-1]==0 and tf[i][j-1]==False:
        tf=dfs(grid, i, j-1, tf)
    # 우측
    if (i > -1 and j > -1) and (i < m and j+1 < n) and grid[i][j+1]==0 and tf[i][j+1]==False:
        tf=dfs(grid, i, j+1, tf)
    # 하단
    if (i > -1 and j > -1) and (i+1 < m and j < n) and grid[i+1][j]==0 and tf[i+1][j]==False:
        tf=dfs(grid, i+1, j, tf)

    return tf

count=0

for i in range(m):
    for j in range(n):
        if grid[i][j]==0 and tf[i][j]==False:
            tf=dfs(grid, i, j, tf)
            count+=1

print(count)