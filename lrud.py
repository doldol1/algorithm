n=int(input())
m=input().split()

print(n)
print(m)

dest_dic={'L':(0, -1),
          'R':(0, 1),
          'U':(-1, 0),
          'D':(1, 0),}

piv=[1,1]

for i in m:
    if piv[0]+dest_dic[i][0] < 1 or piv[1]+dest_dic[i][1] < 1:
        continue
    elif piv[0]+dest_dic[i][0] > n or piv[1]+dest_dic[i][1] > n:
        continue
    else:
        piv[0]+=dest_dic[i][0]
        piv[1]+=dest_dic[i][1]

print(piv[0], piv[1])