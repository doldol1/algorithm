# map()은 첫번째 인자로 '변환 함수', 두 번째 인자로 iterable을 받는다.
n=list(map(int,input()))

total=0
for i in n:
    # i가 0이라면 continue한다. 엄밀히 따지면 더해야 하겠지만, 
    # 문제에서 요구하는 출력은 결과값 뿐이기 때문에 굳이 자원을 낭비하지 않기 위함
    if i==0:
        continue

    if total==0:
        total+=i
    else:
        if i==1:
            total+=i
        else:
            total*=i

print(total)