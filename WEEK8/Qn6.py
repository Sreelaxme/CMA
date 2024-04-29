import matplotlib.pyplot as plt
import networkx as nx
from directed import DirectedGraph
import numpy as np
import random

def pagerank(G:DirectedGraph, d=0.85, max_iter=100, tol=1.0e-6):
    n = len(G.graph)
    A = np.zeros((n, n))

    # Construct the adjacency matrix
    for i in range(1, n + 1):
        for j in G.graph[i]:
            A[j - 1, i - 1] = 1 / len(G.graph[i])

    # Initialize PageRank vector
    p = np.ones(n) / n

    # Damping factor
    beta = 1 - d

    for _ in range(max_iter):
        p_next = d * np.dot(A, p) + beta / n
        if np.linalg.norm(p_next - p, ord=1) < tol:
            break
        p = p_next

    return p

DirectedGraph.pagerank = pagerank

def plot_graph_with_pagerank(P:DirectedGraph,d):
        G = nx.DiGraph()

        pagerank_scores = P.pagerank(d)
        # print(P.n)
        node_size = [pagerank_scores[node] * 20000 for node in range( P.n )]

        for node, neighbors in P.graph.items():
            if not neighbors:
                G.add_node(node)
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        # print(len(G.graph))
        pos = nx.spring_layout(G)
        print((list(G)))
        print(len(node_size))
        nx.draw_networkx(G, pos, with_labels=True, node_size=node_size,node_color='skyblue')
        plt.show()
DirectedGraph.plot_graph_with_pagerank = plot_graph_with_pagerank
if __name__ == "__main__":
    p = 0.05; n = 25
    g = DirectedGraph(n)
    for i in range(n):
        for j in range(n):
            if i != j and random.random() <= p:
                g.addEdge(i+1, j+1)
    print(g)
    pt = g.pagerank(0.85)
    # print(type(pt))
    # print(pt.size)
    g.plot_graph_with_pagerank(0.85)