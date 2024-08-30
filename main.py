import sys
from Dijkstra.Dijkstra import dijkstra, reconstruct_path, configure_dijkstra_graph
from Flooding.Flooding import configure_flooding_node
from lsr.lsr import Node

def run_dijkstra():
    graph, start_node = configure_dijkstra_graph()
    end_node = input("Ingrese el nodo final para calcular el camino más corto: ").strip()
    
    distances, shortest_path = dijkstra(graph, start_node)
    
    print("Distancias desde el nodo de inicio:")
    for node, distance in distances.items():
        print(f"Distancia a {node}: {distance}")
    
    path = reconstruct_path(shortest_path, start_node, end_node)
    print("Camino más corto desde", start_node, "hasta", end_node, ":")
    if path:
        print(" -> ".join(path))
    else:
        print("No existe un camino desde", start_node, "hasta", end_node)

def run_flooding():
    configure_flooding_node()

def run_lsr():
    print("Configuración del nodo para Link State Routing:")
    node_name = input("Ingrese el nombre del nodo (por ejemplo, 'A'): ").strip()
    node = Node(node_name)

    while True:
        neighbor = input("Ingrese un nodo vecino (o 'fin' para terminar de agregar enlaces): ").strip()
        if neighbor.lower() == 'fin':
            break
        cost = float(input(f"Ingrese el costo del enlace hacia {neighbor}: "))
        node.add_link(neighbor, cost)

    print("\nConfiguración de enlaces completa. Ahora puede recibir LSPs de otros nodos.")
    
    while True:
        command = input("\nComando (enviar_lsp, recibir_lsp, dijkstra, fin): ").strip().lower()
        if command == 'enviar_lsp':
            lsp = node.generate_lsp()
            print(f"LSP generado: {lsp}")
        elif command == 'recibir_lsp':
            lsp_input = input("Ingrese el LSP recibido (formato: {'sender': 'A', 'links': {'B': 1, 'C': 4}}): ")
            lsp = eval(lsp_input)
            node.receive_lsp(lsp)
            print("LSP recibido y grafo actualizado.")
        elif command == 'dijkstra':
            distances, shortest_path = node.run_dijkstra()
            print("Distancias calculadas desde el nodo actual:")
            for node_name, distance in distances.items():
                print(f"Distancia a {node_name}: {distance}")
        elif command == 'fin':
            break
        else:
            print("Comando no reconocido. Por favor, intente nuevamente.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py [dijkstra|flooding|lsr]")
        sys.exit(1)

    algorithm = sys.argv[1]

    if algorithm == "dijkstra":
        run_dijkstra()
    elif algorithm == "flooding":
        run_flooding()
    elif algorithm == "lsr":
        run_lsr()
    else:
        print("Algoritmo no reconocido. Usa 'dijkstra', 'flooding' o 'lsr'.")
