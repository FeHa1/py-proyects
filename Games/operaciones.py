import random
import time

OPERADORES = ["+", "-", "*"]
OPERADOR_MIN = 3
OPERADOR_MAX= 12
PROBLEMAS_TOTALES = 10


def generar_problema():
    izq = random.randint(OPERADOR_MIN, OPERADOR_MAX)
    der = random.randint(OPERADOR_MIN, OPERADOR_MAX)
    operador = random.choice(OPERADORES)

    expr = str(izq) + " " + operador + " " + str(der)
    respuesta = eval(expr)
    return expr, respuesta

error = 0
input("\nToca ENTER para comenzar")
print("------------------------")

inicio_temporizador = time.time()

for i in range(PROBLEMAS_TOTALES):
    expr, respuesta = generar_problema()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(respuesta):
            break
        else:
            error += 1
            print("¡Respuesta incorrecta! Vuelve a intentarlo")

final_temporizador = time.time()
tiempo_total = round(final_temporizador - inicio_temporizador, 2)

print("------------------------------------------------------------")
print(f"¡Buen trabajo! completaste el reto en {tiempo_total} segundos")
print(f"Cometiste errores un total de {error} veces\n")