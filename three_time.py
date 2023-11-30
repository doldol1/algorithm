# n=int(input())

# print(n)
# count=0

# for i in range(60):
#     if '3' in str(i):
#         print('i:', i)
#         count+=1
#         continue
#     for j in range(60):
#         if '3' in str(j):
#             count+=1
#             print('j:', j, 'i:', i)
#             continue
#         for k in range(n+1):
#             if '3' in str(k):
#                 count+=1

# print(count)
# 틀린 코드




h=int(input())

count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                print(i,'시', j, '분', k, '초')
                count+=1

print(count)