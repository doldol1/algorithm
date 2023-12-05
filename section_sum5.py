n, m = map(int, input().split(' '))

inp_matrix=list()
inp_matrix.append([0]*(n+1))
for i in range(1, n+1):
    inp_matrix.append([0]+list(map(int, input().split(' '))))


sum_matrix=list()
sum_matrix.append([0]*(n+1))
for i in range(1, n+1):
    tmp_line=[0]
    for j in range(1, n+1):
        tmp_line.append(sum_matrix[i-1][j]+sum(inp_matrix[i][:j+1]))
    
    sum_matrix.append(tmp_line)

result=list()
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split(' '))
    result.append(sum_matrix[x2][y2]-sum_matrix[x1-1][y2]-sum_matrix[x2][y1-1]+sum_matrix[x1-1][y1-1])

for i in result:
    print(i)