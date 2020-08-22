m1=[[2,3],
     [4,5],
     [6,7]]
m2=[[3,4,5],[5,6,1]]
for i in range(len(m1)):
    print(m1[i])
for i in range(len(m2)):
    print(m2[i])
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            res[i][j] +=m1[i][k]*m2[k][j]
for i in res:
    print(i)