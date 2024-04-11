import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

while True:
    respuesta = int(input(f"¿Cuánto es {num1} + {num2}? "))
    if respuesta == num1 + num2:
        print("¡Correcto! Esa es la suma.")
        break
    else:
        print("Esa no es la suma correcta. Inténtalo de nuevo.")