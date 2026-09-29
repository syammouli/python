#trees
# level order traversal

import collections
from collections import deque,defaultdict

# class Node:
#     def __init__(self, val):
#         self.val = val 
#         self.left = None
#         self.right = None


# def build_tree(arr):
#     if not arr:
#         return None
    
#     root = Node(arr[0])
#     queue = deque([root])
#     i = 1

#     while queue and i < len(arr):
#         curr = queue.popleft()

#         if i < len(arr) and arr[i] is not None:
#             curr.left = Node(arr[i])
#             queue.append(curr.left)
#         i += 1

#         if i < len(arr) and arr[i] is not None:
#             curr.right = Node(arr[i])
#             queue.append(curr.right)
#         i += 1

#     return root


# def levelOrder(root):
#     if not root:
#         return []
    
#     queue = collections.deque([root])
#     result = []

#     while queue:
#         level_size = len(queue)
#         current_level = []

#         for _ in range(level_size):
#             node = queue.popleft()
#             current_level.append(node.val)

#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)

#         result.append(current_level)

#     return result


# arr = [1, 2, 3, 4, 5, None, 6]
# root = build_tree(arr)

# print("level order", levelOrder(root))


class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

root=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)


root.left=node2
root.right=node3
node2.left=node4
node2.right=node5


def printNodes(node):
    if not node:
        return
    print(node.val)

    if node.left:
        print("left node value-->",node.left.val)
    else:
        print("left node value--> None")
    if node.right:
        print("right node value-->",node.right.val)
    else:
        print("right node value--> None")   

    printNodes(node.left)
    printNodes(node.right)



printNodes(root)

print(root.val)
def levelOrder(root):
    if not root:
        return
    
    queue=deque([root])
    result=[]

    while queue:
        node=queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

print("level order cehck",levelOrder(root))
#recursive inorder
def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

inorder(root)

#iterative inorder
def iterativeInorder(root):

    stack=[]
    result=[]
    current=root

    while current or stack:
        while current:
            stack.append(current)
            current=current.left

        current=stack.pop()
        result.append(current.val)

        current=current.right

    return result
    
print("iterative inorder")
print(iterativeInorder(root))


#recursive preorder
def preOrder(root):
    if not root:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)
print("preOrder")
preOrder(root)

#iterative preorder
def iterativePreorder(root):
    if not root:
        return []
    stack=[root]
    res=[]
    while stack:
        node=stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)  #to push the elements to left so next elements will be popped on top

        if node.left:
            stack.append(node.left)
    return res
print("itereative preorder")
print(iterativePreorder(root))


#iterative postorder
def iterativePostorder(root):
    stack=[]
    result=[]
    current=root
    while current or stack:
        if current:
            stack.append(current)
            result.append(current.val)
            current=current.right

        else:
            current=stack.pop()
            current=current.left

    return result[::-1]
print("iterative postorder")
print(iterativePostorder(root))

def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)

print("postorder")
postOrder(root)


def all_order_once(root):
    if not root:
        return
    preorder=[]
    postorder=[]
    inorder=[]

    stack=[(root,1)]
    while stack:
        node,state=stack.pop()
        if state==1:            
            preorder.append(node.val)
            stack.append((node,2))
            if node.left:
                stack.append((node.left,1))

        elif state==2:
            inorder.append(node.val)
            stack.append((node,3))
            if node.right:
                stack.append((node.right,1))

        else:
            postorder.append(node.val)

    return preorder,inorder,postorder
print("printing all orders in one code")
print(all_order_once(root))

#max depth of a binary tree
def maxDepth(root):
    if not root:
        return 0
    
    return 1+ max(maxDepth(root.left),maxDepth(root.right))

print("maximm",maxDepth(root))

#check if tree is balanced or not

def isBalanced(root):
    def dfs(root):
        if not root:
            return 0
        left=dfs(root.left)
        if left==-1:
            return -1
        right =dfs(root.right)
        if right==-1:
            return -1        
        if abs(left-right)>1:
            return -1
        return 1+max(left,right)
    return dfs(root)!=-1

print("if tree is balanced")
print(isBalanced(root))
 

def searchInTree(root,target):
    if not root:
        return False
    if root.val==target:
        return True
    return searchInTree(root.left,target) or searchInTree(root.right,target)

   

print(searchInTree(root,8))


#diameter of a tree
def diameter(root):
    dia=0
    def dfs(root):
        nonlocal dia
        if not root:
            return 0
        left = dfs(root.left)
        right= dfs(root.right)

        dia= max(dia,left+right)

        return 1+max(left,right)
    dfs(root)
    return dia

print(diameter(root))


#maximum path sum in a treee
#         -10
#         /  \
#        9   20
#           /  \
#          15   7

# Answer: 42  (15 + 20 + 7)
print("mmmmmmmmmm")

def maxpathsum(root):
    maximum=float('-inf')
    def dfs(root):
        nonlocal maximum
        if not root:
            return 0
        left=max(dfs(root.left),0)
        right=max(dfs(root.right),0)
        current=root.val+left+right
        maximum=max(maximum,current)
        return root.val+max(left,right)
    dfs(root)
    return maximum
print(maxpathsum(root))


# def isSameTree(p, q):
#     # case 1: both are None
#     if not p and not q:
#         return True

#     # case 2: one is None
#     if not p or not q:
#         return False

#     # case 3: values different
#     if p.val != q.val:
#         return False

#     # case 4: check left and right
#     return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def zigzagOrder(root):
    queue=deque([root])
    result=[]
    left_to_right=True
    while queue:
        level_size=len(queue)
        level=deque()

        for _ in range(level_size):
            node=queue.popleft()

            if left_to_right:
                level.append(node.val)

            else:
                level.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(level))
        left_to_right= not left_to_right
    return result

print(zigzagOrder(root))

#boundary traversal of leaf

def boundaryTraversal(root):
    if not root:
        return []
    result=[]

    def is_leaf(root):
        return not root.left and not root.right
    
    if not is_leaf(root):
        result.append(root.val)

    def add_left_nodes(root):
        current=root.left
        while current:
            if not is_leaf(current):
                result.append(current.val)

            if root.left:
                current=current.left

            else:
                current=current.right

    def add_leaves(root):
        if is_leaf(root):
            result.append(root.val)
            return
        if root.left:
            add_leaves(root.left)
        if root.right:
            add_leaves(root.right)

    def add_right_nodes(root):
        current=root.right
        temp=[]
        while current:
            if not is_leaf(current):
                 temp.append(current.val)
            if current.right:
                current=current.right

            else:
                current=current.left
        result.extend(temp[::-1])
    add_left_nodes(root)
    add_leaves(root)
    add_right_nodes(root)

    return result
print("boundaries")
print(boundaryTraversal(root))


#vertical traversal

def verticalTraversal(root):
    if not root:
        return []
    col_map=defaultdict(list)
    queue=deque([(root,0,0)])
    while queue:
        node,row,col=queue.pop()
        col_map[col].append((row,node.val))

        if node.left:
            queue.append((node.left,row+1,col-1))
        if node.right:
            queue.append((node.right,row+1,col+1))

        result=[]
        for col in sorted(col_map.keys()):
            col_nodes=sorted(col_map[col],key=lambda x:(x[0],x[1]))

            result.append([val for row,val in col_nodes])
    return result
print(verticalTraversal(root))


#top view in a tree

def topView(root):
    if not root:
        return
    dic={}
    queue=deque([(root,0)])
    while queue:
        node,col=queue.popleft()
        if col not in dic:
            dic[col]=node.val

        if node.left:
            queue.append((node.left,col-1))
        if node.right:
            queue.append((node.right,col+1))

    result=[]
    for ind in sorted(dic.keys()):
        result.append(dic[ind])
    return result

print(topView(root))


#bottom view 

def bottomView(root):
    if not root:
        return
    
    dic={}
    queue=deque([(root,0)])

    while queue:
        node,col=queue.popleft()

        #here we are replacing the value with latest
        dic[col]=node.val

        if node.left:
            queue.append((node.left,col-1))

        if node.right:
            queue.append((node.right,col+1))

        
    result=[]
    for ind in sorted(dic.keys()):
        result.append(dic[ind])
    return result

print("above is top view, below is bottom view of tree")
print(bottomView(root))

#right view

def rightView(root):
    result=[]
    def recFunc(root,level):
        if not root:
            return        
        if level==len(result):
            result.append(root.val)

        recFunc(root.right,level+1)
        recFunc(root.left,level+1)

        return result
    return recFunc(root,0)
print(rightView(root))
print("right and left views, above and below")

def leftView(root):
    result=[]
    def recFunc(root,level):
        if not root:
            return        
        if level==len(result):
            result.append(root.val)

        recFunc(root.left,level+1)
        recFunc(root.right,level+1)

        return result
    return recFunc(root,0)
print(leftView(root))

#L25. Check for Symmetrical Binary Trees

def symmetricalTree(t1,t2):
    if not t1 and not t2:
        return True
    
    if not t1 or not t2:
        return False
    
    if t1.val!=t2.val:
        return False
    
    return (symmetricalTree(t1.left,t2.right) and symmetricalTree(t1.right,t2.left))

print("symmetrical tree")
print(symmetricalTree(root,root))

#return node to path, pathPrint Root to Node Path in Binary Tree

def nodeToPath(root,target):
    result=[]
    def dfs(root):
        if not root:
            return False
        result.append(root.val)
        if root.val==target:
            return True
        if (dfs(root.left) or dfs(root.right)):
            return True
        result.pop()
        return False
    dfs(root)
    return result

print("node to path")
print(nodeToPath(root,5))
        

# L27. Lowest Common Ancestor in Binary Tree | LCA 

def LCA(root,p,q):
    if not root:
        return None
    if root.val==p or root.val==q:
        return root.val
    left=LCA(root.left,p,q)
    right=LCA(root.right,p,q)

    if left and right:
        return root.val
    
    return left if left else right
print("LCA")
print(LCA(root,4,5))

#  Maximum Width of Binary Tree 

def maxWidth(root):
    if not root:
        return 0
    
    queue=deque([(root,0)])
    max_width=0
    while queue:
        level_size=len(queue)
        min_index=queue[0][1]
        first=last=0
        for i in range(level_size):
            root,index=queue.popleft()
            cur_id=index-min_index

            if i==0:
                first=cur_id
            if i==level_size-1:
                last=cur_id

            if root.left:
                queue.append((root.left,2*cur_id+1))

            if root.right:
                queue.append((root.right,2*cur_id+2))
        max_width=max(max_width,last-first+1)
    return max_width

print("maxWidth")
print(maxWidth(root))


# Children Sum Property in Binary Tree 

# def childrenSum(root):
#     if not root:
#         return
#     current_sum=0
#     if root.left:
#         current_sum+=root.left.val
#     if root.right:
#         current_sum+=root.right.val

#     if current_sum<root.val:
#         if root.left:
#             root.left.val=root.val
#         if root.right:
#             root.right.val=root.val

#     childrenSum(root.left)
#     childrenSum(root.right)
#     total=0
#     if root.left:
#         total+=root.left.val
#     if root.right:
#         total+=root.right.val

#     if root.left or root.right:
#         root.val=total

# print("children sum")
# print(childrenSum(root))

# def printNewChildren(root):
#     if not root:
#         return
#     print(root.val)
#     printNewChildren(root.left)
#     printNewChildren(root.right)

# printNewChildren(root)

def markParents(root,parentslist):
    queue=[root]
    while queue:
        node=queue.pop(0)
        if node.left:
            parentslist[node.left]=node
            queue.append(node.left)
        if node.right:
            parentslist[node.right]=node
            queue.append(node.right)


def nodesAtDistance(root,target,k):
    parentslist={}
    markParents(root,parentslist)

    queue=deque([target])
    visited=set()
    visited.add(target)
    distance=0
    while queue:
        if distance==k:
            break
        
        size=len(queue)
        for _ in range(size):
            node=queue.popleft()
            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append(node.left)

            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append(node.right)
            if node in parentslist and parentslist[node] not in visited:
                visited.add(parentslist[node])                                                          
                queue.append(parentslist[node])

        distance+=1

    return [node.val for node in queue]
        
print("nodes at distance")
print(nodesAtDistance(root,node2,1))

# Minimum time taken to BURN the Binary Tree from a Node

def trackparents(root,parentslist):
    queue=deque([root])
    while queue:
        node=queue.popleft()
        if node.left:
            parentslist[node.left]=node
            queue.append(node.left)
        if node.right:
            parentslist[node.right]=node
            queue.append(node.right)

def burnTree(root,target):
    queue=deque([target])

    parentslist={}
    trackparents(root,parentslist)

    visited=set()
    visited.add(target)
    time=0
    while queue:
        size=len(queue)
        burned=False
        for _ in range(size):
            node=queue.popleft()

            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append(node.left)
                burned=True
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append(node.right)
                burned=True
            if node in parentslist and parentslist[node] not in visited:
                visited.add(parentslist[node])
                queue.append(parentslist[node])
                burned = True  
        if burned:
            time+=1

    return time

print("Minimum time taken to BURN the Binary Tree from a Node")
print(burnTree(root,node2))
            
#  Count total Nodes in a COMPLETE Binary Tree 

def leftHeight(root):
    height=0
    while root:
        height+=1
        root=root.left
    return height

def rightHeight(root):
    height=0
    while root:
        height+=1
        root=root.right
    return height


def countNodes(root):
    if not root:
        return
    lh=leftHeight(root)
    rh=rightHeight(root)

    if lh==rh:
        return (2**lh)-1 #this is formula to count nodes in complete tree
    else:
        return 1+countNodes(root.left) + countNodes(root.right)

print(" Count total Nodes in a COMPLETE Binary Tree ")
print(countNodes(root))


#  Construct a Binary Tree from Preorder and Inorder Traversal

class TreeNodes:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def constructBinary(preorder,inorder):
    
    inordermap={}
    for i,val in enumerate(inorder):
        inordermap[val]=i
    
    preorderIndex=0

    class TreeNode2:
        def __init__(self,val):
            self.val=val
            self.left=left


    def dfs(left,right):
        nonlocal preorderIndex
        if left>right:
            return None
        root_value=preorder[preorderIndex]
        preorderIndex+=1
        roots=TreeNodes(root_value)
        inorderIndex=inordermap[root_value]

        roots.left=dfs(left,inorderIndex-1) 
        roots.right=dfs(inorderIndex+1,right)

        return roots
    return dfs(0,len(inorder)-1)

preorder = [1,2,4,5,3]
inorder  = [4,2,5,1,3]

roots = constructBinary(preorder, inorder)


# def inorderTraversal(root):
#     if not root:
#         return

#     inorderTraversal(root.left)
   
#     inorderTraversal(root.right)
#     print(root.val, end=" ")

# print("Inorder Traversal:")
# inorderTraversal(roots)


class TreeNode2:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def buildingTree(inorder1,postorder1):
    inordermap={}
    for i,val in enumerate(inorder1):
        inordermap[val]=i
    postIndex=len(postorder1)-1

    def dfs(left,right):
        nonlocal postIndex
        if left>right:
            return None
        rootValue=postorder1[postIndex]
        postIndex-=1

        root2=TreeNode2(rootValue)
        inorderIndex=inordermap[rootValue]

        root2.right=dfs(inorderIndex+1,right)
        root2.left=dfs(left,inorderIndex-1)
        return root2
    
    return dfs(0,len(inorder1)-1)

postorder1 = [4,5,2,3,1]
inorder1   = [4,2,5,1,3]
buildingTree(inorder1,postorder1)


def serialize(root):
    if not root:
        return ""
    
    queue=deque([root])
    result=[]
    while queue:
        node=queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        else:
            result.append("N")

    return ",".join(result)

print("serialize")
print(serialize(root))



class deserializeTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def deserialize(data):
    if not data:
        return None
    values=data.split(",")
    root=deserializeTree(values[0])

    queue=deque([root])
    index=1
    while queue:
        node=queue.popleft()
        if values[index] != "N":
            node.left=deserializeTree(values[index])
            queue.append(node.left)
        index+=1

        if values[index] !="N":
            node.right=deserializeTree(values[index])
            queue.append(node.right)
        index+=1

    return root

print("deserialize")
print(deserialize("1,2,3,N,N,4,5,N,N,N,N"))


def morrisInorder(root):
    
    
    current=root
    while current:
        if not current.left:
            print(current.val, end=" ")
            current=current.right
        else:
            predecessor=current.left
            while predecessor.right and predecessor.right!=current:
                predecessor=predecessor.right

            if not predecessor.right:
                print(current.val,end=" ")
                predecessor.right=current
                current=current.left

            else:
                predecessor.right=None
                current=current.right
print("morris Inorder")
print(morrisInorder(root))



def flattenArray(root):
    prev=None
    def dfs(root):
        nonlocal prev

        if not root:
            return
        
        dfs(root.right)
        dfs(root.left)

        root.right=prev

        root.left=None
        
        root=prev
    dfs(root)

print(flattenArray(root))