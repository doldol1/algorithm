n, m=map(int, input().split(' '))
j=int(input())

apples=list()

for i in range(j):
    apples.append(int(input()))

### 입력 preset
# n, m= 5, 1
# j=3
# apples=[1,5,3]

# n, m= 5, 2
# j=3
# apples=[1,5,3]

##############입력테스트#############
# print(n, m)
# print(j)

# for i in apples:
#     print(i)
####################################

basket=[0,m-1]
move=0
diff=0
tot=0

for i in apples:
    t_a=i-1
    if basket[0]<=t_a and basket[1]>=t_a:
        continue
    elif basket[0]> t_a:
        diff=basket[0]-t_a
        basket[0]=t_a
        basket[1]=basket[1]-diff
        tot+=diff
    elif basket[1]< t_a:
        diff=t_a-basket[1]
        basket[1]=t_a
        basket[0]=basket[0]+diff
        tot+=diff

print(tot)