import math


class MyQueue:
    def makeQueue(self, graph):
        pass
    def add(self, listOfNodes):
        pass

    def deleteMin(self, dist):
        pass

    def decreaseKey(self, node, minVal):
        pass


class arrayPQ(MyQueue):
    def __init__(self):
        self.nodeArray = []

    def makeQueue(self, graph):
        self.nodeArray = [node for node in graph.getNodes()]   # list comprehention

    def add(self, listOfNodes):
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
        self.indices = {}

    def makeQueue(self, graph):
        # children - 2n+1  and 2n+2
        # parents - (n-1) // 2
        for node in graph.getNodes():
            self.insert(node, math.inf)

    def add(self, listOfNodes):
        for node in listOfNodes:
            self.insert(node, math.inf)

    def deleteMin(self, dist):  # this one just returns min right and deletes it from queue
        minNode = self.nodeArrayHeap[0][0]
        self.nodeArrayHeap[0] = self.nodeArrayHeap[-1]  # replace with last item
        self.nodeArrayHeap.pop(-1)  # delete the items from the arrays
        self.indices.pop(minNode)
        self.indices[self.nodeArrayHeap[0][0]] = 0  # set last ones new index to 0
        self.heapify(0)
        return minNode

    def decreaseKey(self, node, newVal):  # this heapifies the new updated values
        index = self.indices[node]
        self.nodeArrayHeap[index] = (node, newVal)
        self.heapify(index)

    def swap(self, first, second):
        firstNode = self.nodeArrayHeap[first]
        secondNode = self.nodeArrayHeap[second]
        tempIndex = self.indices[firstNode[0]]
        self.nodeArrayHeap[first] = secondNode
        self.indices[firstNode[0]] = self.indices[secondNode[0]]
        self.nodeArrayHeap[second] = firstNode
        self.indices[secondNode[0]] = tempIndex

    def insert(self, node, dist):
        self.nodeArrayHeap.append((node, dist))
        self.indices[node] = len(self.nodeArrayHeap) - 1
        current = len(self.nodeArrayHeap) - 1
        while self.nodeArrayHeap[current][1] < self.nodeArrayHeap[parent(current)][1]:  # while larger than parent
            self.swap(current, parent(current))
            current = parent(current)

    def heapify(self, index):
        if not self.isLeaf(index):
            # children - 2n+1  and 2n+2
            # parents - (n-1) // 2
            swapPosition = index
            leftChild = (2 * index) + 1
            rightChild = (2 * index) + 2
            leftChildVal = self.nodeArrayHeap[leftChild][1]
            rightChildVal = self.nodeArrayHeap[rightChild][1]
            if rightChild <= len(self.nodeArrayHeap):
                if leftChildVal < rightChildVal:
                    swapPosition = rightChild
                else:
                    swapPosition = leftChild
            else:
                swapPosition = leftChild
            if self.nodeArrayHeap[index][1] > leftChildVal or self.nodeArrayHeap[index][1] > rightChildVal:
                self.swap(index, swapPosition)
                self.heapify(swapPosition)

    def isLeaf(self, index):
        if index >= (len(self.nodeArrayHeap) - 1) / 2:
            return True
        else:
            return False

    def __len__(self):
        return len(self.nodeArrayHeap)