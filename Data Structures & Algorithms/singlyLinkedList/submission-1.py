class Node:
    def __init__(self, val: int, next_node = None) -> None:
        self.val = val
        self.nextNode = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.nextNode

        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.nextNode
        return - 1

    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.nextNode = self.head.nextNode
        self.head.nextNode = new_head
        if not new_head.nextNode:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        self.tail.nextNode = Node(val)
        self.tail = self.tail.nextNode

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.nextNode
        
        if curr and curr.nextNode:
            if curr.nextNode == self.tail:
                self.tail = curr
            curr.nextNode = curr.nextNode.nextNode
            return True
        return False
 
    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.nextNode
        while curr:
            arr.append(curr.val)
            curr = curr.nextNode
        return arr
