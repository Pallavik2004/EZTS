def merge_sort(arr):
    if len(arr)>1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]

    # while len(left_arr)>1:
        merge_sort(left_arr)
        merge_sort(right_arr)

        i=0
        j=0
        t=0
        # temp=[0]*len(arr)
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[t]=left_arr[i]
                
                i+=1
            else:
                arr[t]=right_arr[j]
                
                j+=1
            t+=1 
               
        while i<len(left_arr):
            arr[t]=(left_arr[i])
            t+=1
            i+=1
        
        while j<len(right_arr):
            arr[t]=(right_arr[j])
            t+=1
            j+=1 
        
arr=list(map(int,input().split()))
merge_sort(arr)
print(arr)