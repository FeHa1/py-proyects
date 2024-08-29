import random # libreria para que elija numeros al azar de un campo dado 

def roll():
    min = 1
    max = 6
    roll = random.randint(min, max) # usa el metodo 'randint()' que devuelve enteros de un rango dado

    return roll

value = roll()

while True:
    players = input('Ingrese el numero de jugadores (2-8): ')
    if players.isdigit(): # el métdo 'isdigit()' va a chequear si lo que se ingresa es un numero
        players = int(players)
        if 2 <= players <= 8:
            break
        else:
            print('Deben ser entre 2 y 8 jugadores.')        
    else: 
        print('Numero no valido, intente otra vez.')

max_score = 3
player_score = [0 for _ in range(players)] # recorre un '_' porque no necesitamos un nombre de varuable para recorrerla

while max(player_score) < max_score:

    for player_index in range(players):
        print('\nJugador numero', player_index + 1, 'acaba de empezar')
        print('Tu puntuación total es: ', player_score[player_index], '\n')

        current_score = 0

        while True:
            should_roll = input('Te gustaria seguir (s)?: ')
            if should_roll.lower() != 's': # el método 'lower()' es para que si pone una 's' mayuscula me lo convierta a minuscula
                break

            value = roll()
            if value == 1:
                print('Sacaste un 1! Vulta terminada!')
                current_score += value - 1# current_score = 0
                break # rompe porque si sacaste 1 termina tu vuelta
            else:
                current_score += value
                print('Tu scaste un: ', value)
            
            print('Tu puntuación actual es: ', current_score)

        player_score[player_index] += current_score
        print('Tu puntuación total es: ', player_score[player_index])

max_score = max(player_score)
winning_index = player_score.index(max_score)
print('El jugador numero', winning_index + 1, 'es el ganado con una puntuación de ', max_score)

