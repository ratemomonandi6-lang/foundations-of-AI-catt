@@ -0,0 +1,85 @@
class Graph:
    def __init__(self):
        self.graph = {}

    # Method to add edges
    def add_edge(self, node, neighbor):

        # Create node if not present
        if node not in self.graph:
            self.graph[node] = []

        # Add neighbor
        self.graph[node].append(neighbor)

    def dfs(self, start, goal):

        # Stack for DFS
        stack = [start]

        # Visited nodes
        visited = []

        # Parent tracking
        parent = {}
        parent[start] = None

        print("=== Depth First Search Traversal ===")

        while stack:

            # Remove last item (LIFO)
            current = stack.pop()

            if current not in visited:

                print("Visited Node:", current)

                visited.append(current)

                # Goal test
                if current == goal:
                    print("\nGoal Node Found!")
                    break

                # Add neighbors
                for neighbor in reversed(self.graph[current]):

                    if neighbor not in visited:

                        stack.append(neighbor)

                        if neighbor not in parent:
                            parent[neighbor] = current

        # Reconstruct path
        path = []

        node = goal

        while node is not None:
            path.append(node)
            node = parent[node]

        path.reverse()

        print("\n=== Path to Goal ===")
        print(" -> ".join(path))


# Create graph object
g = Graph()

# Add edges
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')

# Nodes without children
g.graph['D'] = []
g.graph['E'] = []
g.graph['F'] = []

g.dfs('A', 'F')