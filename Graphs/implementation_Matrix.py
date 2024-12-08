class Graph:

    def __init__(self, n):
        self.n = n
        self.adj_matrix = [[0] * (n + 1) for _ in range(n + 1)]  # Adjacency matrix initialization

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # Undirected graph

    def remove_edge(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

    def dfs(self, start):
        visited = [False] * (self.n + 1)
        print("DFS Traversal:", end=" ")
        self._dfs_recursive(start, visited)
        print()

    def _dfs_recursive(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        for neighbor in range(1, self.n + 1):  # Corrected the range to include all nodes
            if self.adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                self._dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        visited = [False] * (self.n + 1)
        stack = [start]
        dfs_list = []

        while stack:
            node = stack.pop()

            if not visited[node]:  # Fixed the incorrect function call
                dfs_list.append(node)
                visited[node] = True

                for neighbor in range(self.n, 0, -1):  # Traverse neighbors in reverse to match stack order
                    if self.adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                        stack.append(neighbor)
        return dfs_list

    def bfs(self, start):
        visited = [False] * (self.n + 1)
        queue = [start]
        visited[start] = True
        bfs_list = []

        while queue:
            node = queue.pop(0)  # Use pop(0) for BFS (queue behavior)

            bfs_list.append(node)
            for neighbor in range(1, self.n + 1):  # Corrected range
                if self.adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return bfs_list


if __name__ == '__main__':
    n = 5
    g = Graph(n)

    # Adding edges
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 2)
    g.add_edge(2, 4)
    g.add_edge(1, 4)
    g.add_edge(3, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 5)

    # Perform DFS and BFS
    g.dfs(5)
    print("DFS Iterative:", g.dfs_iterative(5))
    print("BFS Traversal:", g.bfs(5))
