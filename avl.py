# class node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#         self.height=1

# # insert the nodes
# def insert(root,data):
#     if not root:
#         return node(data)
#     if data<root.data:
#         root.left=insert(root.left,data)
#     else:
#         root.right=insert(root.right,data)
#     root.height=1+max(ght(root.left),ght(root.right))
#     BF=get_BF(root)

#     # RR rotation
#     if BF>1 and data<root.left.data:
#         return right_rotate(root)
#     # Rl rotation
#     if BF>1 and data>root.left.data:
#         root.left=left_rotate(root.left)
#         return right_rotate(root)
#     # LL rotation
#     if BF<-1 and data>root.right.data:
#         return left_rotate(root)
#     # LR rotation
#     if BF<-1 and data<root.right.data:
#         root.right=right_rotate(root.right)
#         return left_rotate(root)
#     return root

# def left_rotate(a):
#     B=a.right
#     temp=B.left
#     B.left=a
#     a.right=temp

#     a.height=1+max(ght(a.left),ght(a.right))
#     B.height=1+max(ght(B.left),ght(B.right))

#     return B
    
# def right_rotate(a):
#     B=a.left
#     temp=B.right
#     B.right=a
#     a.left=temp

#     a.height=1+max(ght(a.left),ght(a.right))
#     B.height=1+max(ght(B.left),ght(B.right))

#     return B
    
    



# def get_BF(root):
#         if not root:
#             return 0 
#         return ght(root.left)-ght(root.right)
        
# def ght(root):
#     if not root :
#         return 0
#     return root.height
# # print the data in in_order format
# def in_order(root): 
#     if not root:
#         return 
#     in_order(root.left)
#     print(root.data)
#     in_order(root.right)


# root=None
# vl=[19,99,75,7,21,34,38,27,134,100,290,0,12,17,143]
# for i in vl:
#     root=insert(root,i)
# in_order(root)


# n=input()
# count=0
# for i in range(int(n)+1):
#     if len(str(i))<=3:
#         continue
#     elif len(str(i))%3==0:
#         count+=len(str(i))//3-1
#     else:
#         count+=len(str(i))//3
# print(count)

# arr=list(map(int,input().split()))
# for i in arr:
#     if i<=0:
#         arr.remove(i)
# print(arr)       
# print(min(arr))        
# arr=list(map(int,input().split()))
# for i in sorted(arr):
#     if i<=0:
#         arr.pop(0)  
# print(arr)

# def missing_num(nums):
#     maxx=max(nums)
#     res=0
#     for i in range(1,maxx+2):
#         if i not in nums:
#             res=i
#             break
#     return res
# arr=list(map(int,input().split()))
# print(missing_num(arr))


# arr=list(map(int,input().split()))
# arr.sort()
# res=1
# for i in arr:
#     if res==i:
#         res+=1
# print(res)  


# arr=list(map(int,input().split()))
# sums=[]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i!=j:
#             sums.append(sum(arr[i:j]))
# print(max(sums))            


# arr=list(map(int,input().split()))
# maximum=0
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i!=j and sum(arr[i:j])>maximum:
#                 maximum=sum(arr[i:j])
# print(maximum)

arr=list(map(int,input().split()))
current_sum=0
max_sum=0
start=-1
end=-1

for i in range(len(arr)):
    current_sum+=arr[i]
    if max_sum<current_sum:
        max_sum=current_sum
    if current_sum<0:
        current_sum=0
# leetcode 53 