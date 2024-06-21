adjency_list={1:[(1,2,0),(1,3,0)],
             2:[(2,1,0),(2,7,0)],
             3:[(3,1,0),(3,5,0),(3,6,0)],
             4:[(4,7,0),(4,8,0)],
             5:[(5,3,0),(5,7,0)],
             6:[(6,3,0),(6,8,0)],
             7:[(7,2,0),(7,5,0),(7,4,0)],
             8:[(8,4,0),(8,6,0)]
             }

visited_list={1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False}
s=[]
E=1

def dfs(adjency_list,visited_list,s,E):
    if visited_list[E]==False:
        s.append(E)
        visited_list[E] = True
    else:
        return
    for i in adjency_list[E]:
        dfs(adjency_list,visited_list,s,i[1])
    print(s.pop())   

# q=[]



def bfs(adjency_list,E):
    q=[E]
    v={}
    for i in adjency_list:
        v[i]=False
    v[E]=True    
    while len(q)!=0:
        curr=q.pop()
        print(curr)
        for i in adjency_list[curr]:
            if v[i[1]]==False:
                q.append(i[1])
                v[i[1]]=True
print("breadth first search")           
bfs(adjency_list,E)
print("-----------------------")
print("depth first search")
dfs(adjency_list,visited_list,s,E)