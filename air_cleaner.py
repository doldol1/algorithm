# 입력받기
# r= row, c= column, t= time passed
# r, c, t= map(int, input().split(' '))
r, c, t= 7, 8, 30


# 격자 입력
# r_grid=list()
# for row in range(r):
#     r_grid.append(list(map(int, input().split(' '))))
r_grid=[[0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 3, 0, 0, 8],
        [-1, 0, 5, 0, 0, 0, 22, 0],
        [-1, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 10, 43, 0],
        [0, 0, 5, 0, 15, 0, 0, 0],
        [0, 0, 40, 0, 0, 0, 20, 0]] 


# 리스트 element-wise 더하기
def list_elwise(x, y, r, c):
    for row in range(r):
        for col in range(c):
            x[row][col]+=y[row][col]

    return x

# 공기 순환 함수
def grid_circulate(x, r, c):

    # 공기청정기 위치 찾기
    for row in range(r):
        if x[row][0]== -1:
            c_up=row
            c_down=row+1
            break
        
    # 위쪽 반시계방향 순환
    m1=0
    m2=0
    
    # 왼쪽->오른쪽 이동
    for col in range(1, c):
        if col==1:
            m1=x[c_up][col]
            x[c_up][col]=0

        else:
            m2=x[c_up][col]
            x[c_up][col]=m1
            m1=m2
    
    # 아래->위 이동
    for row in range(c_up-1, -1, -1):
        m2=x[row][c-1]
        x[row][c-1]=m1
        m1=m2
    
    # 오른쪽->왼쪽 이동
    for col in range(c-2, -1, -1):
        m2=x[0][col]
        x[0][col]=m1
        m1=m2
    
    # 위->아래 이동
    for row in range(0, c_up):
        if row== c_up-1:
            x[row][0]=m1
            break
        m2=x[row][0]
        x[row][0]=m1
        m1=m2



    # 아래쪽 시계방향 순환
    m1=0
    m2=0

    # 왼쪽->오른쪽 이동
    for col in range(1, c):
        if col==1:
            m1=x[c_down][col]
            x[c_down][col]=0
        else:
            m2=x[c_down][col]
            x[c_down][col]=m1
            m1=m2

    # 위->아래 이동
    for row in range(c_down+1, r):
        m2=x[row][c-1]
        x[row][c-1]=m1
        m1=m2

    # 오른쪽->왼쪽 이동
    for col in range(c-2, -1, -1):
        m2=x[r-1][col]
        x[r-1][col]=m1
        m1=m2
    
    # 아래->위 이동
    for row in range(r-2, c_down, -1):
        if row== c_down-1:
            x[row][0]=m1
            break
        m2=x[row][0]
        x[row][0]=m1
        m1=m2
    
    return x





# 확산시 동시에 일어나는 것이고, 순차적이지 않기 때문에 각 좌표에 가감할
# grid용 리스트가 하나 더 필요하다.
for time in range(1, t+1):
    dust_move=[[0 for col in range(c)] for row in range(r)]    
    
    # 미세먼지 확산
    for row in range(r):
        for col in range(c):
            if r_grid[row][col]==0 or r_grid[row][col]==-1:
                pass
            else:
                dust=r_grid[row][col]//5
                d_count=0

                # 방향별 확산 가능 여부 확인
                # 북
                if row-1 >= 0 and r_grid[row-1][col] != -1:
                    dust_move[row-1][col]+=dust
                    d_count+=1
                # 남
                if row+1 < r and r_grid[row+1][col] != -1:
                    dust_move[row+1][col]+=dust
                    d_count+=1
                # 서
                if col-1 >= 0 and r_grid[row][col-1] != -1:
                    dust_move[row][col-1]+=dust
                    d_count+=1
                # 동
                if col+1 < c and r_grid[row][col+1] != -1:
                    dust_move[row][col+1]+=dust
                    d_count+=1
                
                dust_move[row][col]-=d_count*dust
                

    r_grid=list_elwise(r_grid, dust_move, r, c)

    # print(f'{time} 회차 먼지 이동')
    # for i in r_grid:
    #     print(i)
    

    # 공기 순환
    r_grid=grid_circulate(r_grid, r, c)
    
    # print(f'{time} 회차 공기 순환')
    # for i in r_grid:
    #     print(i)


# 미세먼지 합 출력
total=0
for s in r_grid:
    total+=sum(s)
total+=2

print(total)