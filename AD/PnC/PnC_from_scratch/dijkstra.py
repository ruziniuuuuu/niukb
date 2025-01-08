from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph # a dict for the adjacency list

    def add_edges(self, node_1, node_2, weight):
        if node_1 not in self.graph:
            self.graph[node_1] = {}
        self.graph[node_1][node_2] = weight

    def shortest_distances(self, source: str):
        # initialize the distances of all nodes to infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0

        # Init a priority queue
        pq = [(0, source)]
        heapify(pq)

        # Create a set to hold visited nodes
        visited = set()

        while pq:  # while the pq is not empty
            curr_dist, curr_node = heappop(pq)

            if curr_node in visited:
                continue
            visited.add(curr_node)

            for neighbor, weight in self.graph[curr_node].items():
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heappush(pq, (new_dist, neighbor))

if __name__ == '__main__':
    graph = {
        "A": {"B": 3, "C": 3},
        "B": {"A": 3, "D": 3.5, "E": 2.8},
        "C": {"A": 3, "E": 2.8, "F": 3.5},
        "D": {"B": 3.5, "E": 3.1, "G": 10},
        "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
        "F": {"G": 2.5, "C": 3.5},
        "G": {"F": 2.5, "E": 7, "D": 10},
    }

    G = Graph(graph)

    print(G.graph)

    pq = [(3, "A"), (1, "C"), (7, "D")]
    # Convert into a queue object
    heapify(pq)
    # Return the highest pq
    heappop(pq)
    # heappush
    heappush(pq, (0, "B"))
    heappop(pq)