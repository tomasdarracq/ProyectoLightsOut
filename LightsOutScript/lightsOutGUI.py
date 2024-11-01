import tkinter as tk
import numpy as np

from scriptLightsOut import lightsOutSolver


class LightsOutGame:
    def __init__(self, root, size):
        self.size = size
        self.root = root
        # Inicializa el tablero de forma aleatoria
        self.board = np.random.randint(0, 2, (size, size))
        lightsOutSolver(self.board)
        self.buttons = [[None for _ in range(size)] for _ in range(size)]

        # Crear los botones de la GUI
        for i in range(size):
            for j in range(size):
                button = tk.Button(
                    root, width=10, height=4, command=lambda i=i, j=j: self.toggle_lights(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.update_buttons()

    def toggle_lights(self, i, j):
        """Cambia el estado del botón y de sus vecinos"""
        directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)
                      ]  # (i, j) más vecinos (arriba, abajo, izquierda, derecha)
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.size and 0 <= nj < self.size:
                # XOR para cambiar entre 0 y 1 (apagar/encender)
                self.board[ni, nj] ^= 1

        self.update_buttons()

    def update_buttons(self):
        """Actualizar la apariencia de los botones basado en el estado del tablero"""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i, j] == 1:
                    self.buttons[i][j].config(bg='red')  # Encendido
                else:
                    self.buttons[i][j].config(bg='green')  # Apagado

        # Verificar si todas las luces están encendidas (todos los valores de la matriz son 1)
        if np.all(self.board == 0):
            print("¡Ganaste! Todas las luces están encendidas.")
            self.show_win_message()

    def show_win_message(self):
        """Mostrar un mensaje de victoria en la interfaz"""
        win_label = tk.Label(
            self.root, text="¡Ganaste! Todas las luces están encendidas.", fg="blue", font=("Helvetica", 16))
        win_label.grid(row=self.size, column=0, columnspan=self.size)


# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Lights Out")

# Tamaño del tablero (por ejemplo, 5x5)
game = LightsOutGame(root, 3)

# Iniciar el loop principal de Tkinter
root.mainloop()
