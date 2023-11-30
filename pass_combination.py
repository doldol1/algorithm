from itertools import combinations

l, c= map(int, input().split())
a_list=list(input().split(' '))

# l, c= 4, 6
# a_list=['a', 't', 'c', 'i', 's', 'w']

combi_list=combinations(a_list, l)

s_list=list()

type_a=['a', 'e', 'i', 'o', 'u']

for combi in combi_list:
    sort_combi=sorted(combi)
    mom=0
    son=0
    for mes in sort_combi:
        if mes in type_a:
            mom+=1
        else:
            son+=1
    
    if mom > 0 and son > 1:
        s_list.append(sort_combi)
    else:
        continue

s_list=sorted(s_list)

for i in s_list:
    print(''.join(i))