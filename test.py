class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None

class LinkedList:
  def __init__(self):
    self.head = None
  def convert_node(self,arr):
    head=Node(arr[0])
    temp=head
    for i in range(1,len(arr)):
      new_node=Node(arr[i])
      temp.next=new_node
      temp=temp.next
    return head
  
  def merge(self,l2):
    pass
  def insert_node(head,k,val):
    if head==None and head.next==None:
      return head
    temp=head
    if k==1:
      new_node=Node(val)
      head=new_node
      head.next=temp
      return head
    prev=None
    cnt=1
    while temp:
      if k==cnt:
        prev.next=Node(val)
        prev.next.next=temp
      prev=temp
      temp=temp.next
      cnt+=1
    return head 

  def merge_list(lis1,lis2):
    if lis1==None and lis2==None:
      return None
    elif lis1==None:
      return lis2
    elif lis2==None:
      return lis1
    dummy=Node(-1)
    l1,l2=lis1,lis2
    mover=dummy
    while l1 and l2:
      while l1 and l2 and l1.data<=l2.data:
        mover.next=l1
        l1=l1.next
        mover=mover.next
      while l2 and l1 and l2.data<l1.data:
        mover.next=l2
        l2=l2.next
        mover=mover.next
    if l1:
      mover.next=l1
      mover=mover.next
    elif l2:
      mover.next=l2
      mover=mover.next
    return dummy.next

  def detect_cycle(head):
    set1=set()
    temp=head
    while temp:
      if temp not in set1:
        set1.add(temp)
        temp=temp.next
      else:
        return True
    return False
  
  def middle_element(head):
    temp=head
    slow=temp
    fast=temp
    while fast and fast.next:
      fast=fast.next.next
      slow=slow.next
    return slow

  def reverse_list(head):
    if head is None or head.next is None:
      return head
    temp=None
    p=head
    q=head
    # cnt=0
    while q.next:
      q=q.next
      p.next=temp
      temp=p
      p=q
      # print(p.data)
    p.next=temp
    return p

  def reverse_list_recursion(head):
    oldhead=head
    reshead=head
    detach=None

    # while reshead.next!=None:
    #   reshead=oldhead.next
    #   oldhead.next=detach
    #   detach=oldhead
    #   oldhead=reshead
    # reshead.next=detach

    def reverse_rec(oldhead,reshead,detach):
      if reshead.next==None:
        reshead.next=detach
        return reshead
      reshead=oldhead.next
      oldhead.next=detach
      detach=oldhead
      oldhead=reshead
      return reverse_rec(oldhead,reshead,detach)
  
    return reverse_rec(oldhead,reshead,detach)
  
  def detect_cycle_dummy(head):
    dummy=Node(-1)
    mover=head
    while mover:
      if mover.next==dummy:
        return True
      temp=mover.next
      mover.next=dummy
      mover=temp
    return False

  def intersection_of_list(l1,l2):
    visited=set()
    l1_mover=l1
    l2_mover=l2
    while l1_mover:
      visited.add(l1_mover)
      l1_mover=l1_mover.next
    while l2_mover:
      if l2_mover in visited:
        return l2_mover
      visited.add(l2_mover)
      l2_mover=l2_mover.next
    return None

class DoublyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  
  def print_list(self):
    temp=self.head
    while temp:
      prev=temp.prev.data if temp.prev else "None"
      next=temp.next.data if temp.next else "None"
      print(prev,temp.data,next)
      temp=temp.next
    return

  def print(head):
    temp=head
    while temp:
      prev=temp.prev.data if temp.prev else "None"
      next=temp.next.data if temp.next else "None"
      print(prev,temp.data,next)
      temp=temp.next

  def append_node(self,node):
    if self.head==None:
      self.head=node
      self.head.next=None
      return
    temp=self.head
    while temp.next:
      temp=temp.next
    temp.next=node

  def append(self,data):
    new_node=Node(data)
    if self.head==None:
      self.head=new_node
      self.tail=new_node
      return
    temp=self.head
    while temp.next:
      temp=temp.next
    temp.next=new_node
    new_node.prev=temp
    self.tail=new_node
  
  def intersection(self,list2):
    visited=set()
    l1=self.head
    l2=list2.head
    while l1:
      visited.add(l1)
      l1=l1.next
    while l2:
      if l2 in visited:
        return True
      visited.add(l2)
      l2=l2.next
    return False

  def intersection_pointers(self,list2):
    pointerA=self.head
    flag1,flag2=1,1
    pointerB=list2.head
    while pointerA!=pointerB and flag1 and flag2:
      if pointerA.next==None:
        pointerA.next=list2.head
        flag1=flag1-1
      else:
        pointerA=pointerA.next
      if pointerB.next==None:
        pointerB.next=self.head
        flag2=flag2-1
      else:
        pointerB=pointerB.next
    return pointerA.data if not flag1 and flag2 else None

  def middle_element(self):
    # head=self.head
    # tail=self.tail
    # i=head
    # j=tail
    # while i!=j:
    #   i=i.next
    #   j=j.prev
    # return i.data
    slow=self.tail
    fast=self.tail
    while fast.prev and fast.prev.prev:
      slow=slow.prev
      fast=fast.prev.prev
      # print(slow.data,fast.data)
    return slow.data

  def reverse(self):
    curr=self.head
    temp=None
    while curr:
      temp=curr.prev
      curr.prev=curr.next
      curr.next=temp
      curr=curr.prev
    return temp.prev

  def deep_copy(self):
    head=self.head
    temp=head
    while temp:
      new_node=Node(temp.data)
      new_node.prev=temp
      new_node.next=temp.next
      temp.next=new_node
      temp=temp.next.next
      if temp:
        temp.prev=new_node
    temp=head
    dummy=Node(None)
    mover=dummy
    while temp:
      mover.next=temp.next
      temp.next.prev=mover
      mover=mover.next
      temp=temp.next.next
    DoublyLinkedList.print(dummy.next)
    return dummy.next
  
class CircularLinkedList:
  def __init__(self):
    self.head=None
    # self.tail=self.head
  def append(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
      self.head.next=new_node
      self.tail=new_node
      return
    temp=self.head
    while temp.next and temp.next!=self.head:
      temp=temp.next
    temp.next=new_node
    new_node.prev=temp
    new_node.next=self.head
    return self.head
  
  def middle_element(self):
    slow=self.head
    fast=self.head
    flag=1
    while (fast!=self.head and fast.next!=self.head) or flag:
      if flag:
        flag=0
      slow=slow.next
      fast=fast.next.next
    return slow.data

  def count(self):
    cnt=1
    if self.head is None:
      return 0
    # elif self.head.next is self.head:
    #   return 1
    temp=self.head.next
    while temp:
      if temp==self.head:
        return cnt
      temp=temp.next
      cnt+=1

class Stack:
  def __init__(self):
    self.top=None
    self.size=0
  def push(self,val):
    new_node=Node(val)
    if self.top is None:
      self.top=new_node
      return
    new_node.next=self.top
    self.top=new_node
    return
  
  def pop(self):
    self.top=self.top.next
    return
  
  def get_top(self):
    return self.top.data

class Queue:
  def __init__(self):
    self.start=None
    self.end=None
  
  def push(self,val):
    new_node=Node(val)
    if self.start is None and self.end is None:
      self.start=new_node
      self.end=new_node
      return
    self.end.next=new_node
    self.end=new_node
    return

  def pop(self):
    temp=self.start
    self.start=self.start.next
    temp.next=None

  def get_top(self):
    return self.start.data

class Stack_Array:
  def __init__(self,size):
    self.size=0
    self.stack=[None]*size
    self.top=None
  def push(self,val):
    self.size+=1
    if self.size>len(self.stack):
      self.size-=1
      print("Cant add More")
      return None
    if self.top is None:
      self.top=0
    else:
      self.top=self.top+1
    self.stack[self.top]=val
    return
  
  def pop(self):
    if self.top==None:
      print("No more element to delete")
      return None
    self.stack[self.top]=None
    self.top-=1
    self.size-=1

  def get_top(self):
    if self.top==None:
      print("Not registered")
      return None
    return self.stack[self.top]

class Queue_Array:
  def __init__(self,size):
    self.size=0
    self.start=None
    self.end=None
    self.Queue=[None]*size
  def push(self,val):
    self.size+=1
    if self.size>len(self.Queue):
      print("Memory Limit Hit")
      self.size-=1
      return
    if self.end is None:
      self.start=self.end=0
    else:
      self.end=(self.end+1)%self.size
    self.Queue[self.end]=val

  def pop(self):
    if self.start is None:
      print("No elements to pop")
      return
    self.Queue[self.start]=None
    self.start=(self.start+1)%self.size
    self.size-=1
  def get_top(self):
    return self.Queue[self.start]

class Stack_conversions:
  def priority(char):
    if chr=='^':
      return 3
    elif chr=='/' or chr=='*':
      return 2
    elif chr=='+' or chr=='-':
      return 1
    else:
      return 0

  def infix_to_postfix(quest):
    st=Stack_Array(len(quest))
    res=''
    i=0
    while i<len(quest):
      if (quest[i]>='a' and quest[i]<='z') or (quest[i]>='A' and quest[i]<='Z'):
        res=res+quest[i]
      elif quest[i]=='(':
        st.push(quest[i])
      elif quest[i]==')':
        while st.get_top() and st.get_top()!='(':
          res=res+st.get_top()
          st.pop()
        if st.get_top():
          st.pop()
      else:
        while st.get_top()!=None and st.get_top()!='(' and Stack_conversions.priority(quest[i])>=Stack_conversions.priority(st.get_top()):
          res=res+st.get_top()
          st.pop()
        st.push(quest[i])
      i+=1
    while st.get_top()!=None:
      res+=st.get_top()
      st.pop()
    return res

class StackNode:
  def __init__(self,data):
    self.data=data
    self.next=None

class Stack_new:
  def __init__(self):
    self.top=None
    self.size=None
  
  def get_size(self):
    return self.size
  
  def push(self,data):
    new_node=StackNode(data)
    if self.top is None:
      self.top=new_node
      return
    new_node.next=self.top
    self.top=new_node

  def pop(self):
    if self.top is None:
      print("No element to pop")
      return
    # temp=self.top
    self.top=self.top.next
    # temp.next=None
    return
  def get_top(self):
    if self.top is None:
      return None
    return self.top.data

class TreeNode:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
  def assign_values(root,node):
    if root is None:
      return False
    if root.left is None:
      root.left=node
      return True
    elif root.right is None:
      root.right=node
      return True
    else:
      return TreeNode.assign_values(root.left,node) or TreeNode.assign_values(root.right,node)
  def assign_values_bst(root,node):
    if root is None:
      return False
    if root.left is None and node.data<root.data:
      root.left=node
      return True
    elif root.right is None and node.data>root.data:
      root.right=node
      return True
    else:
      return TreeNode.assign_values_bst(root.left,node) | TreeNode.assign_values_bst(root.right,node)
  def print_tree(root):
    if root is None:
      return
    print(root.data)
    TreeNode.print_tree(root.left)
    TreeNode.print_tree(root.right)
  def level_order_traversal(node,level):
    if node==None:
      return
      # res.append([])
    if len(res)-1!=level:
      res.append([])
    res[level].append(node.data)
    # if len(res)==le
    TreeNode.level_order_traversal(node.left,level+1)
    TreeNode.level_order_traversal(node.right,level+1)
    return res
  def level_order_traversal_queue(node):
    if node is None:
      return
    res=[]
    queue=[node]
    while queue:
      temp=[]
      for i in range(len(queue)):
        n=queue.pop(0)
        if n is None:
          return res
        if n.left:
          queue.append(n.left)
        if n.right:
          queue.append(n.right)
        temp.append(n.data)
      res.append(temp)
    return res
  def left_view(node,level):
    if node is None:
      return
    if len(res)==level:
      res.append(node.data)
    TreeNode.left_view(node.left,level+1)
    TreeNode.left_view(node.right,level+1)
    return res
  def top_view(node,vertical_level,dic):
    if node is None:
      return
    if vertical_level not in dic:
      dic[vertical_level]=node.data
    TreeNode.top_view(node.left,vertical_level-1,dic)
    TreeNode.top_view(node.right,vertical_level+1,dic)
    return dic
  def bottom_view(node,vertical_level,dic):
    if node is None:
      return
    dic[vertical_level]=node.data
    TreeNode.bottom_view(node.left,vertical_level-1,dic)
    TreeNode.bottom_view(node.right,vertical_level+1,dic)
    return dic
  def lowest_common_anscestor(node,p,q):
    if node is None:
      return
    if node==p or node==q:
      return node
    left=TreeNode.lowest_common_anscestor(node.left,p,q)
    right=TreeNode.lowest_common_anscestor(node.right,p,q)
    if left!=None and right!=None:
      return node
    return left or right
# n=int(input())
# root=None
# while n>0:
#   if root is None:
#     root=TreeNode(int(input()))
#   else:
#     node=TreeNode(int(input()))
#     TreeNode.assign_values(root,node)
#   n-=1
# # TreeNode.print_tree(root)
# # print(TreeNode.level_order_traversal(root,0))
# dic=TreeNode.bottom_view(root,0,{})
# dic=dict(sorted(dic.items()))
# print(list(dic.values()))
# # print(TreeNode.left_view(root,0))

class Sathish_Sir_Probelms:
  class Knight_min_problem:
    # A Chessboard has always a 8*8 grid , and a knight can only possibly move 8 moves from a pos
    # So imagine the chessbaord like a 2*2 matrix and start working
    class Cell:
      def __init__(self,x,y,moves):
        self.x=x
        self.y=y
        self.moves=moves

    def check_boundary(self,x,y):
      # return True
      return True if 0<=x<8 and 0<=y<8 else False
    
    def knight_min_bfs(self,knight_pos,target_pos):
      dx=[-1,-1,1,1,2,2,-2,-2]
      dy=[-2,2,2,-2,1,-1,1,-1]
      queue=[]
      visited = [[False]*8 for _ in range(8)]
      # visited = [[False]*8]*8 
      # This Wont work because it creates shallow copy
      print(visited)
      queue.append(self.Cell(knight_pos[0],knight_pos[1],0))
      visited[knight_pos[0]][knight_pos[1]]=True
      while queue:
        k=queue.pop(0)
        if k.x==target_pos[0] and k.y==target_pos[1]:
          return k.moves
        for i in range(8):
          x=k.x+dx[i]
          y=k.y+dy[i]

          if Sathish_Sir_Probelms.Knight_min_problem.check_boundary(self,x,y) and not visited[x][y]:
            print(x,y)
            visited[x][y]=True
            queue.append(self.Cell(x,y,k.moves+1))
      return -1
    

    min_steps=float('inf')
    '''DFS'''
    def knight_min_dfs(self,knight_pos,target_pos,steps,visited):
      dx=[-1,-1,1,1,2,2,-2,-2]
      dy=[-2,2,2,-2,1,-1,1,-1]
      x=knight_pos[0]
      y=knight_pos[1]
      if x==target_pos[0] and y==target_pos[1]:
        Sathish_Sir_Probelms.Knight_min_problem.min_steps=min(Sathish_Sir_Probelms.Knight_min_problem.min_steps,steps)
        return
      if steps>Sathish_Sir_Probelms.Knight_min_problem.min_steps:
        return
      for i in range(8):
        cx=x+dx[i]
        cy=y+dy[i]
        print(cx,cy)
        if Sathish_Sir_Probelms.Knight_min_problem.check_boundary(self,cx,cy) and not visited[cx][cy]:
          visited[cx][cy]=True
          Sathish_Sir_Probelms.Knight_min_problem.knight_min_dfs(self,(cx,cy),target_pos,steps+1,visited)
          visited[cx][cy]=False
      return -1

out1=Sathish_Sir_Probelms.Knight_min_problem()
visited = [[False]*8 for _ in range(8)]
knight_pos=(0,0)
visited[knight_pos[0]][knight_pos[1]]=True
out1.knight_min_dfs(knight_pos,(2,1),0,visited)
print(Sathish_Sir_Probelms.Knight_min_problem.min_steps)

# Note: Important Concept
# visited=[[1]*4]*4
# visited[0][0]=0
# print(visited)
# visited=[[1]*4 for _ in range(4)]
# visited[0][0]=0
# print(visited)