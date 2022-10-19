import math


class MyQueue:
    def makeQueue(self, graph):
        pass
    def add(self, listOfNodes):
        pass

    def deleteMin(self):
        pass

    def decreaseKey(self):
        pass


class arrayPQ(MyQueue):
    def __init__(self):
        self.nodeArray = []

    def makeQueue(self, graph):
        self.nodeArray = [node for node in graph.getNodes()]   # list comprehention

    def add(self, listOfNodes):
        # for i in listOfNodes:
        self.nodeArray += listOfNodes

    def deleteMin(self, dist):
        minVal = math.inf
        minNode = None
        for i in dist:
            if i not in self.nodeArray: # if it's not in the priority queue, only want ones we haven't seen
                continue
            if dist[i] < minVal:
                minVal = dist[i]
                minNode = i  # node name not a num
        self.nodeArray.remove(minNode)
        return minNode

    def __len__(self):
        return len(self.nodeArray)


def parent(current):
    return (current - 1) // 2


class heapPQ(MyQueue):
    def __init__(self):
        self.nodeArrayHeap = []
        self.heapSize = 0

    def makeQueue(self, graph):
        # children - 2n+1  and 2n+2
        # parents - (n-1) // 2
        self.nodeArrayHeap = [self.insert(node) for node in graph.getNodes()] # TODO does this actually insert correctly?

    def add(self, listOfNodes):
        self.nodeArrayHeap = [self.insert(node) for node in listOfNodes] # TODO this too, also increment the heap size

    def deleteMin(self):  # TODO this one just returns min right
        return self.nodeArrayHeap[0]

    def decreaseKey(self):  # TODO but this one actually removes top node and heapifies
        self.nodeArrayHeap[0] = self.nodeArrayHeap[self.heapSize -1] # replace with last item
        self.nodeArrayHeap.__delitem__(-1)
        --self.heapSize
        self.heapify(0)

    def swap(self, first, second):
        temp = self.nodeArrayHeap[first]
        self.nodeArrayHeap[first] = self.nodeArrayHeap[second]
        self.nodeArrayHeap[second] = temp

    def insert(self, node):
        self.nodeArrayHeap[++self.heapSize] = node
        current = self.heapSize

        while self.nodeArrayHeap[current] < self.nodeArrayHeap[parent(current)]: #while larger than parent
            self.swap(current, parent(current))
            current = parent(current)

    def heapify(self, index):
        if not self.isLeaf(index):
            # children - 2n+1  and 2n+2
            # parents - (n-1) // 2
            swapPosition = index
            rightChild = (2 * index) + 1
            leftChild = (2 * index) + 2
            rightChildVal = self.nodeArrayHeap[rightChild]
            leftChildVal = self.nodeArrayHeap[leftChild]
            if rightChild <= self.heapSize:
                if leftChildVal < rightChildVal:
                    swapPosition = rightChild
                else:
                    swapPosition = leftChild
            else:  # TODO figure this one out, why val not left child
                swapPosition = leftChildVal
            if self.nodeArrayHeap[index] > leftChildVal or self.nodeArrayHeap[index] > rightChildVal:
                self.swap(index, swapPosition)
                self.heapify(swapPosition)

    def isLeaf(self, index):
        if index > self.heapSize/2:
            return True
        else:
            return False
