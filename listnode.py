class listnode:
    def __init__(self,data):
        self.data=data
        self.next=None
    def traversal(self,head):
        node=head
        while node is not None:
            print(node.data)
            node=node.next
    def searchnode(self,head,target):
        node=head
        while node.next is not None and node.data !=target:
            node=node.next
        return node is not None
    def removenode(self,head,target):
        curnode=head
        prednode=None
        while curnode is not None and curnode.data !=target:
            prednode=curnode
            curnode=curnode.next
        if curnode is not None:
            if curnode is head:
                head=curnode.next
            else:
                prednode.next=curnode.next
                
