import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random 
def dfs(graph, start, end):
    visited = set()
    stack = [(start, [start])]
    start_time = time.time()  # Record the start time

    pos = nx.spring_layout(graph)

    while stack:
        current_node, path = stack.pop()
        if current_node == end:
            return  (time.time() - start_time)*(10**3)  # Return the path and the time taken

            # return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

                    # Highlight the edge being explored
                    # yield path + [neighbor]
def bfs(graph, start, end):
    visited = set()
    queue = [(start, [start])]
    pos = nx.spring_layout(graph)
    start_time = time.time()  # Record the start time

    while queue:
        current_node, path = queue.pop(0)
        if current_node == end:
            return (time.time() - start_time)*(10**3)  # Return the path and the time taken


        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.neighbors(current_node):
                # debug+=str(neighbor)
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))





def dijkstra(graph, start, end):
    # Initialize distances dictionary with infinite distance for all nodes
    distances = {node: float('inf') for node in graph.nodes()}
    # Initialize the distance to the start node as 0
    distances[start] = 0
    start_time = time.time()
    # Initialize empty dictionary to store predecessors
    predecessors = {}
    
    # Initialize priority queue with start node and its distance
    priority_queue = [(start, 0)]
    
    while priority_queue:
        # Pop the node with the smallest distance from the priority queue
        current_node, current_distance = priority_queue.pop(0)
        
        # Stop if we reached the end node
        if current_node == end:
            break
        
        # Iterate over neighbors of the current node
        for neighbor in graph.neighbors(current_node):
            # Calculate the new distance to the neighbor
            new_distance = current_distance + graph[current_node][neighbor].get('weight', 1)
            
            # If the new distance is shorter than the current distance
            if new_distance < distances[neighbor]:
                # Update the distance to the neighbor
                distances[neighbor] = new_distance
                # Update the predecessor of the neighbor
                predecessors[neighbor] = current_node
                # Add the neighbor and its distance to the priority queue
                priority_queue.append((neighbor, new_distance))
                # Sort the priority queue based on distances
                priority_queue.sort(key=lambda x: x[1])
    
    # If we reached the end node, reconstruct the path
    if end in predecessors:
        path = []
        current_node = end
        while current_node != start:
            path.insert(0, current_node)
            current_node = predecessors[current_node]
        path.insert(0, start)
        return (time.time() - start_time)*(10**3)
        # return path, distances[end]
    else:
        # No path found
        return float('inf')

    
if __name__ == "__main__":
    dfs_time = []
    bfs_time = []
    dij_time = []
    X = []
        # Function to generate a random graph
    def generate_random_graph(nodes, edges):
        G = nx.gnm_random_graph(nodes, edges)
        return G

    # Generate 10 random graphs with different number of nodes and edges
    graphs = []
    for i in range(200,300):
        # num_nodes = random.randint(i, i+5)
        num_nodes = i
        num_edges = random.randint(num_nodes - 1, num_nodes * (num_nodes - 1) // 2)
        X.append(num_nodes)
        graph = generate_random_graph(num_nodes, num_edges)
        graphs.append(graph)

    # Run algorithms on each graph
    for graph in graphs:
        # Example start and end nodes
        start_node = random.choice(list(graph.nodes()))
        end_node = random.choice(list(graph.nodes()))

        # Run DFS
        dfs_t = dfs(graph, start_node, end_node)
        dfs_time.append(dfs_t)

        # Run BFS
        bfs_t = bfs(graph, start_node, end_node)
        bfs_time.append(bfs_t)

        tdij = dijkstra(graph,start_node,end_node)
        dij_time.append(tdij)


    # for i in range(0, 10):
    #     G = nx.complete_graph(i + 5)
    #     tbfs = bfs(G, 0, i)
    #     tdfs = dfs(G, 0, i)
    #     tdij = dijkstra(G,0,i)
    #     dfs_time.append(tdfs)
    #     bfs_time.append(tbfs)
    #     dij_time.append(tdij)
    # Create a sample graph
   
    # X = [i for i in range(1, 101)]
    print(X)
    print("dfs time ",dfs_time)
    print("bfs time ", bfs_time)
    print("Dij time ", dij_time)
    plt.plot(X, dfs_time, label="DFS Time")
    plt.plot(X, bfs_time, label="BFS Time")
    plt.plot(X,dij_time,label = "Dijkstras Time")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Time (milliseconds)")
    plt.title("Time for different algorithms")
    plt.legend()
    plt.grid()
    plt.show()
