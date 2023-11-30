n= int(input())

# def sum(start, end):
#     tot=0
#     for i in range(start, end+1): 
#         tot+=i

#     return tot

start=1
end=1
sum_num=1
total=0


while end <= n:
    if sum_num == n:
        total+=1
        sum_num-=start
        start+=1
        

    elif sum_num < n:
        end+=1
        sum_num+=end
    elif sum_num > n:
        sum_num-=start
        start+=1
        

print(total)








# def sum(start, end):
#     tot=0
#     for i in range(start, end-1, -1): # 역순으로 할때 -1을 꼭 해주자
#         # print(i)
#         tot+=i

#     # print(start, end, tot)
#     return tot

# def five_sum(int:n):


#     sub_num=2

#     piv=n//sub_num+sub_num//2

#     total=0

#     while piv-sub_num >= 0:
#         piv_sum=sum(piv, piv-sub_num)

#         if n==piv_sum: #(sum_list[piv]-sum_list[piv-sub_num]):
#             total+=1
#             # print(sub_num, piv)
#             sub_num+=1
#             piv=n//sub_num+sub_num//2
#         elif n< piv_sum: #(sum_list[piv]-sum_list[piv-sub_num+1]):
#             piv-=1
#         elif n> piv_sum: #(sum_list[piv]-sum_list[piv-sub_num+1]):
#             sub_num+=1
#             piv=n//sub_num+sub_num//2
    
#     return total+1

# print(five_sum(n))








# n= int(input())

# def five_sum(int:n):
#     sum_list=[0]
#     tmp_sum=0
#     for i in range(1,n+1):
#         tmp_sum+=i
#         sum_list.append(tmp_sum)
#     # print(sum_list)

#     sub_num=2

#     piv=n//sub_num+sub_num//2

#     total=0

#     while piv-sub_num >= 0:
#         if n==(sum_list[piv]-sum_list[piv-sub_num]):
#             total+=1
#             # print(sub_num, piv)
#             sub_num+=1
#             piv=n//sub_num+sub_num//2
#         elif n< (sum_list[piv]-sum_list[piv-sub_num+1]):
#             piv-=1
#         elif n> (sum_list[piv]-sum_list[piv-sub_num+1]):
#             sub_num+=1
#             piv=n//sub_num+sub_num//2
    
#     return total+1

# print(five_sum(n))