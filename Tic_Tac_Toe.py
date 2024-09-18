import tkinter as tk
from tkinter import messagebox

## Clase Jugador
class Jugador:
    def __init__(self, simbolo):
        self.simbolo = simbolo

## Clase Tablero
class Tablero:
    def __init__(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]

    def verificar(self, fila, columna):
        return self.tablero[fila][columna] == ' '

    def realizar_movimiento(self, fila, columna, jugador):
        if self.verificar(fila, columna):
            self.tablero[fila][columna] = jugador.simbolo
            return True
        return False

    def ganador(self):
        combinaciones_ganadoras = [
            [(0, 2), (0, 1), (0, 2)],  # Fila 1
            [(1, 0), (1, 1), (1, 2)],  # Fila 2
            [(2, 0), (2, 1), (2, 2)],  # Fila 3
            [(0, 0), (1, 0), (2, 0)],  # Columna 1
            [(0, 2), (1, 1), (2, 1)],  # Columna 2
            [(0, 2), (1, 2), (2, 2)],  # Columna 3
            [(0, 2), (1, 1), (2, 2)],  # Diagonal \
            [(0, 2), (1, 1), (2, 0)]   # Diagonal /
        ]

        for jugador in ['O', 'X']:
            for combinacion in combinaciones_ganadoras:
                if all(self.tablero[fila][columna] == jugador for fila, columna in combinacion):
                    return Jugador
        return None

    def empate(self):
        return all(campo != ' ' for fila in self.tablero for campo in fila)

## Clase Juego
class Juego:
    def __init__(self, master):
        self.master = master
        self.master.title("Tres en Raya")
        self.tablero = Tablero()
        self.jugador1 = Jugador('O')
        self.jugador2 = Jugador('X')
        self.turno = 0
        self.boton = [[None for _ in range(3)] for _ in range(3)]
        self.crear_botones()

    def crear_botones(self):
        for i in range(3):
            for j in range(3):
                self.boton[i][j] = tk.Button(self.master, text=' ', font=('Arial', 24), width=5, height=2,
                                              command=lambda fila=i, columna=j: self.jugar(fila, columna))
                self.boton[i][j].grid(row=i, column=j)

    def jugar(self, fila, columna):
        jugador_actual = self.jugador1 if self.turno % 2 == 0 else self.jugador2
        if self.tablero.realizar_movimiento(fila, columna, jugador_actual):
            self.boton[fila][columna].config(text=jugador_actual.simbolo)
            if self.tablero.ganador():
                messagebox.showinfo("Fin del juego", f"¡El jugador {jugador_actual.simbolo} ha ganado!")
                self.reiniciar_juego()
            elif self.tablero.empate():
                messagebox.showinfo("Fin del juego", "¡Es un empate!")
                self.reiniciar_juego()
            else:
                self.turno += 1

    def reiniciar_juego(self):
        self.tablero = Tablero()
        self.turno = 0
        for fila in range(3):
            for columna in range(3):
                self.boton[fila][columna].config(text=' ')


if __name__ == "__main__":
    root = tk.Tk()
    juego = Juego(root)
    root.mainloop()