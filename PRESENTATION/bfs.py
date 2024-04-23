import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bfs(graph, start, end):
    visited = set()
    queue = [(start, [start])]
    while queue:
        print("queue",queue)
        current_node, path = queue.pop(0)

        if current_node == end:
            return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

                    
                
            # print(debug)
def animate_path(graph, path):
    pos = nx.circular_layout(graph)
    
    def animate(i):
        ax.clear()
        nx.draw(graph, pos, with_labels=True, node_color='skyblue', ax=ax)
        nx.draw_networkx_nodes(graph, pos, nodelist=path[:i+1], node_color='green', ax=ax)
        nx.draw_networkx_edges(graph, pos, edgelist=[(path[j], path[j+1]) for j in range(i)], edge_color='green', ax=ax)
        plt.title(f"Step {i+1}: Path from {path[0]} to {path[-1]}")
    
    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, animate, frames=len(path), repeat=False)
    plt.show()

# Example usage:
G = nx.DiGraph()
# G.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 5), (4, 6), (6, 7)])

# G.add_edges_from([(0, 1), (1, 2),  (2, 0), (0, 3), (3, 4), (4, 0)])
G.add_edges_from([(0,1),(0,2),(0,3),(9,4),(9,5),(3,6),(2,6),(2,7),(3,8),(5,1),(0,9)])
start_node = 0
end_node = 1

# print(list(G.neighbors(1)))

path = bfs(G, start_node, end_node)
# path = []
# for edge in path_generator:
#     path += edge
# print(path)
print("Shortest path:", path)
animate_path(G, path)
