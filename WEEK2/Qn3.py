from Qn1 import UndirectedGraph
from Qn2 import ERRandomGraph
import matplotlib.pyplot as plt
import random
import math
def isConnected(graph:UndirectedGraph):
    frontier = [list(graph.graph.keys())[0]]
    expanded = []

    #BFS
    while len(frontier) > 0:
        curr = frontier.pop(0)
        expanded.append(curr)
        frontier += [neigh for neigh in graph.graph[curr] if ((neigh not in expanded) and (neigh not in frontier))]

    return len(expanded) == len(graph.graph)

UndirectedGraph.isConnected = isConnected

if __name__ == "__main__":
    numSamples = 100
    graphSize = 100
    resolution = 100

    P = [i/resolution for i in range(resolution)]
    connectedFraction = []

    for p in P:
        numConnectedSamples = 0
        # print(p)
        for i in range(numSamples):
            g = ERRandomGraph(graphSize)
            g.sample(p)
            # print(g)

            if g.isConnected():
                numConnectedSamples += 1

        connectedFraction.append(numConnectedSamples/numSamples)


    # plt.plot(P, connectedFraction)
    # plt.axvline(x=math.log(graphSize)/graphSize, c='r', label="Avg. Node Degree")
    # plt.show()

    plt.plot(P[:int(resolution*0.1)], connectedFraction[:int(resolution*0.1)])
    plt.axvline(x=math.log(graphSize)/graphSize, c='r', label="Avg. Node Degree")
    plt.grid()
    plt.show()