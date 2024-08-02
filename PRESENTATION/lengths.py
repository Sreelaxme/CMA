import networkx as nx
import matplotlib.pyplot as plt
import random
import time

def dfs(graph, start, end):
    visited = set()
    stack = [(start, [start])]
    start_time = time.time()  # Record the start time

    while stack:
        current_node, path = stack.pop()
        if current_node == end:
            return path, (time.time() - start_time) * 1000  # Return the path and the time taken

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return  [], (time.time() - start_time) * 1000


def bfs(graph, start, end):
    visited = set()
    queue = [(start, [start])]
    start_time = time.time()  # Record the start time

    while queue:
        current_node, path = queue.pop(0)
        if current_node == end:
            return path, (time.time() - start_time) * 1000  # Return the path and the time taken

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return  [], (time.time() - start_time) * 1000
def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    start_time = time.time()
    predecessors = {}
    priority_queue = [(start, 0)]

    while priority_queue:
        current_node, current_distance = priority_queue.pop(0)
        if current_node == end:
            break

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor].get('weight', 1)
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                priority_queue.append((neighbor, new_distance))
                priority_queue.sort(key=lambda x: x[1])

    if end in predecessors:
        path = []
        current_node = end
        total_weight = 0
        while current_node != start:
            path.insert(0, current_node)
            total_weight += graph[predecessors[current_node]][current_node].get('weight', 1)
            current_node = predecessors[current_node]
        path.insert(0, start)
        return path, (time.time() - start_time) * 1000, len(path) - 1, total_weight
    else:
        return None, (time.time() - start_time) * 1000, float('inf'), float('inf')

if __name__ == "__main__":
    dfs_lengths = []
    dfs_weights = []
    bfs_lengths = []
    bfs_weights = []
    dij_lengths = []
    dij_weights = []
    dfs_times = []
    bfs_times = []
    dij_times = []
    X = []
    
    def generate_random_graph(nodes, edges):
        G = nx.gnm_random_graph(nodes, edges)
        for u, v in G.edges():
            G[u][v]['weight'] = random.randint(1, 10)  # Assign random weights
        return G

    graphs = []
    for i in range(100, 200):
        G = nx.complete_graph(i)
        graphs.append(G)
        # X.append(i+5)
    # for i in range(100, 200):
    #     # num_nodes = random.randint(i, i+5)
    #     num_nodes = i
    #     num_edges = random.randint(num_nodes - 1, num_nodes * (num_nodes - 1) // 2)
    #     graph = generate_random_graph(num_nodes, num_edges)
    #     graphs.append(graph)

    for graph in graphs:
        start_node = random.choice(list(graph.nodes()))
        end_node = random.choice(list(graph.nodes()))
        X.append(len(graph.nodes()))

        dfs_path, dfs_time = dfs(graph, start_node, end_node)
        dfs_lengths.append(len(dfs_path) - 1)
        dfs_weights.append(sum(graph[u][v].get('weight', 1) for u, v in zip(dfs_path[:-1], dfs_path[1:])))
        dfs_times.append(dfs_time)

        bfs_path, bfs_time = bfs(graph, start_node, end_node)
        bfs_lengths.append(len(bfs_path) - 1)
        bfs_weights.append(sum(graph[u][v].get('weight', 1) for u, v in zip(bfs_path[:-1], bfs_path[1:])))
        bfs_times.append(bfs_time)

        dij_path, dij_time, dij_length, dij_weight = dijkstra(graph, start_node, end_node)
        dij_lengths.append(dij_length)
        dij_weights.append(dij_weight)
        dij_times.append(dij_time)

    # print("DFS lengths:", dfs_lengths)
    # print("DFS weights:", dfs_weights)
    # print("BFS lengths:", bfs_lengths)
    # print("BFS weights:", bfs_weights)
    # print("Dijkstra lengths:", dij_lengths)
    # print("Dijkstra weights:", dij_weights)

    plt.plot(X, dfs_times, label="DFS Time")
    plt.plot(X, bfs_times, label="BFS Time")
    plt.plot(X, dij_times, label="Dijkstra Time")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Path Length")
    plt.title("Time Comparison")
    plt.legend()
    plt.grid()
    plt.show()

    # plt.plot(X, dfs_lengths, label="DFS Path Length")
    # plt.plot(X, bfs_lengths, label="BFS Path Length")
    # plt.plot(X, dij_lengths, label="Dijkstra Path Length")
    # plt.xlabel("Number of Nodes")
    # plt.ylabel("Path Length")
    # plt.title("Path Length Comparison")
    # plt.legend()
    # plt.grid()
    # plt.show()

    # plt.plot(X, dfs_weights, label="DFS Path Weight")
    # plt.plot(X, bfs_weights, label="BFS Path Weight")
    # plt.plot(X, dij_weights, label="Dijkstra Path Weight")
    # plt.xlabel("Number of Nodes")
    # plt.ylabel("Path Weight")
    # plt.title("Path Weight Comparison")
    # plt.legend()
    # plt.grid()
    # plt.show()
