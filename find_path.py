mapp=[[1,2,2,3],
      [3,1,4,2],
      [1,5,3,3],
      [1,2,1,1]]


dp=[[False]*4,[False]*4,[False]*4,[False]*4]
print(dp)
dp[0][0]=mapp[0][0]

for i in range(1,len(mapp[0])):
    dp[0][i]=dp[0][i-1]+mapp[0][i]
for j in range(1,len(mapp)):
    dp[j][0]=dp[j-1][0]+mapp[j][0]
for i in range(1,len(mapp)):
    for j in range(1,len(mapp)):
        if dp[i-1][j]<dp[i][j-1]:
            dp[i][j]=dp[i-1][j]+mapp[i][j]
        else:
            dp[i][j]=dp[i][j-1]+mapp[i][j]

for i in dp:
    print(i)

