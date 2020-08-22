from binaryTree import BinaryTreeNode
import queue
from traversal import levelOrderTraversal
maximum=float("-infinity")
def findMaxRecursive(root):
    global maximum
    if not root:
        return maximum
    if root.data>maximum:
        maximum=root.getData()
    findMaxRecursive(root.getLeft())
    findMaxRecursive(root.getRight())
    return maximum
maximum=float("-infinity")
def findMaxIterative(root):
    global maximum
    if not root:
        return maximum
    q=queue.Queue()
    q.put(root)
    node=None
    while not q.empty():
        node=q.get()
        if maximum<node.getData():
            maximum=node.getData()
        if node.getLeft() is not None:
            q.put(node.getLeft())
        if node.getRight() is not None:
            q.put(node.getRight())
    return maximum
def insertInBinaryTree(root,data):
    new=BinaryTreeNode(data)
    if not root:
        root=new
        return root
    q=queue.Queue()
    q.put(root)
    while not q.empty():
        node=q.get()
        if node.getData()==data:
            return root
        if node.getLeft() is None:
            node.left=new
            return root
        else:
            q.put(node.getLeft())
        if node.getRight() is None:
            node.right=new
            return root
        else:
            q.put(node.getRight())
        
    
a=BinaryTreeNode(3)
b=BinaryTreeNode(4)
c=BinaryTreeNode(5)
d=BinaryTreeNode(0)
a.left=b
a.right=c
b.left=d
print(findMaxRecursive(a))
print(findMaxIterative(a))
insertInBinaryTree(a,7)
l=[]
levelOrderTraversal(a,l)
print(l)

