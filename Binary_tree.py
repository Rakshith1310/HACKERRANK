class Node: 
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
class Tree:
    def createNode(self, data):
        return Node(data)
    def insertNode(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insertNode(node.left, data)
        else data > node.data:
            node.right = self.insertNode(node.right, data)
        return node
    def deleteNode(self, node, data):
        if node is None: return None
        if node.data == data:
            if not node.right and not node.left:
                return None
            if not node.right and node.left:
                return node.lef
            if not node.left and node.right: 
                return node.right
            else:
                pnt = node.left
                while pnt.left!=None:
                    pnt = pnt.left
                node.data = pnt.data
                node.right = self.deleteNode(node.right, node.data)
            if data<node.data:
                node.left = deleteNode(node.left, data)
            else:
                node.right = deleteNode(node.right, data)
