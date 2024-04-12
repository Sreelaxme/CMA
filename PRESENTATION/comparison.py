import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
def dfs_animation(graph, start, end):
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
def bfs_animation(graph, start, end):
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


if __name__ == "__main__":
    dfs_time = []
    bfs_time = []
    for i in range(0, 10):
        G = nx.complete_graph(i + 5)
        tbfs = bfs_animation(G, 0, i)
        tdfs = dfs_animation(G, 0, i)
        dfs_time.append(tdfs)
        bfs_time.append(tbfs)

    X = [i for i in range(5, 15)]
    print(X)
    print("dfs time ",dfs_time)
    print("bfs time ", bfs_time)
    plt.plot(X, dfs_time, label="DFS Time")
    plt.plot(X, bfs_time, label="BFS Time")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Time (milliseconds)")
    plt.title("Time Taken to Find Path Between 2 Nodes")
    plt.legend()
    plt.grid()
    plt.show()


