import numpy as np


def gauss_elimination_binary(a_matrix, b_matrix):
    # Verificación de tamaño de matrices
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("ERROR: La matriz no es cuadrada")
        return
    if b_matrix.shape[0] != a_matrix.shape[0]:
        print("ERROR: El vector constante tiene tamaño incorrecto")
        return

    # Inicialización
    n = len(b_matrix)
    augmented_matrix = np.concatenate(
        (a_matrix, b_matrix.reshape(-1, 1)), axis=1)  # Matriz ampliada
    print("Matriz ampliada inicial:")
    print(augmented_matrix)

    # Escalonamiento Gaussiano modificado
    for i in range(n):
        # Si el elemento pivote es 0, busca una fila debajo para intercambiar
        if augmented_matrix[i, i] == 0:
            for j in range(i + 1, n):
                if augmented_matrix[j, i] == 1:
                    # XOR entre filas
                    augmented_matrix[i] = augmented_matrix[i] ^ augmented_matrix[j]
                    break

        # Aplicar la transformación Fi → Fi + Fj a las filas debajo
        for j in range(i + 1, n):
            if augmented_matrix[j, i] == 1:
                # XOR entre filas
                augmented_matrix[j] = augmented_matrix[j] ^ augmented_matrix[i]

    print("\nMatriz después del escalonamiento:")
    print(augmented_matrix)

    # Sustitución hacia atrás para encontrar la solución
    x = np.zeros(n, dtype=int)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1]  # Término independiente
        for j in range(i + 1, n):
            # XOR para eliminar variables conocidas
            x[i] = x[i] ^ (augmented_matrix[i, j] * x[j])

    print("\nSolucion encontrada (vector x):")
    print(x)

    return x


def lightsOutSolver(matrix):
    n = matrix.shape[0]

    # Crear la matriz de coeficientes A de tamaño n*n por n*n, inicializada en ceros
    a_matrix = np.zeros((n * n, n * n), dtype=int)

    # Iterar sobre cada posición (i, j) en la matriz del juego
    for i in range(n):
        for j in range(n):
            # Calcular el índice lineal que corresponde a la posición (i, j) en una matriz 1D
            index = i * n + j

            # Establecer a 1 el elemento en la diagonal principal de la matriz A,
            # que representa la luz en la posición (i, j)
            a_matrix[index, index] = 1

            # Ahora, necesitamos marcar los vecinos (arriba, abajo, izquierda, derecha)
            # Si el vecino está dentro de los límites del tablero, ponemos un 1 en su posición correspondiente

            # Verificar si la luz tiene un vecino en la fila de arriba
            if i > 0:  # Si no estamos en la primera fila
                vecino_arriba_index = index - n
                a_matrix[index, vecino_arriba_index] = 1

            # Verificar si la luz tiene un vecino en la fila de abajo
            if i < n - 1:  # Si no estamos en la última fila
                vecino_abajo_index = index + n
                a_matrix[index, vecino_abajo_index] = 1

            # Verificar si la luz tiene un vecino a la izquierda
            if j > 0:  # Si no estamos en la primera columna
                vecino_izquierda_index = index - 1
                a_matrix[index, vecino_izquierda_index] = 1

            # Verificar si la luz tiene un vecino a la derecha
            if j < n - 1:  # Si no estamos en la última columna
                vecino_derecha_index = index + 1
                a_matrix[index, vecino_derecha_index] = 1

    # Aplanar la matriz de entrada para obtener el vector de términos constantes
    constant_matrix = matrix.flatten()
    print("Matriz del juego (inicial):")
    print(matrix)
    print("Vector de términos constantes:")
    print(constant_matrix)

    # Resolver el sistema de ecuaciones usando eliminación gaussiana binaria
    solution_vector = gauss_elimination_binary(a_matrix, constant_matrix)

    # Convertir el vector de solución en una matriz
    solution_matrix = solution_vector.reshape(n, n)
    print("\nSolucion encontrada (matriz):")
    print(solution_matrix)

    print("\nSolucion encontrada (vector):")
    print(solution_vector)

    return solution_matrix
