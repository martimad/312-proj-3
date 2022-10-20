import math


class MyQueue:
    def makeQueue(self, graph):
        pass

    def add(self, node):
        pass

    def deleteMin(self, dist):
        pass

    def decreaseKey(self, node, minVal):
        pass


class arrayPQ(MyQueue):
    def __init__(self):
        self.nodeArray = []

    def makeQueue(self, graph):
        self.nodeArray = [node for node in graph]   # list comprehension

    def add(self, node):
        self.nodeArray.append(node)

    def deleteMin(self, dist):
        minVal = math.inf
        minNode = None
        minIndex = 0
        for i, node in enumerate(self.nodeArray):  # TODO please explain how this works i copied it from a friend
            if minVal >= dist[node]:
                minVal = dist[node]
                minIndex = i
                minNode = node
        self.nodeArray.pop(minIndex)
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
        for node in graph:
            self.insert(node, math.inf)

    def add(self, listOfNodes):
        for node in listOfNodes:
            self.insert(node, math.inf)

    def deleteMin(self, dist):  # this one just returns min right and deletes it from queue
        minNode = self.nodeArrayHeap[0][0]
        self.nodeArrayHeap[0] = self.nodeArrayHeap[-1]  # replace with last item
        self.nodeArrayHeap.pop(-1)  # delete the items from the arrays
        self.indices.pop(minNode)
        if not len(self.indices) == 0:
            self.indices[self.nodeArrayHeap[0][0]] = 0  # set last ones new index to 0
            self.heapify(0)
        return minNode

    def decreaseKey(self, node, newVal):  # this heapifies the new updated values
        if node not in self.indices.keys():
            return
        index = self.indices[node]  # the index it used to be at
        oldVal = self.nodeArrayHeap[index][1]
        self.nodeArrayHeap[index] = (node, newVal)
        self.bubbleUp(index)
        #self.heapify(index)

    def swap(self, first, second):
        firstNode = self.nodeArrayHeap[first]
        secondNode = self.nodeArrayHeap[second]
        tempIndex = self.indices[firstNode[0]]
        self.nodeArrayHeap[first] = secondNode
        self.indices[firstNode[0]] = self.indices[secondNode[0]]
        self.nodeArrayHeap[second] = firstNode
        self.indices[secondNode[0]] = tempIndex

    def bubbleUp(self, index):
        while self.nodeArrayHeap[index][1] < self.nodeArrayHeap[parent(index)][1]:  # while larger than parent
            self.swap(index, parent(index))
            index = parent(index)
            if index == 0:
                break


    def insert(self, node, dist):
        self.nodeArrayHeap.append((node, dist))
        self.indices[node] = len(self.nodeArrayHeap) - 1
        current = len(self.nodeArrayHeap) - 1
        self.bubbleUp(current)

    def heapify(self, index):
        # if not index == 0:  # meaning it's not the top-top node
        #     while self.nodeArrayHeap[index][1] < self.nodeArrayHeap[parent(index)][1]:  # while smaller than parent
        #         self.swap(index, parent(index))
        #         index = parent(index)
        if not self.isLeaf(index):  # if it's not the top node,and it's bubbled up as high as it needs,then send it down
            # children - 2n+1  and 2n+2
            # parents - (n-1) // 2
            swapPosition = index
            leftChild = (2 * index) + 1
            rightChild = (2 * index) + 2
            leftChildVal = self.nodeArrayHeap[leftChild][1]
            rightChildVal = math.inf
            if rightChild < len(self.nodeArrayHeap):
                rightChildVal = self.nodeArrayHeap[rightChild][1]
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