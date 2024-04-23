from grid import Grid

class Search:

    def __init__(self, graph : Grid):
        self.graph = graph

    def RunSearch(self, start, target):
        pass
        # Override

    # Get list of directions (unit vectors) to follow 
    # To navigate to target 
    def GetPathEdges(self) -> list[tuple[int,int]]:
        return []
        # Override

    # Get list of cells in the path to target
    def GetPathNodes(self) -> list[tuple[int,int]]:
        return []
        # Override

    
class BFS:

    def __init__(self, graph : Grid):

        self.graph = graph
        self.pathTree = {}
        self.nodeTree = {}

        self.targetFound = False

    
    def RunSearch(self, start, target):

        self.start = start
        self.target = target
        self.targetFound = False

        frontier = [start]
        expanded = set([start])
        self.nodeTree[start] = None
        self.pathTree[start] = None

        while len(frontier) > 0:

            curr = frontier.pop(0)  # Queue  
            
            if curr == target:
                self.targetFound = True
                return

            for d,node in self.graph.GetNeighbors(curr).items():
                if node not in expanded:
                    self.pathTree[node] = d
                    self.nodeTree[node] = curr
                    expanded.add(node)
                    frontier.append(node)


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



    



