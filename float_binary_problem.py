a=0.3+0.6
if a==0.9:
    print('True: ', a)
else:
    print('False', a)

print('이럴 경우, round()를 사용하여 값을 바꿔준다.')

b=round(0.3+0.6, 1)
if b==0.9:
    print('True: ', b)
else:
    print('False', b)