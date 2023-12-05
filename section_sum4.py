n, m =map(int, input().split(' '))
t_list=[0]+list(map(int, input().split(' ')))

sec_list=list()
for i in range(m):
    sec_list.append(tuple(map(int, input().split(' '))))

######### 입력 테스트 #######33
# print(n, m)
# print(t_list)
# print(sec_list)
#########################3####

sum_list=list()
tmp=0

for i in t_list:
    tmp+=i
    sum_list.append(tmp)

# for i in range(n+1):
    
    # if i==0:
    #     sum_list.append(t_list[i])
    # else:
    #     sum_list.append(t_list[i]+sum_list[i-1])

######### sum_list 테스트 ######
# print(t_list)
# print(sum_list)
################################

for i, j in sec_list:
    total=sum_list[j]-sum_list[i-1]
    print(total)