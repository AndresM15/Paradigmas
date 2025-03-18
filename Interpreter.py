from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from GramTaticBoardLexer import GramTaticBoardLexer
from GramTaticBoardParser import GramTaticBoardParser
from GramTaticBoardListener import GramTaticBoardListener
from visualizer import TacticVisualizer
from menu_tactic import menu

class TaticInterpreter(GramTaticBoardListener):
    def __init__(self):
        self.visualizer = TacticVisualizer()

    def enterPlayerAction(self, ctx: GramTaticBoardParser.PlayerActionContext):
        text = ctx.getText()
        print(f"[DEBUG] Contexto completo: {text}")

        player_str = ctx.INT().getText()
        player = int(player_str)

        action_ctx = ctx.action()
        if action_ctx.moveAction():
            x_str = action_ctx.moveAction().INT(0).getText()
            y_str = action_ctx.moveAction().INT(1).getText()
            x, y = int(x_str), int(y_str)
            print(f"Jugador {player} se mueve a ({x}, {y})")
            self.visualizer.add_player(player, x, y)

        elif action_ctx.passAction():
            target_str = action_ctx.passAction().INT().getText()
            target = int(target_str)
            print(f"Jugador {player} pasa el balón a {target}")
            self.visualizer.add_ball_pass(player, target)

        elif action_ctx.shootAction():
            print(f"Jugador {player} dispara al arco")
            self.visualizer.add_shot(player)

    def show_visualization(self):
        print("[INFO] Mostrando visualización...")
        self.visualizer.show()

def main():
    print("\nMenú Principal:")
    print("1. Cargar táctica desde archivo")
    print("2. Ingresar táctica manualmente")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
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

    elif opcion == "2":
        menu()

    elif opcion == "3":
        print("👋 Saliendo del programa.")
        return

    else:
        print("⚠️ Opción no válida. Intente nuevamente.")
        main()

if __name__ == "__main__":
    main()
