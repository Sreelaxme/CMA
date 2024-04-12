from collections import defaultdict,deque
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bfs(G, source , target):
    q = deque()
    q.append(source)
    visited = [source]
    path = []
    while q :

        curr = q.popleft()
        path.append(curr)
        print("keriii")
        if curr == target :
            break
        for neigh in G.neighbors(curr):

            if neigh not in visited:
                visited.append(neigh)
                q.append(neigh)
    # print(path)
    return path
def dfs(graph, start,target):
    visited = set()
    stack = [start]
    path = []
    while stack:
        current_node = stack.pop()
        print("kerii")
        path.append(current_node)
        if current_node == target:
            return
        if current_node not in visited:
            visited.add(current_node)
            print(current_node)  # Process the node (or do whatever you want)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return path
def visualize_graph_with_path(graph, path):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=700)
    nx.draw_networkx_nodes(graph, pos, nodelist=path, node_color='red', node_size=700)
    nx.draw_networkx_edges(graph, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], edge_color='red', width=2)
    plt.show()


if __name__ == "__main__":
    # graph = nx.Graph()
    # edge = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    # graph.add_edges_from(edge)
    # pos = nx.spring_layout(graph)
    # nx.draw_networkx(graph,pos)
    # path = dfs(graph, 1 ,3)

    # def update(frame):
    #     ax.clear()
    #     nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, ax=ax)
    #     if frame < len(path):
    #         nx.draw_networkx_nodes(G, pos, nodelist=path[:frame+1], node_color='red', node_size=700, ax=ax)
    #         nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(frame)], edge_color='red', width=2, ax=ax)

    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 9)])
    start_node = 1
    end_node = 9

    path = bfs(G, start_node, end_node)
    visualize_graph_with_path(G,path)
    # print(path)
    # if path:
    #     print("Path found:", path)

    #     fig, ax = plt.subplots()
    #     pos = nx.spring_layout(G)
    #     ani = FuncAnimation(fig, update, frames=len(path)+1, interval=1000, repeat=False)
    #     # plt.close()  # Prevents duplicate plots in Colab

    #     # HTML(ani.to_jshtml())
    #     # ani.save("hii.mp4",fps = 3)
    #     # Show animation
    #     plt.show()
    # else:
    #     print("No path found between nodes", start_node, "and", end_node)
