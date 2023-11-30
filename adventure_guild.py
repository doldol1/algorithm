n=map(int, input().split(' '))
n_s=sorted(n)

team=0
start=0
end=0
while end < len(n_s):
    std=n_s[end]

    if (end+1-start) == std:
        team+=1
        start=end+1
        end=start
    else:
        end+=1

print(team)
# 만약 2 2 2 3 3이라면
'''
1회차
start=0, end=1, team=0
2회차
start=2, end=2, team=1
3회차
start=2, end=3, team=1
4회차
start=2, end=4, team=1
5회차
start=4
'''