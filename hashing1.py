input_list=[22,10,47,42,56,100,50,92,99,79]

hash_list=[False]*10

for i in input_list:
    h_k=i%10
    if hash_list[h_k]==False:
        hash_list[h_k]=i
    else:
        for j in range(0,len(hash_list)):
            h1_k=(h_k+j)%10
            if hash_list[h1_k]==False:
                hash_list[h1_k]=i
                break
            
print(hash_list)                       
    