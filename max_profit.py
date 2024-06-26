n=int(input())
fib=[-1]*n
arr=[]
def fabinocii(n):
    for i in range(0,n+1):
        if i <=0:
            arr.append(i)
        else:
            arr.append(arr[i-1]+arr[i-2])
def calc_max(p,w,c,n):
    if n==0 or c==0:
        return 0
    if (w[n-1]>c):
        return calc_max(p,w,c,n-1)
    else:
        return max(p[n-1]+calc_max(p,w,c-w[n-1],n-1),calc_max(p,w,c,n-1))
def calc_max(p,w,c,n):
    if n==0 or c==0:
        return 0
    if dp[n][c]!=-1:
        return dp[n][c]
    if(w[n-1]<=c):
        dp[n][c]=max(p[n-1]+calc_max(p,w,c-w[n-1],n-1),calc_max(p,w,c,n-1))
        return dp[n][c]
    else:
        dp[n][c]=calc_max(p,w,c,n-1)
        return dp[n][c]
        # return max(p[n-1]+calc_max(p,w,c-w[n-1],n-1),calc_max(p,w,c,n-1))
 
p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
c=15
n=len(p)
dp=[[-1 for _ in range(c+1)] for _ in range(n+1) ]
print(calc_max(p,w,c,n))
print(dp)