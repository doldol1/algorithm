a=[1, 2, 3, 4, 5, 5, 5]
remove_set= {3,5}

b=[i for i in a if i not in remove_set]

print(b)


m=3
c=[[0]*m for _ in range(4)]
print(len(c))
print(c)