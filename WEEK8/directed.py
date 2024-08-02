import matplotlib.pyplot as plt
import queue
class DirectedGraph:
    def __init__(self, n = None):
        self.isFree = True
        self.n = 0
        self.nEdges = 0
        self.graph = {}
        self.prob = {}
        if n is not None :
            self.isFree = False
            self.n = n
            for i in range(1,n+1):
                self.graph[i] = list()

    # def addProb (self):
    #     for i in range(1,self.n+1):
    #         for neigh in self.graph[i]:
    #             self.prob[(i,neigh)] = 1/len(self.graph[i])

    def addNode(self,newNode):
        if not self.isFree and newNode> self.n:
            raise Exception("Node index cannot exceed number of nodes")
        else:
            self.graph[newNode] = list()
            self.n+=1
    
    def addEdge(self,a,b):
        if not self.isFree:
            if(a>self.n or b>self.n):
                raise Exception("Node index cannot be greater than number of nodes")
        if a not in self.graph.keys():
            self.graph[a] = list()
        if b not in self.graph.keys():
            self.graph[b] = list()
        self.graph[a].append(b)
        # self.graph[b].append(a)
        self.nEdges+=1
    
    def __add__(self, other):
        new_instance = DirectedGraph(self.n)  # Create a new instance with the same number of nodes
        new_instance.graph = self.graph.copy()  # Copy the existing graph
        new_instance.nEdges = self.nEdges  # Copy the edge count
        new_instance.n = self.n
        new_instance.isFree = self.isFree
        if type(other) == int:
            new_instance.addNode(other)
        elif isinstance(other, tuple):
            new_instance.addEdge(other[0],other[1])
        return new_instance
    def __str__(self):
        string = "Graph with " + str(self.n) + " nodes and "+str(self.nEdges)+ " edges.Neighbours of the nodes are as belows\n"
        for i in self.graph:
            string+="Node "+str(i)+ " :" + str(self.graph[i])
            string+="\n"

        return string
    def plotDegDist(self):
        deg = list()
        for i in self.graph :
            deg.append(len(self.graph[i]))
        degDict = {}
        for i in deg:
            if i in degDict:
                degDict[i]+=1
            else :
                degDict[i] = 1
        avg = sum(deg)/len(self.graph)
        x = list(range(0,len(self.graph)))
        y = list()
        for i in x:
            if i in degDict:
                y.append(degDict[i]/len(self.graph))
            else:
                y.append(0)
        plt.axvline(x=avg, label = 'Avg. Node degree', color = 'red')
        # plt.plot(deg, label = 'Actual degree distribution', color = 'blue', marker= 'o')
        plt.scatter(x,y,label = 'Actual degree Distribution')
        plt.xlabel('Node Degree')
        plt.ylabel('Fraction of nodes')
        plt.title('Node Degree Distribution')
        plt.grid(True)
        plt.legend()
        plt.show()
    def isConnected(self):
        frontier = [list(self.graph.keys())[0]]
        expanded = []

        #BFS
        while len(frontier) > 0:
            curr = frontier.pop(0)
            expanded.append(curr)
            frontier += [neigh for neigh in self.graph[curr] if ((neigh not in expanded) and (neigh not in frontier))]

        return len(expanded) == len(self.graph)
    def oneTwoComponentSizes(self):
        vertices = set(self.graph.keys())  # Adjusted range to include all vertices

        # q.put(vertices[0])
        components = [0,0]
        visited = set()  # Keep track of visited nodes
        while True:
            diff = list(vertices-visited)
            if len(diff)<=components[1]:
                break
            q = queue.Queue()
            q.put(diff[0])
            count = 0
            while not q.empty():
                node = q.get()
                visited.add(node)
                count+=1
                # print(node)

                for neighbor in self.graph[node]:  # Assuming self.graph is an adjacency list
                    if neighbor not in visited:
                        q.put(neighbor)
            if count>components[0]:
                components[1] = components[0]
                components[0] = count
            elif count > components[1]:
                components[1] = count

            return components