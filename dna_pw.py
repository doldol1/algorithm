s, p= map(int, input().split(' '))
st_list=list(input())
a_lim, c_lim, g_lim, t_lim=map(int, input().split(' '))

########## PRESET ####
# s, p= 9, 8
# st_list=['C', 'C', 'T', 'G', 'G', 'A', 'T', 'T', 'G']
# a_lim, c_lim, g_lim, t_lim= 2, 0, 1, 1

# s, p= 4, 2
# st_list=['G', 'A', 'T', 'A']
# a_lim, c_lim, g_lim, t_lim= 1, 0, 0, 1

####### input test ########
# print(s, p)
# print(st_list)
# print(a_lim, c_lim, g_lim, t_lim)
#############

st_pw=0
ed_pw=p

can_list=st_list[st_pw:ed_pw]

a_c=can_list.count('A')
c_c=can_list.count('C')
g_c=can_list.count('G')
t_c=can_list.count('T')
count=0

while(ed_pw <= s):

    if a_c>= a_lim \
            and c_c>= c_lim \
            and g_c>= g_lim \
            and t_c>= t_lim:
        count+=1
    # can_list=st_list[st_pw:ed_pw]

    # if can_list.count('A')>= a_lim \
    #     or can_list.count('C')>= c_lim \
    #     or can_list.count('G')>= g_lim \
    #     or can_list.count('T')>= t_lim:
    #     count+=1
    

    # a_c, c_c, g_c, t_c= 0, 0, 0, 0
    # for i in can_list:
    #     if i=='A':
    #         a_c+=1
    #     elif i=='C':
    #         c_c+=1
    #     elif i=='G':
    #         g_c+=1
    #     elif i=='T':
    #         t_c+=1
        
    #     if a_c>= a_lim \
    #         and c_c>= c_lim \
    #         and g_c>= g_lim \
    #         and t_c>= t_lim:
    #         count+=1
    #         break
    if ed_pw>=s:
        break

    if st_list[st_pw]=='A':
        a_c-=1
    elif st_list[st_pw]=='C':
        c_c-=1
    elif st_list[st_pw]=='G':
        g_c-=1
    elif st_list[st_pw]=='T':
        t_c-=1
    st_pw+=1

    if st_list[ed_pw]=='A':
        a_c+=1
    elif st_list[ed_pw]=='C':
        c_c+=1
    elif st_list[ed_pw]=='G':
        g_c+=1
    elif st_list[ed_pw]=='T':
        t_c+=1
    ed_pw+=1



print(count)

