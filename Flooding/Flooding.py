import socket
import threading
import pickle

class FloodingNode:
    def __init__(self, port, neighbors):
        self.port = port
        self.neighbors = neighbors
        self.received_messages = set()

    def start(self):
        threading.Thread(target=self.listen_for_messages, daemon=True).start()

    def listen_for_messages(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(('localhost', self.port))
            print(f"Node listening on port {self.port}")

            while True:
                data, addr = s.recvfrom(1024)
                message = pickle.loads(data)
                self.handle_message(message)

    def handle_message(self, message):
        msg_id = message['id']
        ttl = message['ttl']

        if msg_id not in self.received_messages and ttl > 0:
            print(f"Node {self.port} received message: {message['data']}")
            self.received_messages.add(msg_id)
            message['ttl'] -= 1
            self.flood(message)

    def flood(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            for neighbor in self.neighbors:
                s.sendto(pickle.dumps(message), ('localhost', neighbor))
                print(f"Node {self.port} sent message to {neighbor}")

    def send_message(self, data, ttl=10):
        message = {'id': id(data), 'data': data, 'ttl': ttl}
        self.handle_message(message)

def configure_flooding_node():
    port = int(input("Ingrese el puerto en el que quiere escuchar: "))
    neighbors_input = input("Ingrese los puertos de los vecinos separados por comas (por ejemplo: 5002,5003): ")
    neighbors = [int(neighbor.strip()) for neighbor in neighbors_input.split(",")]

    node = FloodingNode(port, neighbors)
    node.start()

    while True:
        send = input("Desea enviar un mensaje? (s/n): ").strip().lower()
        if send == 's':
            message = input("Ingrese el mensaje a enviar: ")
            node.send_message(message)
        elif send == 'n':
            print("Nodo en modo escucha.")
        else:
            print("Opción no válida. Por favor ingrese 's' para enviar un mensaje o 'n' para continuar escuchando.")
