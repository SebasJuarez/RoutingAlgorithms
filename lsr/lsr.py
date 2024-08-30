from Dijkstra.graph import Graph
from Dijkstra.Dijkstra import dijkstra

class Node:
    def __init__(self, name):
        self.name = name
        self.graph = Graph()
        self.lsp_database = {}

    def add_link(self, neighbor, cost):
        self.graph.add_edge(self.name, neighbor, cost)
        self.lsp_database[self.name] = self.graph.edges[self.name]

    def receive_lsp(self, lsp):
        sender = lsp['sender']
        self.lsp_database[sender] = lsp['links']
        for node, links in self.lsp_database.items():
            for neighbor, cost in links.items():
                self.graph.add_edge(node, neighbor, cost)

    def generate_lsp(self):
        return {'sender': self.name, 'links': self.graph.edges[self.name]}

    def run_dijkstra(self, start_node=None):
        if start_node is None:
            start_node = self.name
        distances, shortest_path = dijkstra(self.graph, start_node)
        return distances, shortest_path
