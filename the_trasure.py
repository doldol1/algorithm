n= int(input())

a_list=list(map(int, input().split(' ')))
b_list=list(map(int, input().split(' ')))

# n=5
# a_list=[1, 1, 1, 6, 0]
# b_list=[2, 7, 8, 3, 1]

# n=3
# a_list=[1, 1, 3]
# b_list=[10, 30, 20]

# n=9
# a_list=[5, 15, 100, 31, 39, 0, 0, 3, 26]
# b_list=[11, 12, 13, 2, 3, 4, 5, 9, 1]

a_sorted=sorted(a_list)
b_sorted=sorted(b_list)


total=0
for i in range(n):
    total+=a_sorted[-i-1]*b_sorted[i]


print(total)