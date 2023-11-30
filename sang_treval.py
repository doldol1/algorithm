############# 입력 ##########
the_case= int(input())
t=the_case

case_list=list()
while t!=0:
    n, m= map(int, input().split())
    flight_list=list()
    for _ in range(m):
        flight_list.append(list(map(int, input().split(' '))))
    case_list.append(flight_list)
    t-=1


total_result=list()

for i in range(the_case):
    