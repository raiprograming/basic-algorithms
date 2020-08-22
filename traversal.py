from binaryTree import BinaryTreeNode
import queue
def preOrderRecursive(root,result):
    if not root:
        return
    result.append(root.data)
    preOrderRecursive(root.left,result)
    preOrderRecursive(root.right,result)
def preOrderIterative(root,result):
    if not root:
        return
    stack=[]
    stack.append(root)
    while stack:
        node=stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
def inOrderRecursive(root,result):
    if not root:
        return
    inOrderRecursive(root.left,result)
    result.append(root.data)
    inOrderRecursive(root.right,result)
def inOrderIterative(root,result):
    if not root:
        return
    stack=[]
    node=root
    while stack or node:
        if node:
            stack.append(node)
            node=node.left
        else:
            node=stack.pop()
            result.append(node.data)
            node=node.right
def postOrderRecursive(root,result):
    if not root:
        return
    postOrderRecursive(root.left,result)
    postOrderRecursive(root.right,result)
    result.append(root.data)
def postOrderIterative(root,result):
    if not root:
        return
    visited=set()
    stack=[]
    node=root
    while stack or node:
        if node:
            stack.append(node)
            node=node.left
        else:
            node=stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node=node.right
            else:
                visited.add(node)
                result.append(node.data)
                node=None 
def levelOrderTraversal(root,result):
    if not root:
        return
    q=queue.Queue()
    q.put(root)
    node=None
    while not q.empty():
        node=q.get()
        result.append(node.getData())
        if node.getLeft() is not None:
            q.put(node.getLeft())
        if node.getRight() is not None:
            q.put(node.getRight())

a=BinaryTreeNode(4)
b=BinaryTreeNode(3)
c=BinaryTreeNode(5)
d=BinaryTreeNode(7)
c.left=d
a.left=b
a.right=c
res=[]
inOrderRecursive(a,res)
print(res)
res.clear()
inOrderIterative(a,res)
print(res)
res.clear()
postOrderIterative(a,res)
print(res)
res.clear()
levelOrderTraversal(a,res)
print(res)
