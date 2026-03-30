class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        
        new_node = Node(key, val)

        if not self.root:
            self.root = new_node
            return

        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
       
        curr = self.root
        
        while curr:
            if key == curr.key:
                return curr.val
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        
        return -1

    def getMin(self) -> int:

        current = self.findMin(self.root)
        return current.val if current else -1
        
    def findMin(self, node: Node) -> Node:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        current = self.root
        while current and current.right:
            current = current.right
        return current.val if current else -1

    def remove(self, key: int) -> None:

        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, curr: Node, key: int) -> Node:

        if curr == None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)

        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result
    
    def inorderTraversal(self, root: Node, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
