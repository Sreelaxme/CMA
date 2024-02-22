import networkx as nx
import matplotlib.pyplot as plt
import random

class Lattice:
  def __init__(self, n):
    # Create a 5x5 grid graph without any edges
    self.grid = nx.Graph()
    self.n = n

    # Add nodes to the graph
    for i in range(n):
        for j in range(n):
            self.grid.add_node((i, j))


  def show(self):
    pos = {(x,y):(y,-x) for x,y in self.grid.nodes()}

    nx.draw(self.grid,pos, node_size = 0.1)

  def percolate(self, p):
     for node in self.grid.nodes():
        x, y = node
        # Check right neighbor
        if x < self.n-1:
            if random.random() < p:
                self.grid.add_edge(node, (x+1, y))
        # Check bottom neighbor
        if y < self.n-1:
            if random.random() < p:
                self.grid.add_edge(node, (x, y+1))
     pos = {(x,y):(y,-x) for x,y in self.grid.nodes()}

  def showPaths(self):
    edge_colors = {}
    for i in range(self.n):
    #   path = nx.dfs_edges(self.grid, source=(0,i), depth_limit=self.n)
    # Calculate shortest path lengths from the source node
      # shortest_path_lengths = nx.single_source_shortest_path_length(self.grid, (0,i))

      # # Find the node(s) at maximum depth
      # max_depth = max(shortest_path_lengths.values())
      reachable_nodes = nx.descendants(self.grid, (0,i))
      max_x = max((node[0] for node in reachable_nodes), default=0)  # Get the maximum x-coordinate with default
      max_depth_nodes = [node for node in reachable_nodes if node[0] == max_x]  # Find nodes with max x
      # print(max_depth_nodes)
      path = list()
      for node in max_depth_nodes:
          path1 = nx.shortest_path(self.grid, (0,i), node)
          # print(path)
          if(len(path) == 0 or len(path1)<len(path)):
            path = path1
          # Color the edges along the shortest path
      for u, v in zip(path[:-1], path[1:]):
          edge_colors[(u, v)] = 'green'
    pos = {(x,y):(y,-x) for x,y in self.grid.nodes()}

    nx.draw(self.grid,  pos, node_size = 0.1,edge_color=[edge_colors.get(e, 'red') for e in self.grid.edges()])

  def existsTopDownPath(self):
    # Check if a path exists between any node in the top layer and any node in the bottom layer
    top_layer_nodes = [(i, 0) for i in range(self.n)]
    bottom_layer_nodes = [(i, self.n-1) for i in range(self.n)]

    for top_node in top_layer_nodes:
        for bottom_node in bottom_layer_nodes:
            if nx.has_path(self.grid, top_node, bottom_node):
                return True
    return False