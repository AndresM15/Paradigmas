import matplotlib.pyplot as plt

class   TacticVisualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.players = {}
        self.passes = []
        self.shots = []
        self.draw_field()

    def update_visualization(self):
        """Limpia y redibuja toda la táctica."""
        self.ax.clear()  # Limpia el gráfico antes de redibujar
        self.draw_field()  # Dibuja la cancha desde cero

        # Dibuja jugadores
        for number, (x, y) in self.players.items():
            self.ax.plot(x, y, 'bo', markersize=8)
            self.ax.text(x, y + 2, str(number), fontsize=10, color='black', ha='center')

        # Dibuja pases
        for (x1, y1, x2, y2) in self.passes:
            self.ax.arrow(x1, y1, x2 - x1, y2 - y1, head_width=1, length_includes_head=True, color='yellow')

        # Dibuja disparos
        for (x, y) in self.shots:
            self.ax.arrow(x, y, 10, 0, head_width=1.5, length_includes_head=True, color='red')

        self.fig.canvas.draw()  # Redibuja el gráfico
        self.fig.canvas.flush_events()  # Maneja eventos de la ventana

    def draw_field(self):
        """Dibuja la cancha de fútbol."""
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 60)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_title("Tactic Board - Visualización de Jugadas")

        # Línea central
        self.ax.plot([50, 50], [0, 60], 'k-', lw=2)

        # Áreas
        self.ax.add_patch(plt.Rectangle((0, 20), 10, 20, fc='none', ec='k'))
        self.ax.add_patch(plt.Rectangle((90, 20), 10, 20, fc='none', ec='k'))

    def add_player(self, number, x, y):
        """Coloca un jugador en (x,y) y actualiza la visualización."""
        self.players[number] = (x, y)
        self.update_visualization()

    def add_ball_pass(self, from_player, to_player):
        """Dibuja una flecha amarilla de pase."""
        if from_player in self.players and to_player in self.players:
            x1, y1 = self.players[from_player]
            x2, y2 = self.players[to_player]
            self.passes.append((x1, y1, x2, y2))
            self.update_visualization()

    def add_shot(self, player):
        """Dibuja una flecha roja simulando un disparo al arco."""
        if player in self.players:
            x, y = self.players[player]
            self.shots.append((x, y))
            self.update_visualization()

    def show(self):
        plt.close(self.fig)
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.draw_field()
        self.update_visualization()  # Actualiza con los datos actuales
        plt.show(block=False)
