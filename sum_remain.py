n, m = map(int, input().split(' '))
t_list=list(map(int, input().split(' ')))

tmp=0
s_list=list()

for i in t_list:
    s_list.append(i+tmp)
    tmp=i+tmp

count_list=[0]*m
count=0

for i in s_list:
    rem=i%m
    if rem==0:
        count+=1
    count_list[rem]+=1

for i in range(m):
    if count_list[i] > 1:
        count+=(count_list[i]*(count_list[i]-1) // 2)
print(count)