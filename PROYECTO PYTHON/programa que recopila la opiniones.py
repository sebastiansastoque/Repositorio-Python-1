#CON ESTE PROYECTO NOS VAMOS A ENFOCAR EN UN PROGRAMA QUE RECOPILE OPINIONES SOBRE LAS PELICULAS QUE HAYAN VISTO LOS USUARIOS
class Pelicula:
    def __init__(self, titulo, genero, duracion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.resenas = []
        self.opiniones = []

    def agregar_resena(self, resena):
        self.resenas.append(resena)

    def agregar_opinion(self, opinion):
        self.opiniones.append(opinion)

    def obtener_resenas(self):
        return self.resenas

    def obtener_opiniones(self):
        return self.opiniones

def main():
    peliculas = {}

    while True:
        titulo = input("Ingresa el título de la película (o 'salir' para terminar): ")
        if titulo.lower() == 'salir':
            break
        genero = input("Ingresa el género de la película: ")
        duracion = input("Ingresa la duración de la película (en minutos): ")

        pelicula = Pelicula(titulo, genero, duracion)
        peliculas[titulo] = pelicula

        print("Por favor, deja tu reseña para la película {}.".format(titulo))
        resena = input("Reseña: ")
        pelicula.agregar_resena(resena)

        print("Ahora, deja tu opinión sobre la película:")
        opinion = input("Opinión: ")
        pelicula.agregar_opinion(opinion)

    print("\nReseñas y opiniones:")
    for titulo, pelicula in peliculas.items():
        print("\n--- {} ---".format(titulo))
        print("Reseñas:")
        for index, resena in enumerate(pelicula.obtener_resenas(), 1):
            print("{}. {}".format(index, resena))
        print("\nOpiniones:")
        for index, opinion in enumerate(pelicula.obtener_opiniones(), 1):
            print("{}. {}".format(index, opinion))

if __name__ == "__main__":
    main()