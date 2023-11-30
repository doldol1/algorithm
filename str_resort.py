st=input()

num=[]
strg=[]

for i in st:
    if i.isdecimal():
        print(f'{i}는 숫자입니다.')
        num.append(int(i))
    else:
        print(f'{i}는 문자입니다.')
        strg.append(i)

fl=sorted(strg)+list(str(sum(num)))
fs=''.join(s for s in fl)
print(fs)