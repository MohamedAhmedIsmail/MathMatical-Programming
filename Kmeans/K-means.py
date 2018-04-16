import numpy as np
import math
f = open("C:\\Users\\mohamed ismail\\Desktop\\K_Means0022.txt")
k = int(f.readline())
content = f.readlines()
num = []
mean = []
for line in content:
    l = line.split(' ')
    a , x , y = int(l[0]) , int(l[1]) , int(l[2])
    num.append((a  , x , y))
dist=np.zeros((k,len(num)))
cnt=np.zeros(1002)
meantemp= []
c = 0
for i in range(k):
    mean.append([num[i][0] , num[i][1] , num[i][2]])
    meantemp.append([0,0,0])
while True:
    mn=100000
    clnum = -1
    outClusters = []
    sums = []
    for i in range(k):
        outClusters.append([])
        sums.append([0,0])
    c=0
    for i in range(k):
        for j in range(len(num)):
            dist[i][j] = math.sqrt(((mean[i][1]-num[j][1]) ** 2 ) + ((mean[i][2]-num[j][2])** 2 ))
            
            #dist[i][j]=(abs(((mean[i][1]-num[j][1])**k))+abs(((mean[i][2]-num[j][2])**k))**(1/k))

    for i in range(k):
        cnt[i]=0

    for j in range(len(num)):
        for i in range(k):
            if dist[i][j] < mn:
                mn=dist[i][j]
                clnum=i
        sums[clnum][0]+=num[j][1]
        sums[clnum][1]+=num[j][2]
        
        cnt[clnum]+=1
        outClusters[clnum].append(num[j])
        mn=100000        
        clnum=-1
        
    for i in range(k):
        meantemp[i][1]=sums[i][0]/cnt[i]
        meantemp[i][2]=sums[i][1]/cnt[i]
        
    for i in range(k):
        if int(mean[i][1])==int(meantemp[i][1]) and int(mean[i][2])==int(meantemp[i][2]):
            c+=1
    if c==k:
        break
    else:
        for i in range(k):
            mean[i][2] = meantemp[i][2]
            mean[i][1] = meantemp[i][1]
print(dist)
for i in range(k):
    print("cluster " , i  + 1)
    for j in range(len(outClusters[i])):
        print(outClusters[i][j][0] , " " , outClusters[i][j][1] , " " , outClusters[i][j][2] )
    print("==========================")