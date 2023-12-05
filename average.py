n=int(input())
t_list=list(map(int,input().split()))

######### 입력 테스트 ########3
# print(n)
# print(t_list)
##########################

m=max(t_list)

for i in range(n):
    t_list[i]=t_list[i]/m*100

print(round(sum(t_list)/n, 2))