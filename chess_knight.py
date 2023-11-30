piv=input()

col_dict={'a': 1,
          'b': 2,
          'c': 3,
          'd': 4,
          'e': 5,
          'f': 6,
          'g': 7,
          'h': 8}
x=col_dict[piv[0]]
y=int(piv[1])

mov=((-1, +2),
     (+1, +2),
     (+2, +1),
     (+2, -1),
     (+1, -2),
     (-1, -2),
     (-2, -1),
     (-2, +1))

count=0

for i in mov:
    if x+i[0] < 1 or y+i[1] < 1:
        continue
    elif x+i[0] > 8 or y+i[1] > 8:
        continue
    else:
        count+=1

print(count)