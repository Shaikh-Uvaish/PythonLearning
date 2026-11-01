from collections import deque

class GraphMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.locations = []

    def add_location(self, name):
        self.locations.append(name)

    def add_edge(self, src, dest):
        i = self.locations.index(src)
        j = self.locations.index(dest)
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1

    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.locations[v], end=" ")

        for i in range(self.vertices):
            if self.matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start):
        print("\nDFS Traversal (Adjacency Matrix):", end=" ")
        visited = [False] * self.vertices
        start_index = self.locations.index(start)
        self.dfs_util(start_index, visited)


class GraphList:
    def __init__(self):
        self.graph = {}

    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = []

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def bfs(self, start):
        print("\nBFS Traversal (Adjacency List):", end=" ")
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            location = queue.popleft()
            print(location, end=" ")

            for neighbor in self.graph[location]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


def main():
    locations = ['A', 'B', 'C', 'D', 'E']
    print("Locations:", locations)

    # Adjacency Matrix Graph
    g_matrix = GraphMatrix(len(locations))
    for loc in locations:
        g_matrix.add_location(loc)

    g_matrix.add_edge('A', 'B')
    g_matrix.add_edge('A', 'C')
    g_matrix.add_edge('B', 'D')
    g_matrix.add_edge('C', 'E')
    g_matrix.add_edge('D', 'E')

    # Adjacency List Graph
    g_list = GraphList()
    for loc in locations:
        g_list.add_location(loc)

    g_list.add_edge('A', 'B')
    g_list.add_edge('A', 'C')
    g_list.add_edge('B', 'D')
    g_list.add_edge('C', 'E')
    g_list.add_edge('D', 'E')

    source = 'A'
    print(f"\nStarting traversal from location: {source}")

    # Run DFS and BFS
    g_matrix.dfs(source)
    g_list.bfs(source)

    # Display matrices
    print("\n\nAdjacency Matrix:")
    for row in g_matrix.matrix:
        print(row)

    print("\nAdjacency List:")
    for key, value in g_list.graph.items():
        print(f"{key} -> {value}")


if __name__ == "__main__":
    main()
