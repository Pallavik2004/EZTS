graph=[[0,4,False,False,False,False,False,8,False],
      [4,0,8,False,False,False,False,11,False],
      [False,8,0,7,False,4,False,False,2],
      [False,False,7,0,9,14,False,False,False],
      [False,False,False,9,0,10,False,False,False],
      [False,False,4,14,10,0,2,False,False],
      [False,False,False,False,False,2,0,1,6],
      [8,11,False,False,False,False,1,0,7],
      [False,False,2,False,False,False,6,7,0],
      ]

ls=[0]*len(graph)
dictionary={}
for i in range(len(graph)):
      if i not in dictionary:
            dictionary[i] = float('inf')               
# print(dictionary)
dictionary[0]=0
while len(dictionary)>0:
      minn=min(dictionary.values())
      for k,v in dictionary.items():
            if v==minn:
                  key=k
      
      temp_list=[]
      for val in graph[key]:
            if val!=0 and val!=False:
                  temp_list.append(val)
      for m in temp_list:
            for col in range(len(graph[key])):
                  if graph[key][col]==m and col in dictionary:
                        if dictionary[key]+graph[key][col]<dictionary[col]:
                              dictionary[col]=dictionary[key]+graph[key][col]
      ls[key]=dictionary.pop(key)

print(ls)

