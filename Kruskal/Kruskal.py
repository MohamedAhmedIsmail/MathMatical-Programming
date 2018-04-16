from collections import defaultdict
import sys
#Class to represent a graph
class Graph:

    def __init__(self,vertices):
        self.V= vertices
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
    def KruskalMST(self):
        result =[]
        i = 0
        e = 0
        self.graph =  sorted(self.graph,key=lambda item: item[2])
        parent = [] ; rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V -1 :
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
            if x != y:
                e = e + 1
                result.append([u,v,w])
                self.union(parent, rank, x, y)
        print ("Following are the edges in the constructed MST")
        for u,v,weight  in result:
            print(u, v, weight)
        alist=[]
        for u,v, weight in result:
            alist.append(weight)
        print ("The minimum weight = ",sum(alist))
g = Graph(2)
g.addEdge(2, 1, 67)
g.addEdge(3, 1, 46)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.KruskalMST()