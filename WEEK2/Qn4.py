from Qn1 import UndirectedGraph
from Qn2 import ERRandomGraph

import matplotlib.pyplot as plt
import random
import math
import queue

# def oneTwoComponentSizes(graph:UndirectedGraph):
#     componentSizes = []
#     nodes= list(graph.graph.keys())
#     frontier = [nodes.pop(0)]
#     expanded = []

#     #BFS
#     componentSize = 0
#     while len(frontier) > 0:
#         curr = frontier.pop(0)
#         componentSize += 1
#         expanded.append(curr)
#         frontier += [neigh for neigh in graph.graph[curr] if ((neigh not in expanded) and (neigh not in frontier))]
#         try:
#             nodes.remove(curr)
#         except:
#             pass
#         if len(frontier) == 0 and len(nodes)>0:
#             componentSizes.append(componentSize)
#             componentSize = 0
#             frontier = [nodes.pop()]

#     if len(componentSizes) == 0:
#         return [componentSize,0]
    
#     return sorted(componentSizes + [componentSize],reverse = True)[:2]
def oneTwoComponentSizes(graph:UndirectedGraph):
    vertices = set(graph.graph.keys())  # Adjusted range to include all vertices

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

          for neighbor in graph.graph[node]:  # Assuming self.graph is an adjacency list
              if neighbor not in visited:
                  q.put(neighbor)
      if count>components[0]:
        components[1] = components[0]
        components[0] = count
      elif count > components[1]:
        components[1] = count

    return components

UndirectedGraph.oneTwoComponentSizes = oneTwoComponentSizes

def TestLargestCC(n=1000):
    f = ERRandomGraph(n)
    runs = 50
    xPts = 100
    y1 = [0 for i in range(xPts)] #sizes of the largest connected components
    y2 = [0 for i in range(xPts)] #sizes of the second largest connected components
    x = []
    for i in range(0,xPts):
        p = i/(xPts*100)
        x.append(p)
        for j in range(0,runs):
            f.sample(p)
            s1,s2 = f.oneTwoComponentSizes()
            y1[i] += s1
            y2[i] += s2
        y1[i] /= runs
        y2[i] /= runs
    threshold = math.log(n)/n
    LargestCCThreshold = 0.001
    plt.plot(x,y1, color = "r")
    plt.plot(x,y2, color = "b")
    plt.axvline(x=threshold, color = "y", label = "Theoretical threshold")
    plt.axvline(x=LargestCCThreshold, color = "g", label = "Theoretical threshold")
    plt.xlabel("p")
    plt.ylabel("Fraction of nodes")
    plt.title("Fraction of nodes in the largest and second-largest\n connected components (CC) of G(1000, p) as function of p")
    plt.legend()
    plt.grid()
    plt.show()
if __name__ == '__main__':
    g = UndirectedGraph()
    g = g + (1, 2)
    g = g + (3, 4)
    g = g + (6, 4)
    print(g.oneTwoComponentSizes())

    g = ERRandomGraph(100)
    g.sample(0.01)
    print(g.oneTwoComponentSizes())

    TestLargestCC()
