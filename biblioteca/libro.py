class Libro:
    def __init__(self, titulo, autor, genero, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero 
        self.num_paginas = num_paginas

    def mostrar_info(self):
        print("Titulo:", self.titulo)
        print("Autor:", self.autor) 
        print("Genero:", self.genero)
        print("Numero de paginas:", self.num_paginas)

class LibroPrestado(Libro):
    def __init__(self, titulo, autor, genero, num_paginas, prestado_a):
        super().__init__(titulo, autor, genero, num_paginas)
        self.prestado_a = prestado_a

    def mostrar_info(self):
        super().mostrar_info()
        print("Prestado a:", self.prestado_a)

#Crear objetos de la clase libro
libro1 = Libro("El codigo de Vinci", "Dan Bronw", "Misterio", 624)
libro2 = Libro("Cien alos de soledad", "Gabriel Garcia Marquez", "Realismo magico", 432 )

#Mostrar informacio de los libros
print("\nInformacion de libro 1:")
libro1.mostrar_info()
print("\nInformacion del libro 2")
libro2.mostrar_info()

#Crear objetos de la clase Libroprestado
libro_prestado1 = LibroPrestado("Python crash course", "Eric Matthes", "Programacion", 544, "Juan Perez")
libro_prestado2 = LibroPrestado("Clean code", "Robert C. Martin", "programacion", 464, "Maria Gomez")

#Mostrar Informacion de los libros prestados 
print("\nInformacion del libro prestado 1:")
libro_prestado1.mostrar_info()
print("\nInformacion del libro prestado 2:")
libro_prestado2.mostrar_info()