n=input()

count=0
# 1~9까지는 한 자리 수는 한수가 아니므로 제외
for i in range(10,int(n)+1):
    i_list=list(map(int, str(i)))

    for k in range(len(i_list)):
        if k== len(i_list)-1:
            count+=1
            break
        elif k==0:
            piv= i_list[k+1]-i_list[k]
        else:
            if i_list[k+1]-i_list[k] != piv:
                break

if int(n) < 10:
    count+=int(n)
else:
    count+=9

print(count)

            

