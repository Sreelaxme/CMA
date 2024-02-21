from Qn1 import UndirectedGraph 
import random

class ERRandomGraph(UndirectedGraph):
    def generateGraph(self):
        for i in range (1,len(self.graph)+1):
            for j in range(i+1,len(self.graph)+1):
                if random.random() < self.probability:
                    self.addEdge(i,j)

    def sample(self,probability):
        self.probability = probability
        self.generateGraph()
    

if __name__ == "__main__":
    g = ERRandomGraph(100)
    g.sample(0.7)
    g.plotDegDist()
