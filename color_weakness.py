import sys


grid=[]

leng=int(input())
num=0
while num <leng:
    num+=1
    # line=list(sys.stdin.readline().rstrip())
    line=list(input())

    grid.append(line)

# grid=[['R','R','G','G','B'],
#       ['R','G','G','B','R'],
#       ['G','G','R','R','B'],
#       ['R','R','R','B','B'],
#       ['B','R','B','B','B']]


# print(grid)
# leng=len(grid[0])
total_list=list()

# 번호를 풀어서 확인해 볼까?
# 번호 풀어서 확인하기 위해 번호 입력시 해당 좌표값을 출력하는 함수를 만들자
def coord(num, leng=leng, grid=grid):
    i=num // leng
    j=num % leng
    return grid[i][j]

            

# 재귀 형식은 어떤가?
# RRGGB
# RGGBR
# GGRRB
# RRRBB
# BRBBB
# 8개
# 1. 첫번째 값을 받는다. 어디에도 들어가 있지 않으므로 새로운 chunk에 추가한다.
# 2. 값 범위(0~24)를 벗어나지 않는다면 아래와 옆의 값을 확인하는 함수를 실행한다.(재귀)
#    예를 들면, 0번 값 R일 경우 1번 값을 확인하여 chunk안에 추가한 다음, chunk 값을 넘겨 재귀함수를 실행시킨다.
#    재귀함수는 1번을 기준으로 자신의 양 옆과 아래를 확인하며, 
#    chunk안에 없는데 같은 값이 있다면 chunk안에 값을 포함시킨다.
#    만약, chunk안에 값이 있거나 같은 값이 아니라면 아무것도 하지 않는다.
#    재귀함수의 입력은 piv값(기준값)과 chunk이며, return 값은 chunk이다.
def is_in(piv, grid=grid, total_list=total_list):
    for i in total_list:
        if piv in i:
            return True
    return False


def is_covered(piv, leng=leng):
    # l, r, d: left, right, down
    l, r, d=True, True, True

    # piv가 맨 아래 맨 오른쪽 값일 때
    if (piv%leng) == 0 and (piv//leng +1 == leng):
        l, d= False, False
    # piv가 맨 아래 맨 왼쪽 값일 때
    elif piv == leng**2-1:
        r, d= False, False
    # piv가 맨 왼쪽 값일 때
    elif piv%leng == 0:
        l= False
    # piv가 맨 오른쪽 값일 때
    elif piv%leng+1  == leng:
        r= False
    # piv가 맨 아래 값일 때
    elif piv//leng +1 == leng:
        d= False

    return l, r, d

def get_chunk(piv, subset, grid):
    # if is_in(piv):
    #     return subset
    
    subset.add(piv)

    l, r, d= is_covered(piv)


    if l:
        if (coord(piv)==coord(piv-1)) and (piv-1 not in subset):
            # print("piv-1:", piv-1, "탐색")
            subset=get_chunk(piv-1, subset, grid=grid)
    if r:
        if (coord(piv)==coord(piv+1)) and (piv+1 not in subset):
            # print("piv+1:", piv+1, "탐색")
            subset=get_chunk(piv+1,  subset, grid=grid)
    if d:
        if (coord(piv)==coord(piv+leng)) and (piv+leng not in subset):
            # print("piv+leng:", piv+leng, "탐색")
            sebset=get_chunk(piv+leng,  subset, grid=grid)
    
    return subset

for piv in range(leng**2):
    subset=set()
    if is_in(piv, total_list):
        continue
    else:
        subset=get_chunk(piv, subset, grid)
    
    # print("subset:", subset)
    total_list.append(subset)


# 적록버전

# print('적록버전')
for i in range(leng):
    for j in range(leng):
        if grid[i][j]=='R':
            grid[i][j]='G'

# print(grid)
leng=len(grid[0])
total_list2=list()


for piv in range(leng**2):
    subset2=set()
    if is_in(piv, total_list=total_list2):
        continue
    else:
        subset2=get_chunk(piv, subset2, grid)
    
    # print("subset:", subset2)
    total_list2.append(subset2)


print(len(total_list), len(total_list2))
