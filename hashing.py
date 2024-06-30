class node:
    def __init__(self,data):
        self.data=data
        self.next=None



input_list=[10,16,62,100,20,86,72,7,76,99]
head_list=[None]*10
for i in input_list:
    reminder=i%10
    if  head_list[reminder]==None:
        
        head_list[reminder]=node(i)
        
    else:
        
        head=head_list[reminder]
        while head.next:
            head=head.next
        head.next=node(i)
                
for i in head_list:
    if i!=None:
        print(i.data,end=" ")
        while i.next:
            i=i.next
            print(i.data,end=" ")
            
        print()


