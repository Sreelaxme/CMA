from queue import PriorityQueue

#  heuristic function similar to Euclidean distance
def heuristic(pt, target):
        return (pt[0] - target[0])**2 + (pt[1] - target[1])**2 
def astar(graph, start, target):

        start = start
        target = target
        frontier = PriorityQueue()
        # frontier with priority value and node
        frontier.put((0, start))
        expanded = set([start])
        path = []

        while not frontier.empty:

            curr = frontier.get()  # Queue  
            
            if curr == target:
                return path

            for node in graph.neighbours(curr):
                if node not in expanded:
                    expanded.add(node)
                    frontier.put((heuristic(node,target), node))