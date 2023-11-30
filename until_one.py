import time

n, k= map(int, input().split())

start_time=time.time() # 측정 시작

count= 0

while (n!=1):

    if n%k==0:
        n= n//k
        count+=1
    else:
        n-=1
        count+=1

print(count)

end_time= time.time() # 측정 종료
print("time:", end_time-start_time) # 수행 시간 출력