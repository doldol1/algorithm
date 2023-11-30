from itertools import combinations

d_list=[]

for _ in range(9):
    d_list.append(int(input()))

# d_list=[7, 8, 10, 13, 15, 19, 20, 23, 25]
# d_list=[8, 6, 5, 1, 37, 30, 28, 22, 36]
# d_list=[20, 10, 20, 19, 10, 15, 25, 8, 13]

d_combi=combinations(d_list, 7)

for i in d_combi:
    if sum(i)==100:
        i=sorted(i)
        for j in i:
            print(j)
        break
