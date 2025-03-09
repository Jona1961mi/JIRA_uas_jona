import heapq  # Importamos heapq para usar una cola de prioridad (min-heap)

def heuristica(a, b):
    """Calcula la distancia Manhattan entre dos puntos."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Diferencia en X + Diferencia en Y

def a_star_ms(inicio, objetivo, mapa):
    """Algoritmo A* con límite de memoria para encontrar el camino más corto."""
    
    # Lista de nodos abiertos (frontera de búsqueda), usamos una cola de prioridad.
    # Cada nodo es una tupla (costo estimado f(n), posición)
    abiertos = [(0, inicio)]  
    
    # Diccionario para almacenar el nodo padre de cada nodo, necesario para reconstruir el camino
    padres = {inicio: None}

    # Bucle principal: Mientras haya nodos en la lista de abiertos
    while abiertos:
        # Extraemos el nodo con menor costo f(n) de la cola de prioridad
        _, actual = heapq.heappop(abiertos)

        # Si hemos alcanzado el objetivo, reconstruimos el camino
        if actual == objetivo:
            camino = []
            while actual:
                camino.append(actual)  # Añadimos cada nodo al camino
                actual = padres[actual]  # Retrocedemos a través de los nodos padre
            return camino[::-1]  # Devolvemos el camino en el orden correcto (de inicio a fin)

        # Generamos los nodos vecinos moviéndonos en 4 direcciones (derecha, izquierda, abajo, arriba)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            vecino = (actual[0] + dx, actual[1] + dy)  # Nueva posición después del movimiento
            
            # Verificamos que el vecino esté dentro de los límites del mapa y no sea un obstáculo (1)
            if 0 <= vecino[0] < len(mapa) and 0 <= vecino[1] < len(mapa[0]) and mapa[vecino[0]][vecino[1]] == 0:
                
                # Si el vecino no ha sido visitado, lo añadimos a la cola de prioridad
                if vecino not in padres:
                    heapq.heappush(abiertos, (heuristica(vecino, objetivo), vecino))  # Lo insertamos en la lista de abiertos
                    padres[vecino] = actual  # Registramos su padre para reconstruir el camino después

        # **Límite de memoria:** Si la lista de abiertos crece demasiado, eliminamos los menos prometedores
        if len(abiertos) > 10:
            abiertos = abiertos[:5]  # Nos quedamos solo con los 5 mejores nodos

    # Si terminamos el bucle sin encontrar el objetivo, no hay camino posible
    return None

# Mapa de prueba (0 = camino libre, 1 = obstáculo)
mapa = [
    [0, 0, 1],  # Fila 0
    [1, 0, 1],  # Fila 1
    [0, 0, 0]   # Fila 2
]

inicio = (0, 0)  # Posición inicial en la esquina superior izquierda
objetivo = (2, 2)  # Posición objetivo en la esquina inferior derecha

# Llamamos al algoritmo y almacenamos el resultado en 'camino'
camino = a_star_ms(inicio, objetivo, mapa)

# **Mensaje claro si se encuentra o no el camino**
if camino:
    print("¡Camino encontrado!:", camino)  # Si encontró el camino, lo imprime
else:
    print("No se encontró un camino posible.")  # Si no encontró el camino, lo avisa