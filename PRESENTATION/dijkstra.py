import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    
    predecessors = {}
    
    priority_queue = [(start, 0)]
    
    while priority_queue:
        current_node, current_distance = priority_queue.pop(0)
        
        if current_node == end:
            break
        
        for neighbor in graph.neighbors(current_node):
            new_distance = current_distance + graph[current_node][neighbor].get('weight', 1)
            
            # If the new distance is shorter than the current distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                priority_queue.append((neighbor, new_distance))
                priority_queue.sort(key=lambda x: x[1])
    
    # If we reached the end node, reconstruct the path
    if end in predecessors:
        path = []
        current_node = end
        while current_node != start:
            path.insert(0, current_node)
            current_node = predecessors[current_node]
        path.insert(0, start)
        return path, distances[end]
    else:
        # No path found
        return None, float('inf')




def animate_path(graph, path):
    pos = nx.circular_layout(graph)
    
    def animate(i):
        ax.clear()
        nx.draw(graph, pos, with_labels=True, node_color='skyblue', ax=ax)
        nx.draw_networkx_nodes(graph, pos, nodelist=path[:i+1], node_color='green', ax=ax)
        nx.draw_networkx_edges(graph, pos, edgelist=[(path[j], path[j+1]) for j in range(i)], edge_color='green', ax=ax)
        edge_labels = nx.get_edge_attributes(G,"weight")
        nx.draw_networkx_edge_labels(G,pos,edge_labels)
        plt.title(f"Step {i+1}: Path from {path[0]} to {path[-1]}")
    
    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, animate, frames=len(path), repeat=False)
    plt.show()
# Example usage:
# G = nx.DiGraph()
# G.add_weighted_edges_from([(1, 2, 1), (1, 3, 4), (3, 2, 1), (2, 4, 3), (3, 4, 1)])

# start_node = 1
# end_node = 4
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4, 5, 6])
G.add_weighted_edges_from([(1, 2, 6), (1, 4, 1), (2, 3, 5),
                           (2, 4, 2), (2, 5, 2), (3, 5, 5),
                           (3, 6, 5), (4, 5, 1), (5, 6, 6),(1,6,20)])
start_node = 1
end_node = 6
path, distance = dijkstra(G, start_node, end_node)
print("Shortest path:", path)
print("Distance:", distance)

animate_path(G, path)
