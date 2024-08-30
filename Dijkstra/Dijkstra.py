import heapq
from .graph import Graph

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    shortest_path = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path[neighbor] = current_node

    return distances, shortest_path

def configure_dijkstra_graph():
    graph = Graph()
    print("Configuración del grafo para Dijkstra:")
    
    while True:
        node = input("Ingrese un nodo (o 'fin' para terminar de agregar nodos): ").strip()
        if node.lower() == 'fin':
            break
        graph.add_node(node)
    
    while True:
        from_node = input("Ingrese el nodo de origen de la arista (o 'fin' para terminar de agregar aristas): ").strip()
        if from_node.lower() == 'fin':
            break
        to_node = input(f"Ingrese el nodo de destino para la arista desde {from_node}: ").strip()
        weight = float(input(f"Ingrese el peso de la arista desde {from_node} hasta {to_node}: "))
        graph.add_edge(from_node, to_node, weight)

    start_node = input("Ingrese el nodo inicial para Dijkstra: ").strip()

    return graph, start_node

def reconstruct_path(shortest_path, start, end):
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = shortest_path.get(current_node, None)
        if current_node is None:
            return None
    path.append(start)
    path.reverse()
    return path
