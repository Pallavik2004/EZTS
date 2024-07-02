'''
q=4
i=3
#code for checking right diagional
for x in zip(range(q-1,-1,-1),range(i-1,-1,-1)):
        print(x)
print("\col\col")
#code for chacking left diagional
for x in zip(range(q-1,-1,-1),range(0,i)):
        print(x)
print("\col\col")
'''
def safe(res,row,col):

        for j in range(col):
                if res[row][j]==1:
                        return False

        for j in range(row):
                if res[j][col]==1:
                        return False
                
        for i,j in zip(range(col,-1,-1),range(row,-1,-1)):  
                if res[j][i]==1:
                        return False

        for i,j in zip(range(col,queens),range(row,-1,-1)):  
                if res[j][i]==1:
                        return False
        return True


def solve_queens(res,col):

    if col>=queens:
        return True
    for row in range(queens):
        
        if safe(res,row,col)==True:
            res[row][col]=1
            if solve_queens(res,col+1)==True:
                   return True
        res[row][col]=0
    return False
                   

queens=4
res=[[0 for i in range(queens)] for j in range(queens)]

if solve_queens(res,0)==False:
       print("No Solution")
for i in range(queens):
       print(res[i])

