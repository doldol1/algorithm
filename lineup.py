from collections import deque

n, m=map(int, input().split(' '))


graphs=[None]+[[] for _ in range(1,n+1)]
in_dim=[None]+[0]*n # 나한테 올 수 있는 node들
lined=list()
que=deque()

for _ in range(m):
    a, b=map(int,input().split(' '))
    graphs[a].append(b)
    in_dim[b]+=1

################ input test ###########33
# print(n, m)
# for i in comp_list:
#     print(i)
#################################

# chatgpt에게 위상 정렬 알고리즘 추천받음

for i in range(1,n+1):
    if in_dim[i]==0:
        que.append(i)

while que:
    pop=que.popleft()
    lined.append(pop)
    if graphs[pop]:
        for j in graphs[pop]:
            in_dim[j]-=1
            if in_dim[j]==0:
                que.append(j)

print(' '.join(map(str,lined)))
















# n, m=map(int, input().split(' '))


# graphs=[None]+[[] for _ in range(1,n+1)]
# in_dim=[None]+[0]*n # 나한테 올 수 있는 node들
# lined=list()

# for _ in range(m):
#     a, b=map(int,input().split(' '))
#     graphs[a].append(b)
#     in_dim[b]+=1

# ################ input test ###########33
# # print(n, m)
# # for i in comp_list:
# #     print(i)
# #################################

# # chatgpt에게 위상 정렬 알고리즘 추천받음

# while len(lined)!=n:
#     for i in range(1,n+1):
#         if in_dim[i]==0:
#             lined.append(i)
#             in_dim[i]=-1
#             if graphs[i]:
#                 for j in graphs[i]:
#                     in_dim[j]-=1

# print(' '.join(map(str,lined)))













# n, m=map(int, input().split(' '))

# comp_list=list()
# for _ in range(m):
#     comp_list.append(list(map(int,input().split(' '))))

# ################ input test ###########33
# # print(n, m)
# # for i in comp_list:
# #     print(i)
# #################################

# # chatgpt에게 위상 정렬 알고리즘 추천받음

# graphs=[None]+[[] for _ in range(1,n+1)]
# in_dim=[None]+[0]*n # 나한테 올 수 있는 node들
# lined=list()

# for i in comp_list:
#     graphs[i[0]].append(i[1])
#     in_dim[i[1]]+=1

    
    

# while len(lined)!=n:
#     for i in range(1,n+1):
#         if in_dim[i]==0:
#             lined.append(i)
#             in_dim[i]=-1
#             if graphs[i]:
#                 for j in graphs[i]:
#                     in_dim[j]-=1

# print(' '.join(map(str,lined)))