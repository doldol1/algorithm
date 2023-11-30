n=int(input())
m=int(input())
part_list=list(map(int, input().split()))

########### preset ##############
# n=6
# m=9
# part_list=[2, 7, 4, 1, 5, 3]

########### input test ##########
# print(n)
# print(m)
# print(part_list)


# init
part_list=sorted(part_list)
start=0
end=n-1
sum_p=0
count=0

while start < end:
    sum_p=part_list[start]+part_list[end]
    if sum_p==m:
        count+=1
        start+=1
        end-=1        
    elif sum_p < m:
        start+=1
    elif sum_p > m:
        end-=1
print(count)