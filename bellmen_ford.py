adjency_matrix=[[0,6,4,5,False,False],
                 [False,0,False,False,-1,False],
                 [False,-2,0,False,3,False],
                 [False,False,-2,0,False,-1],
                 [False,False,False,False,0,3],
                 [False,False,False,False,False,0]]
dictionary={}
edge_list=[]
for i in range(len(adjency_matrix)):
    if chr(65+i) not in dictionary:
        dictionary[chr(65+i)] =float('inf')
print(dictionary)   

for i in range(len(adjency_matrix)):
    for j in range(len(adjency_matrix)):
        if adjency_matrix[i][j]!=0 and adjency_matrix[i][j]!=False:
            edge_list.append((chr(65+i),chr(65+j)))
# print(edge_list)

dictionary['A']=0

for i in range(len(edge_list)):
    for j in edge_list:
        k,l=j
        if dictionary[k]+adjency_matrix[ord(k)-65][ord(l)-65]<dictionary[l]:
            dictionary[l]=dictionary[k]+adjency_matrix[ord(k)-65][ord(l)-65]
print(dictionary)        

