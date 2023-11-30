n=int(input())

matrix=list()
for _ in range(n):
    matrix.append(list(map(int,input().split())))


############ preset ##################
# n=3
# matrix=[[0, 1, 0],
#         [0, 0, 1],
#         [1, 0, 0]]

########################################
# n=7
# matrix=[[0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 1],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 1, 0],
#         [1, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 1],
#         [0, 0, 1, 0, 0, 0, 0]]
#####################################

############ input test############
# print(n)

# for i in matrix:
#     print(i)
###############################

### 다시 DFS로 ####
# 방문 기록을 만들어 재귀형으로 순회

def pathfind(matrix, start, visited_list):
    for i in range(n):
        if matrix[start][i]==1 and visited_list[i]==0:
            visited_list[i]=1
            pathfind(matrix, i, visited_list)
    return visited_list

result=list()
for start in range(n):
    visited_list=[0]*n
    result.append(pathfind(matrix, start, visited_list))

for prt in result:
    print(" ".join(map(str, prt)))

# 생각
# DFS 재귀함수 사용하여 각 이동 가능 matrix 구현
# 재귀함수 매개변수: matrix, 출발 node i 정보, i에서 어디로 갈 수 있는지를 확인하는 list
# 단순히 순회하도록 만들면 circle 형태를 띄기 때문에 무한히 순회할 수 있다. 어떻게 이를 막지?
# 재귀함수에서, node a에 대해 경로를 모르는 상태에서 node a로 갈 수 있다면, 
################ 위의 접근 방식의 tree가 아니기 때문에 해결하기 어려움###############3
# gpt의 플로이드 마샬 알고리즘을 응용하여 만들어보기
# i에 대한 j의 경로를 순차적으로 업데이트
# 만약 출발 i에서 j로 갈 수 있다면 갈 수 있는 j들을 모아 집합을 만든 다음
# j에서 k로 갈 수 있는지 확인하여 i->k가 가능하도록 업데이트한다.
# 이 짓을 n번 반복하면, 갈 수 있는 node와 갈 수 없는 node를 가릴 수 있다. 어차피 node가 n개 존재할 때 circle이 생기지 않는 최장 경로는 n-1이기 때문
# 이 짓을 다음 출발에 반복한다.

# for i in range(n):
#     for _ in range(n):
#         for j in range(n):
#             if matrix[i][j]==1:
#                 for k in range(n):
#                     if matrix[j][k]==1:
#                         matrix[i][k]=1

# for prt in matrix:
#     print(" ".join(map(str, prt)))
    # for el in prt:
    #     print(el, end=' ')