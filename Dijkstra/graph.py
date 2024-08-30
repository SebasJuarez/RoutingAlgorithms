class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.add_node(from_node)
        if to_node not in self.edges:
            self.add_node(to_node)
        self.edges[from_node][to_node] = weight
