# baekjoon 1253
# input
n=int(input())

a=list(map(int,input().split(' ')))

# preset
# n=10

# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# input test
# print(n)
# print(' '.join(map(str,a)))

# sort
a=[None]+sorted(a)
# sort test
# print(' '.join(map(str,a)))



count_good=0

for i in range(n+1)[n:0:-1]:
    start=1
    end=n
    while start < end:
        if start==i:
            start+=1
        if end==i:
            end-=1
        if start >= end:
            break
        mea=a[start]+a[end]


        if mea == a[i]:
            count_good+=1
            break
        elif mea > a[i]:
            end-=1
        elif mea < a[i]:
            start+=1


print(count_good)
        