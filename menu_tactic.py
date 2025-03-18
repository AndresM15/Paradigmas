from visualizer import TacticVisualizer

def menu():
    visualizer = TacticVisualizer()
    jugadores = {}

    while True:
        print("\nMenú de Jugadas:")
        print("1. Agregar jugador")
        print("2. Hacer un pase")
        print("3. Hacer un disparo")
        print("4. Mostrar táctica")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                numero = int(input("Número del jugador: "))
                x = int(input("Posición X (0-100): "))
                y = int(input("Posición Y (0-60): "))
                visualizer.add_player(numero, x, y)
                jugadores[numero] = (x, y)
            except ValueError:
                print("⚠️ Error: Ingresa valores numéricos válidos.")

        elif opcion == "2":
            try:
                origen = int(input("Número del jugador que pasa el balón: "))
                destino = int(input("Número del jugador que recibe el balón: "))
                if origen in jugadores and destino in jugadores:
                    visualizer.add_ball_pass(origen, destino)
                else:
                    print("⚠️ Error: Ambos jugadores deben estar en el campo.")
            except ValueError:
                print("⚠️ Error: Ingresa valores numéricos válidos.")

        elif opcion == "3":
            try:
                jugador = int(input("Número del jugador que dispara: "))
                if jugador in jugadores:
                    visualizer.add_shot(jugador)
                else:
                    print("⚠️ Error: El jugador debe estar en el campo.")
            except ValueError:
                print("⚠️ Error: Ingresa un número válido.")

        elif opcion == "4":
            print("📊 Mostrando la táctica...")
            visualizer.show()

        elif opcion == "5":
            print("👋 Saliendo del programa.")
            break

        else:
            print("⚠️ Opción no válida. Intente nuevamente.")
