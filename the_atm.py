n=int(input())
time=list(map(int, input().split(' ')))

time_dict=dict()

for i in range(n):
    time_dict[i]=time[i]

sorted_list=sorted(time_dict.items(), key = lambda item: item[1])

total_time=0
for i in range(n):
    for j in range(i+1):
        total_time+=sorted_list[j][1]

print(total_time)