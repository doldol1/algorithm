n, k= map(int, input().split())

coin_list=list()
for i in range(n):
    coin_list.append(int(input()))

# n=10
# k=4200
# coin_list=[1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

# n=10
# k=4790
# coin_list=[1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

count=0
for j in coin_list[::-1]:
    m=k//j
    if m < 1:
        continue
    else:
        k=k-m*j
        count+=m

print(count)