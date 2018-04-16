import Hungarian
"""
with open('Hungarian_6.txt') as f:
    matrix=[]
    for line in f:
        line=line.split()
        line=[i for i in line]
        matrix.append(line)
a=0
b=0
resultmatrix=[[0 for x in range(len(matrix))] for y in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix)+1):
        if j==0:
            continue
        else:
            resultmatrix[a][b]=matrix[i][j]
        b+=1
    a+=1
    b=0
print(resultmatrix) 
111
    
59

18

22

48

74
"""
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
ans = Hungarian.minimize(mat);
best = sum(mat[i][j] for i,j in ans)
print(best)