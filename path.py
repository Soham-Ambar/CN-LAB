class NetworkRouting:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, source, destination):
        visited = set()
        distances = {node: float('inf') for node in self.graph}
        distances[source] = 0
        predecessors = {}

        while len(visited) < len(self.graph):
            current_node = None
            min_distance = float('inf')

            for node in self.graph:
                if distances[node] < min_distance and node not in visited:
                    min_distance = distances[node]
                    current_node = node

            if current_node is None:
                break

            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                if distances[current_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current_node] + weight
                    predecessors[neighbor] = current_node

        path = []
        current_node = destination
        while current_node != source:
            if current_node not in predecessors:
                return None  # Path not found
            path.insert(0, current_node)
            current_node = predecessors[current_node]
        path.insert(0, source)
        return path

class AODV(NetworkRouting):
    def __init__(self, graph):
        super().__init__(graph)
        self.route_table = {}

    def discover_route(self, source, destination):
        if source not in self.route_table:
            self.route_table[source] = {}
        if destination not in self.route_table[source]:
            shortest_path = self.shortest_path(source, destination)
            if shortest_path:
                self.route_table[source][destination] = shortest_path
            else:
                return None
        return self.route_table[source][destination]

if __name__ == "__main__":
    graph = {
        "A": {"B": 1, "C": 2},
        "B": {"A": 1, "C": 1, "D": 3},
        "C": {"A": 2, "B": 1, "D": 1, "E": 4},
        "D": {"B": 3, "C": 1, "E": 1},
        "E": {"C": 4, "D": 1},
        "F": {"E": 2, "D": 3},
        "G": {"F": 1, "E": 2}
    }

    shortest_path_routing = NetworkRouting(graph)
    aodv_routing = AODV(graph)

    start_node = input("Enter the starting node: ")
    end_node = input("Enter the ending node: ")

    print(f"Shortest path from {start_node} to {end_node}:",
          shortest_path_routing.shortest_path(start_node, end_node))

    print(f"Route discovered by AODV from {start_node} to {end_node}:",
          aodv_routing.discover_route(start_node, end_node))

