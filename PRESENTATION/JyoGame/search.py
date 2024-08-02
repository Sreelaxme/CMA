from grid import Grid
from queue import PriorityQueue


class Search:

    def __init__(self, graph : Grid):

        self.graph = graph
        self.pathTree = {}
        self.nodeTree = {}

        self.targetFound = False

    
    def RunSearch(self, start, target, expandcallbacks : list[callable] = [], frontiercallbacks = []):

        self.start = start
        self.target = target
        self.targetFound = False

        frontier = self.GetFrontier()
        self.PushFrontier(frontier, start)
        expanded = set([start])
        self.nodeTree[start] = None
        self.pathTree[start] = None

        while self.FrontierEmpty(frontier):

            curr = self.PopFrontier(frontier)  # Queue  

            [f(curr) for f in expandcallbacks] 
            
            if curr == target:
                self.targetFound = True
                return

            for d,node in self.graph.GetNeighbors(curr).items():
                if node not in expanded:
                    self.pathTree[node] = d
                    self.nodeTree[node] = curr
                    expanded.add(node)
                    self.PushFrontier(frontier, node)

                    [f(node) for f in frontiercallbacks] 


    def GetPathNodes(self) -> list[tuple[int,int]]:
        if not self.targetFound:
            return []
        
        curr = self.target
        pathNodes = []

        while self.nodeTree[curr] != None:
            pathNodes = [curr] + pathNodes
            curr = self.nodeTree[curr]

        return pathNodes
    
    def GetPathEdges(self) -> list[tuple[int,int]]:
        if not self.targetFound:
            return []
        
        curr = self.target
        pathEdges = []

        while self.nodeTree[curr] != None:
            pathEdges = [self.pathTree[curr]] + pathEdges
            curr = self.nodeTree[curr]

        return pathEdges

    def GetFrontier(self):
        pass

    def PushFrontier(self, frontier, point):
        pass

    def PopFrontier(self, frontier):
        pass

    def FrontierEmpty(self, frontier):
        pass

 
        
class BFS(Search):

    def GetFrontier(self):
        return []

    def PushFrontier(self, frontier, point):
        return frontier.append(point)
    
    def PopFrontier(self, frontier):
        return frontier.pop(0)
    
    def FrontierEmpty(self, frontier):
        return bool(frontier)
    
       
class DFS(Search):

    def GetFrontier(self):
        return []

    def PushFrontier(self, frontier, point):
        return frontier.append(point)
    
    def PopFrontier(self, frontier):
        return frontier.pop()
    
    def FrontierEmpty(self, frontier):
        return bool(frontier)
    

class AStar(Search):

    def GetFrontier(self):
        return PriorityQueue()

    def PushFrontier(self, frontier, point):
        return frontier.put((self.Heuristic(point, self.target), point))
    
    def PopFrontier(self, frontier):
        return frontier.get()[1]
    
    def FrontierEmpty(self, frontier : PriorityQueue):
        return not frontier.empty()

    def Heuristic(self, pt, target):
        return (pt[0] - target[0])**2 + (pt[1] - target[1])**2 
    

class BootyFirstSearch(Search):

    def __init__(self, graph):
        super().__init__(graph)

        self.bootyNumber = 0

    def GetFrontier(self):
        return []

    def PushFrontier(self, frontier, point):
        return frontier.append(point)
    
    def PopFrontier(self, frontier):
        self.bootyNumber = (self.bootyNumber+1)%6 
        try:
            return frontier.pop(-self.bootyNumber)
        except:
            return frontier.pop()
    
    def FrontierEmpty(self, frontier):
        return bool(frontier)