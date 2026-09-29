print("bSt")

class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = treeNode(4)

root.left = treeNode(2)
root.right = treeNode(5)
root.right.left=treeNode(4.6)
root.right.right=treeNode(6)

root.left.left = treeNode(1)
root.left.right = treeNode(3)

# root = treeNode(4)

# root.left = treeNode(2)
# root.right = treeNode(6)

# root.left.left = treeNode(1)
# root.left.right = treeNode(3)

# root.right.left = treeNode(5)
# root.right.right = treeNode(7)

def searchBST(root, target):

    if not root:
        return False
    
    if root.val == target:
        return True
    
    if target < root.val:
        return searchBST(root.left, target)

    return searchBST(root.right, target)


print(searchBST(root, 5))


# Ceil in a Binary Search Tree | BST

def ceilBST(root,target):
    ceil=-1
    while root:
        if target==root.val:
            return root.val
        if target>root.val:
            root=root.right
        else:
            ceil=root.val
            root=root.left
    return ceil

print("ceil in root")
print(ceilBST(root,1.5))

#Floor in a Binary Search Tree

def floor(root,target):
    floorval=-1
    while root:
        if target==root.val:
            return target
        
        if target<root.val:
            root=root.left

        else:
            floorval=root.val
            root=root.right

    return floorval
print("floor val")
print(floor(root,4.5))

#Insert a given Node in Binary Search Tree 
# def insertNode(root,val):
#     if root is None:
#         return treeNode(val)
#     if val<root.val:
#         root.left=insertNode(root.left,val)
#     else:
#         root.right=insertNode(root.right,val)
#     return root

# print("insert in bst")
# print(insertNode(root,9))
    

def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

preorder(root)


# Delete a Node in Binary Search Tree

# def deleteNode(root,key):
#     if not root:
#         return None
    
#     if key<root.val:
#         root.left=deleteNode(root.left,key)
#     if key>root.val:
#         root.right=deleteNode(root.right,key)

#     else:
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
#         else:
#             successor= findMin(root.right)
#             root.right=successor.val
#             root.right=deleteNode(root.right,successor.val)
    

# def findMin(root):
#     while root.left:
#         root=root.left

#     return root

# deleteNode(root,9)


def preorder(root):
    if not root:
        return
    
    preorder(root.left)
    print(root.val,"ll")
    preorder(root.right)

preorder(root)


# K-th Smallest/Largest Element in BST
#if we do iterative inorder traversal of a BST, we will get the elements in sorted order.


def KthSmallest(root,k):
    current=root
    stack =[]

    while True:
        while current:
        
            stack.append(current)
            current=current.left
        current=stack.pop()
        k-=1
        if k==0:
            return current.val
            
        current=current.right
print("kth smallest")
print(KthSmallest(root,4))


def kthLargest(root,k):
    current=root
    stack=[]

    while True:
        while current:
            stack.append(current)
            current=current.right
        current=stack.pop()

        k-=1
        if k==0:
            return current.val
        
        current=current.left

print("kth largest")
print(kthLargest(root,3))




#L46. Check if a tree is a BST or BT | Validate a BST

def isBST(root,min=float('-inf'),max=float('inf')):
    if not root:
        return True
    if not(min<root.val<max):
        return False
    
    leftWing=isBST(root.left, min,root.val)
    rightWing=isBST(root.right, root.val,max)
    return leftWing and rightWing
print("checking if its a BST")
print(isBST(root))


#find the lca in bst

def lca(root,val1,val2):
    if not root:
        return None
    
    if val1<root.val and val2<root.val:       
        return lca(root.left,val1,val2)

    if val1>root.val and val2>root.val:
        return lca(root.right,val1,val2)

    return root.val

print("finding lca")
print(lca(root,4.6,6))


# L48. Construct a BST from a preorder traversal 

class TreeNode1:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def insert(root1,val):
    if root1 is None:
        return TreeNode1(val)
    
    if val<root1.val:
        root1.left=insert(root1.left,val)

    else:
        root1.right=insert(root1.right,val)

    return root1

def build(array):
    root1=None

    for val in array:
        root1=insert(root1,val)
    
    return root1

array=[8, 5, 1]

root1=build(array)


def preordcheck(root1):
    if not root1:
        return
    
    print(root1.val)
    preordcheck(root1.left)
    preordcheck(root1.right)
print("rintin preorder")
preordcheck(root1)



#  Inorder Successor/Predecessor in BST
def successor(root,val):
    success=None

    while root:
        if val<root.val:
            success=root

            root=root.left
        else:
            root=root.right

    return success.val

print("successor")
print(successor(root,4))


def predessor(root,val):
    pred=None
    while root:
        if val>root.val:
            pred=root.val

            root=root.right

        else:
            root=root.left

    return pred

print("predessor")
print(predessor(root,5))


# Binary Search Tree Iterator | BST 

class BSTiterator:
    def __init__(self,root):
        self.stack=[]
        self.pushLeft(root)

    def pushLeft(self,node):
        while node:
            self.stack.append(node )
            node=node.left

    def next(self):
        node=self.stack.pop()

        self.pushLeft(node.right)
        return node.val 
    
    def hasnext(self):
        return len(self.stack)>0 
    

iterator=BSTiterator(root)
print("check iterator")
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())

print(iterator.hasnext())


#Two Sum In BST | Check if there exists a pair with Sum K

def twoSumTree(root,target):
    seen=set()  

    def dfs(root):
        if not root:
            return False

        if (target-root.val)  in seen:
            return True
        seen.add(root.val)

        return dfs(root.right) or dfs(root.left)

    return dfs(root)



print("check 2 sum")
print(twoSumTree(root,9))



# Recover BST | Correct BST with two nodes swapped


class RecoverTreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


class Solution:
    def recovery(self,root):
        self.first =None
        self.middle=None
        self.last=None

        self.prev=RecoverTreeNode(float('-inf'))

        self.inorder(root)

        if self.first and self.last:
            self.first.val,self.last.val=(self.last.val,self.first.val)

        elif self.first and self.middle:
            self.first.val,self.middle.val=(self.middle.val,self.first.val)

        
    def inorder(self,root):
        if not root:
            return

        self.inorder(root.left)
        if self.prev.val>root.val:
            if not self.first:
                self.first=self.prev
                self.middle=root
            else:
                self.last=root

            
        self.prev=root

        self.inorder(root.right)



root = RecoverTreeNode(3)

root.left = RecoverTreeNode(1)

root.right = RecoverTreeNode(4)

root.right.left = RecoverTreeNode(2)


obj=Solution()
obj.recovery(root)

def inordcheck(root):
    if not root:
        return
    
    inordcheck(root.left)
    print("hghg",root.val)
    inordcheck(root.right)

inordcheck(root)



# L53. Largest BST in Binary Tree

class finalTreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class NodeValue:

    def __init__(self,minNode,maxNode,maxSize):
        self.minNode=minNode
        self.maxNode=maxNode
        self.maxSize=maxSize


class Solutions:
    def largestBST(self,root):
        return self.helper(root).maxSize
    
    def helper(self,root):
        if not root:
            return NodeValue(
                minNode=float('inf'),
                maxNode=float('-inf'),
                maxSize=0
            )
        
        left=self.helper(root.left)
        right=self.helper(root.right)

        if left.maxNode<root.val<right.minNode:
            return NodeValue(
                min(root.val,left.minNode),
                max(root.val,right.maxNode),
                left.maxSize+right.maxSize+1
            )
        
        return NodeValue(
            float('-inf'),
            float('inf'),
            max(left.maxSize,right.maxSize)
        )
    

finalRoot = finalTreeNode(10)

finalRoot.left = finalTreeNode(5)
finalRoot.right = finalTreeNode(15)

finalRoot.left.left = finalTreeNode(1)
finalRoot.left.right = finalTreeNode(8)

finalRoot.right.right = finalTreeNode(7)




objs=Solutions()
print(objs.largestBST(finalRoot))