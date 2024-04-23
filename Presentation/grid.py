class Grid:

    def __init__(self):
        self.posToObj = {}
        self.objToPos = {}

    # grid[(x,y)] = obj
    # Sets obj at position (x,y) of grid
    def __setitem__(self, index : tuple[int,int], item):     
        if item == None:
            del self.objToPos[self.posToObj[index]]
            del self.posToObj[index]
            return

        self.posToObj[index] = item
        self.objToPos[item] = index

    # grid[(x,y)] gets the object at this position
    def __getitem__(self, index : tuple[int,int]):
        if index not in self.posToObj:
            return None
        return self.posToObj[index]
    
    # Get all neighboring cells that aren't occupied
    def GetNeighbors(self, index):
        edges = {}
        for d in [(1,0), (0,1), (-1,0), (0,-1)]:
            newPos = (index[0] + d[0], index[1] + d[1])
            if newPos not in self.posToObj:
                edges[d] = newPos
        
        return edges
        