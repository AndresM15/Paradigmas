from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from GramTaticBoardLexer import GramTaticBoardLexer
from GramTaticBoardParser import GramTaticBoardParser
from GramTaticBoardListener import GramTaticBoardListener
from visualizer import TacticVisualizer

class TaticInterpreter(GramTaticBoardListener):
    def __init__(self):
        self.visualizer = TacticVisualizer()

    def enterPlayerAction(self, ctx: GramTaticBoardParser.PlayerActionContext):
        """
        playerAction: 'player' '(' INT ')' action
        """
        # Muestra el texto completo del subárbol
        text = ctx.getText()
        print(f"[DEBUG] Contexto completo: {text}")

        # Extrae el número del jugador
        player_str = ctx.INT().getText()
        player = int(player_str)

        # Identifica la acción
        action_ctx = ctx.action()
        if action_ctx.moveAction():
            # move(30,40)
            x_str = action_ctx.moveAction().INT(0).getText()
            y_str = action_ctx.moveAction().INT(1).getText()
            x, y = int(x_str), int(y_str)
            print(f"Jugador {player} se mueve a ({x}, {y})")
            self.visualizer.add_player(player, x, y)

        elif action_ctx.passAction():
            # pass(7)
            target_str = action_ctx.passAction().INT().getText()
            target = int(target_str)
            print(f"Jugador {player} pasa el balón a {target}")
            # Jugador target debe tener posición
            self.visualizer.add_ball_pass(player, target)

        elif action_ctx.shootAction():
            # shoot(goal)
            print(f"Jugador {player} dispara al arco")
            self.visualizer.add_shot(player)

    def show_visualization(self):
        """Muestra la táctica al final."""
        print("[INFO] Mostrando visualización...")
        self.visualizer.show()

def main():
    input_file = "entrada.tactic"
    print(f"[INFO] Procesando archivo: {input_file}")

    try:
        input_stream = FileStream(input_file, encoding="utf-8")
        lexer = GramTaticBoardLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = GramTaticBoardParser(stream)
        tree = parser.tactic()

        interpreter = TaticInterpreter()
        walker = ParseTreeWalker()
        walker.walk(interpreter, tree)

        interpreter.show_visualization()

    except Exception as e:
        print(f"[ERROR] Ocurrió un problema al procesar la táctica: {e}")

if __name__ == "__main__":
    main()