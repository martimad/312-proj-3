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
            self.insert(node)

    def add(self, listOfNodes):
        for node in listOfNodes:
            self.insert(node)

    def deleteMin(self):  # this one just returns min right and deletes it from queue
        minNode = self.nodeArrayHeap[0][0]
        self.nodeArrayHeap[0] = self.nodeArrayHeap[-1]  # replace with last item
        self.nodeArrayHeap.__delitem__(-1)
        self.heapify(0)
        return minNode

    def decreaseKey(self, node, newVal):  # this heapifies the new updated values
        index = self.indices[node]
        self.nodeArrayHeap[index] = (node, newVal)
        self.heapify(index)

    def swap(self, first, second):
        temp = self.nodeArrayHeap[first]
        tempIndex = self.indices[first]
        self.nodeArrayHeap[first] = self.nodeArrayHeap[second]
        self.indices[first] = self.indices[second]
        self.nodeArrayHeap[second] = temp
        self.indices[second] = tempIndex

    def insert(self, node, dist):
        self.nodeArrayHeap.append((node, dist))
        self.indices[node] = self.nodeArrayHeap.__sizeof__() - 1
        current = self.nodeArrayHeap.__sizeof__()
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
            if rightChild <= self.nodeArrayHeap.__sizeof__():
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
        if index > self.nodeArrayHeap.__sizeof__()/2:
            return True
        else:
            return False
