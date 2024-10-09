
import random

numerosecreto = random.randint(1,101)
adivinado = False
q_intentosmin=0
q_intentosmax=5
print("Bienvenido al primer juego hecho por Lara en Python")

while not adivinado and q_intentosmin< q_intentosmax:
    numero= int(input("Introduce un número del 1 al 100: "))

    if numero == numerosecreto:
        print("Felicitaciones, ganaste!")
        adivinado=True
    elif numero < numerosecreto:
        print("el número secreto es mayor al ingresado")     
    else:
        print("El número secreto es menor al ingresado")

    q_intentosmin += 1

if not q_intentosmin < q_intentosmax:
    print("GAME OVER \nTienes 5 intentos")



    