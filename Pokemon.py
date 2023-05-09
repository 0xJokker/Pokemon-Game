import random

class Pokemon:
    def __init__(self, nombre, ataque, tipo):
        self.nombre = nombre
        self.ataque = ataque
        self.tipo = tipo
        self.vida = 100

    def gano(self):
        print(f"{self.nombre} GANO ESTA BATALLA!!!")
        print("Más suerte la próxima vez!!!")

         

p1 = Pokemon("Pikachu", 15, "electricidad")
p2 = Pokemon("Bulbasur", 15, "planta")
p3 = Pokemon("squirtle", 15, "agua")
p4 = Pokemon("Scyther", 17, "tierra")
p5 = Pokemon("Charmander", 18, "fuego")


def elegir_pokemon1(p1, p2, p3, p4, p5):
    print(f"Elige tu pokemon 1.{p1.nombre}, 2.{p2.nombre}, 3.{p3.nombre}, 4.{p4.nombre}, 5. {p5.nombre}")
    opcion = int(input(""))
    if opcion == 1:
        j1 = p1
        print(f"has elegido {p1.nombre}")
    elif opcion == 2:
        j1 = p2
        print(f"has elegido {p2.nombre}")
    elif opcion == 3:
        j1 = p3
        print(f"has elegido {p3.nombre}")
    elif opcion == 4:
        print(f"has elegido {p4.nombre}")
        j1 = p4
    elif opcion == 5:
        print(f"has elegido {p5.nombre}")
        j1 = p5

    return j1

def elegir_pokemon2(p1, p2, p3, p4, p5):
    print(f"Elige tu Pokemon 1.{p1.nombre}, 2.{p2.nombre}, 3.{p3.nombre}, 4.{p4.nombre}, 5. {p5.nombre}")
    opcion = int(input(""))
    if opcion == 1:
        j2 = p1
        print(f"has elegido {p1.nombre}")
    elif opcion == 2:
        j2 = p2
        print(f"has elegido {p2.nombre}")
    elif opcion == 3:
        j2 = p3
        print(f"has elegido {p3.nombre}")
    elif opcion == 4:
        print(f"has elegido {p4.nombre}")
        j2 = p4
    elif opcion == 5:
        print(f"has elegido {p5.nombre}")
        j2 = p5

    return j2

def daño1(j1,j2):
    if j1.tipo == "agua" and j2.tipo == "fuego":
            j1.ataque = j1.ataque * 1.5
    elif  j1.tipo == "fuego" and j2.tipo == "agua":
            j1.ataque = j1.ataque * 0.8
    elif j1.tipo == "electricidad" and j2.tipo == "tierra":
            j1.ataque = j1.ataque * 0.8


def daño2(j1,j2):
    if j2.tipo == "agua" and j1.tipo == "fuego":
            j2.ataque = j2.ataque * 1.5
    elif  j2.tipo == "fuego" and j1.tipo == "agua":
            j2.ataque = j2.ataque * 0.8
    elif j2.tipo == "electricidad" and j1.tipo == "tierra":
        j2.ataque = j2.ataque * 0.8


def juego():
    while True:
        j1 = elegir_pokemon1(p1, p2, p3, p4, p5)
        j2 = elegir_pokemon2(p1, p2, p3, p4, p5)
        turno = random.randint(1, 2)
        daño1(j1,j2)
        daño2(j1,j2)
        j1.vida = 100
        j2.vida = 100
        while j1 == j2:
            print("opcion invalida")
            j1 = elegir_pokemon1(p1, p2, p3, p4, p5)
            j2 = elegir_pokemon2(p1, p2, p3, p4, p5)

        while j1.vida > 0 and j2.vida > 0:
            if turno == 1:
                j2.vida -= j1.ataque
                turno = 2
                print(f"{j1.nombre} ataca, {j2.nombre} ahora tiene {j2.vida} de vida")
                if j2.vida > 0:
                    print("\n=== PRÓXIMA RONDA ===")

            else:
                j1.vida = j1.vida - j2.ataque
                turno = 1
                print(f"{j2.nombre} ataca, {j1.nombre} ahora tiene {j1.vida} de vida")
                if j1.vida > 0:
                    print("\n=== PRÓXIMA RONDA ===")

            # Consultamos si el pokemon 1 perdio
        if j1.vida <= 0:
            j2.gano()

            # Sino significa que el pokemon 1 gano
        else:
            j1.gano()

        print("¿Volver a jugar? [s/n]")
        volver = input("> ")
        if volver == "s":
            juego()
        elif volver == "n":
            print("Has elegido salir")
            break
juego()



