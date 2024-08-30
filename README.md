# RoutingAlgorithms
Este proyecto implementa tres algoritmos fundamentales de enrutamiento en redes de comunicación:

- Flooding
- Dijkstra
- Link State Routing (LSR)
Cada algoritmo está implementado de manera modular en Python, permitiendo su fácil ejecución y configuración.

## Requisitos
- Python 3.x
- (Opcional) virtualenv para crear un entorno virtual

## Ejecución de los Algoritmos
### Ejecutar el Algoritmo de Flooding
Para ejecutar el algoritmo de Flooding:
```bash
make flooding
```
O tambien:
```bash
python3 main.py flooding
```
Instrucciones

Selecciona el puerto y los vecinos:

El programa te pedirá que ingreses el puerto en el que el nodo debe escuchar y los puertos de los vecinos.

Enviar un mensaje:

Se te preguntará si deseas enviar un mensaje desde el nodo. Si eliges enviar un mensaje, este se propagará a los nodos vecinos.

Ejemplo de uso: 
```bash
Ingrese el puerto en el que quiere escuchar: 5001
Ingrese los puertos de los vecinos separados por comas: 5002,5003
Desea enviar un mensaje? (s/n): s
Ingrese el mensaje a enviar: Hello from node 5001
```
### Ejecutar el Algoritmo de Dijkstra
Para ejecutar el algoritmo de Dijkstra:
```bash
make dijkstra
```
O tambien:
```bash
python3 main.py dijkstra
```
Instrucciones

Configura la topología del grafo:

El programa te pedirá que ingreses los nodos y aristas, incluyendo los pesos de las aristas.

Selecciona el nodo inicial y final:

Se te pedirá que ingreses el nodo inicial y el nodo final para calcular el camino más corto.

Cálculo de rutas:

El programa calculará las distancias mínimas desde el nodo inicial a todos los demás nodos y mostrará el camino más corto al nodo final.

Ejemplo de uso:
```bash
Distancias desde el nodo de inicio:
Distancia a A: 0
Distancia a B: 1
Distancia a C: 3
Distancia a D: 4

Camino más corto desde A hasta D:
A -> B -> C -> D
```
### Ejecutar el Algoritmo de LSR

Para ejecutar el algoritmo de LSR:
```bash
make lsr
```
O tambien:
```bash
python3 main.py lsr
```
Instrucciones

Configuración del nodo:

Ingresa el nombre del nodo y los enlaces a sus vecinos, junto con los costos.

Envío y recepción de LSPs:

El usuario puede generar LSPs, recibir LSPs de otros nodos, y actualizar la base de datos de enlaces.

Cálculo de rutas:

El usuario puede ejecutar el algoritmo de Dijkstra utilizando la información de los LSPs para calcular las rutas óptimas.

Ejemplo de uso:

```bash
LSP generado: {'sender': 'A', 'links': {'B': 1, 'C': 4}}

Distancias calculadas desde el nodo actual:
Distancia a A: 0
Distancia a B: 1
Distancia a C: 4
```
### Limpieza 

Para limpiar los archivos temporales puedes usar: 

```bash
make clean
```

## Contribuciones

Para contribuir al proyecto, realiza un fork del repositorio, realiza tus cambios y envía un pull request. Las contribuciones son bienvenidas para mejorar y expandir este proyecto.
