#!/usr/bin/python3
import math

from CS312Graph import *
import MyQueue
import time



class NetworkRoutingSolver:
    def __init__(self):
        self.source = None
        #self.dest = None
        self.prev = None
        self.dist = None

    def initializeNetwork(self, network):
        assert(type(network) == CS312Graph)
        self.network = network


    # RETURN THE SHORTEST PATH FOR destIndex using dist and prev from dijks
    def getShortestPath(self, destIndex):
        self.dest = destIndex
        path_edges = []
        total_length = 0
        #node = self.network.nodes[self.source]
        node = self.network.nodes[destIndex]
        edges_left = 3
        #dummy edges
        # while edges_left > 0:
        #     edge = node.neighbors[2]
        #     path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
        #     total_length += edge.length
        #     node = edge.dest
        #     edges_left -= 1

        while not node.node_id == self.source:
            # follow path of prev array add to nodes
            prevNode = self.prev[node]
            edge = node.neighbors[prevNode]  #TODO can i reference the neighbor that I want by name in a dic? and i want the prev neighbor
            path_edges.append((edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)))
            total_length += edge.length
            node = self.prev[node]

        return {'cost': total_length, 'path': path_edges}

    # RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
    def computeShortestPaths(self, srcIndex, use_heap=False):
        self.source = srcIndex
        t1 = time.time()
        self.dist, self.prev = self.dijkstra(srcIndex, use_heap)
        t2 = time.time()
        return t2 - t1

    # time complexity - O(n^2)
    def dijkstra(self, src, isBinaryHeap):  # TODO time completities of both implementations

        prev = {}  # using dictionaries instead of arrays, allows me to store the name of the node and its distance
        dist = {}

        # make all inf
        for node in self.network.getNodes():  # kinda like appending all of them
            if node.node_id == src:
                dist[node] = 0
                prev[node] = None
            else:
                dist[node] = math.inf

        if isBinaryHeap: # determines which type of queue to use
            queue = MyQueue.heapPQ()
        else:
            queue = MyQueue.arrayPQ()
        queue.makeQueue(self.network)

        # overall complexity - O(n^2)
        while len(queue) > 0:  # while there's still nodes - O(n)
            curr = queue.deleteMin(dist)
            for neighbor in curr.neighbors: # could be neighbors with each - O(n)
                # get tentative val
                tentative_val = dist[curr] + neighbor.length # - O(1)
                if tentative_val < dist[neighbor.dest]:  # - O(1)
                    dist[neighbor.dest] = tentative_val
                    prev[neighbor.dest] = curr
                    queue.decreaseKey()
        return dist, prev

