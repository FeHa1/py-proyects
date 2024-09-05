with open("historia.txt", "r") as f:
    story = f.read()

palabras = set() # uso 'set()' para que no se repitan elementos
inicio_palabra = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story): 
    if char == target_start: 
        inicio_palabra = i
    
    if char == target_end and inicio_palabra != -1:
        palabra = story[inicio_palabra: i + 1]
        palabras.add(palabra)
        inicio_palabra = -1 # como ya encontramos una palabra reiniciamos la cuenta para el siguiente caracter

respuestas = {}

for palabra in palabras:
    respuesta = input("Ingrese una palabra para " + palabra + ": ")
    respuestas[palabra] = respuesta

for palabra in palabras:
    story = story.replace(palabra, respuestas[palabra])

print(story)

