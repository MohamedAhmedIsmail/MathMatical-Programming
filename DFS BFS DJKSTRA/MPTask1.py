# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:04:16 2017
@author: MohamedIsmail
"""
import time
import queue as Qu
class Node(object):
    def __init__(self, value, w):
        self.value = value
        self.w = w
    def __ge__(self, node):
        return self.w >= node.w

    def __le__(self, node):
        return self.w <= node.w

    def __lt__(self, node):
        return self.w < node.w

    def __gt__(self, node):
        return self.w > node.w


class Edge(object):
    def __init__(self, a, b, w):
        self.u = a
        self.v = b
        self.w = w


class Graph(object):
    def __init__(self):
        self.graph = {}
        self.dist = {}  # for DFS

    def AddNode(self, node):
        if node.value not in self.graph.keys():
            self.graph[node.value] = []
            self.dist[node.value] = 1e9

    def AddEdge(self, edge):
        self.graph[edge.u].append(Node(edge.v, edge.w))
        self.graph[edge.v].append(Node(edge.u, edge.w))

    def BfS(self, s, d):
        q = Qu.Queue()
        q.put(s)
        dist = {}
        par = {}
        for node in self.graph.keys():
            dist[node], par[node] = 1e9, -1

        dist[s] = 0
        while not q.empty():
            node = q.get()
            for x in self.graph[node]:
                if (dist[x.value] <= dist[node] + x.w):
                    continue
                par[x.value] = node
                q.put(x.value)
                dist[x.value] = dist[node] + x.w
        '''tmp = d
        path = []
        while(tmp != -1):
            path.append(tmp)
            tmp = par[tmp]
        path.reverse()
        print("PATH  (BFS):" ,path)'''
        if dist[d] == 1e9:
            dist[d] = -1
        return dist[d]
    def Dijkstra(self, s, d):
        pq = Qu.PriorityQueue()
        pq.put(Node(s, 0))
        vis = {}
        par = {}
        for node in self.graph.keys():
            vis[node], par[node] = 0, -1
        vis[s] = 1
        ans = -1
        while not pq.empty():
            node = pq.get()

            if (node.value == d):
                ans = node.w
                break
            vis[node.value] = 1
            for x in self.graph[node.value]:
                if (vis[x.value] == 1):
                    continue
                # print(node.value + 1 , " to " , x.value + 1 , " with " , x.w + node.w , " x.w = ", x.w)
                pq.put(Node(x.value, x.w + node.w))
                par[x.value] = node.value
        '''tmp = d
        path = []
        while(tmp != -1):
            path.append(tmp)
            tmp = par[tmp]
        path.reverse()
        print("(DIJKSTRA) PATH :" ,path)'''
        return ans
    """
    def depth_first_search(graph,s,d,ret=0):
        
        visited, stack = set(), [self.]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(graph[vertex] - visited)
        return visited
    """
    def Dfs(self, s, d, ret=0):
        if (s == d):
            return ret
        mn = 1e9
        for node in self.graph[s]:
            if (self.dist[node.value] > node.w + ret):
                self.dist[node.value] = node.w + ret
                mn = min(self.Dfs(node.value, d, ret + node.w), mn)
        return mn
Path = "E:/computer science/courses/year 4/semester 1/MathMatical programming/Labs/Lab1/Test Cases/"
Files = ["n10_001.txt", "n10_002.txt", "n100_001.txt", "n100_002.txt", "n1000_001.txt", "n1000_002.txt"]
idx = 1
for filePath in Files:
    f = open(Path + filePath)
    NumberOfNodes = int(f.readline())
    NumberOfEdges = int(f.readline())
    S = int(f.readline())
    D = int(f.readline())
    content = f.read().split('\n')
    G = Graph()

    for line in content:
        edge = line.split(' ')
        try:
            v, u, w = int(edge[0]), int(edge[1]), 1
            if (len(edge) != 2 and edge[2] != ''):
                w = int(edge[2])
            G.AddNode(Node(u, 0))
            G.AddNode(Node(v, 0))
            G.AddEdge(Edge(u, v, w))
        except:
            edge = ""
    print("File ", idx)
    idx = idx + 1
    ft = time.time()
    print("ShortestPath Gh  : ", G.Dijkstra(S, D))
    lt = time.time()
    print("Taken time : ", lt - ft)

# For DFS
'''
File  1
ShortestPath Gh  :  2345
Take time :  0.0
File  2
ShortestPath Gh  :  8256
Take time :  0.0
File  3
ShortestPath Gh  :  1273
Take time :  2.640728712081909
File  4
ShortestPath Gh  :  1855
Take time :  1.1406700611114502
'''

# For BFS
''''
File  1
ShortestPath Gh  :  2345
Take time :  0.0
File  2
ShortestPath Gh  :  8256
Take time :  0.0
File  3
ShortestPath Gh  :  1273
Take time :  0.04686284065246582
File  4
ShortestPath Gh  :  1855
Take time :  0.04688286781311035
File  5
ShortestPath Gh  :  67
Take time :  20.207194566726685
File  6
ShortestPath Gh  :  181
Take time :  6.547186613082886
'''

# For Dijkstra
'''
File  1
ShortestPat Gh  :  2345
Take time :  0.0
File  2
ShortestPat Gh  :  8256
Take time :  0.0
File  3
ShortestPat Gh  :  1273
Take time :  0.06250166893005371
File  4
ShortestPat Gh  :  1855
Take time :  0.015625
File  5
ShortestPat Gh  :  67
Take time :  6.470996618270874
File  6
ShortestPat Gh  :  181
Take time :  3.4376580715179443
'''

