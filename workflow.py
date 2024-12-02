# workflow.py

class Workflow:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, name, node):
        self.nodes[name] = node
        if name not in self.edges:
            self.edges[name] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            self.edges[from_node].append(to_node)
        else:
            raise ValueError("Both nodes must exist in the workflow.")

    def run(self, inputs):
        outputs = inputs
        visited = set()
        queue = []

        # Find all starting nodes (nodes with no incoming edges)
        incoming = {node for targets in self.edges.values() for node in targets}
        starting_nodes = [node for node in self.nodes if node not in incoming]

        queue.extend(starting_nodes)

        while queue:
            current = queue.pop(0)
            node = self.nodes[current]
            outputs = node.run(outputs)
            visited.add(current)
            for neighbor in self.edges.get(current, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

        return outputs
