.PHONY: all dijkstra flooding lsr clean

all: dijkstra flooding lsr

dijkstra:
	@echo "Ejecutando Dijkstra..."
	python3 main.py dijkstra

flooding:
	@echo "Ejecutando Flooding..."
	python3 main.py flooding

lsr:
	@echo "Ejecutando Link State Routing..."
	python3 main.py lsr

clean:
	@echo "Limpiando..."
	rm -rf __pycache__
