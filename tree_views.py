class node:
     
     def __init__(self,data):
          self.data=data
          self.left=None
          self.right=None
class node_data:
    def __init__(self,node,hkey):
        self.node=node
        self.hkey=hkey


def top_view(root):
    temp=node_data(root,0)
    q=[temp]
    q.append(None)
    key_dict={}
    while len(q)!=0:
        curr=q.pop(0)
        if curr==None:
              if len(q)==0:
                   break
              else:
                   q.append(None)
        else:
             if curr.hkey not in key_dict.keys():
                  key_dict[curr.hkey]=curr.node.data           
            

             if curr.node.left!=None:
               temp=node_data(curr.node.left,curr.hkey-1)
               q.append(temp)
             if curr.node.right!=None:   
               temp=node_data(curr.node.right,curr.hkey+1)
               q.append(temp)
    for i in sorted(key_dict):
        print(key_dict[i])

def bottom_view(root):
     temp=node_data(root,0)
     q=[temp]
     q.append(None)
     key_dict={}
     while len(q)!=0:
          curr=q.pop(0)
          if curr==None:
               if len(q)==0:
                    break
               else:
                    q.append(None)
          else:
               #    if curr.hkey not in key_dict.keys():
               key_dict[curr.hkey]=curr.node.data           
               

               if curr.node.left!=None:
                    temp=node_data(curr.node.left,curr.hkey-1)
                    q.append(temp)
               if curr.node.right!=None:   
                    temp=node_data(curr.node.right,curr.hkey+1)
                    q.append(temp)
     for i in sorted(key_dict):
          print(key_dict[i])
def left_view(root):
     q=[root,None]
     print(root.data)
     while len(q)>0:
          c=q.pop(0)
          if c==None:
               # print(root.data)
               if len(q)==0:
                    break
               else:
                    # print(root.data)
                    print(q[0].data)
                    q.append(None)
          else:
               # print(c.data,end=" ")
               if c.left !=None:
                    q.append(c.left)
               if c.right!=None:
                    q.append(c.right)     

def right_view(root):
     q=[root,None]
     print(root.data)
     while len(q)>0:
          c=q.pop(0)
          if c==None:
               # print(root.data)
               if len(q)==0:
                    break
               else:
                    # print(root.data)
                    print(q[-1].data)
                    q.append(None)

          else:
               # print(c.data,end=" ")

               if c.left !=None:
                    q.append(c.left)
               if c.right!=None:
                    q.append(c.right) 

if __name__=='__main__':
          root=node(1)

          root.left=node(2)
          root.right=node(5)

          root.left.left=node(3)
          root.left.right=node(4)

          # root.right.left=node(6)
          root.right.right=node(6)

          root.left.right.left=node(9)
          # root.left.right.left.right=node(10)

          root.right.right.right=node(8)
          root.right.right.left=node(7)
          root.right.right.left.right=node(11)
          root.right.right.left.right.left=node(12)
          root.right.right.left.right.left.right=node(13)
          # root.left.right.left.left=node()
          
          root.left.right.left.right=node(10)
          root.left.right.left.right.left=node(14)
          top_view(root)
          print("-----------------")
          bottom_view(root)
          print("-----------------")
          right_view(root)
          print("-----------------")
          left_view(root)