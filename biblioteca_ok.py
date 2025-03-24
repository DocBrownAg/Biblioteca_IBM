class Libro:
    def __init__(self, titulo, autor, isbn): # Constructor de la clase libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True # Por defecto, el libro está disponible

    def agregar(self): # Método para agregar un libro
        print(f"Libro agregado: {self.titulo} ({self.autor}) - ISBN: {self.isbn}")

    def prestar(self): # Método para prestar un libro
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado con éxito.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self): # Método para devolver un libro
        if not self.disponible:
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto con éxito.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def mostrar(self): # Método para mostrar la información del libro
        if self.disponible:
            disponibilidad = "Sí" 
        else:
            disponibilidad = "No"
        print(f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {disponibilidad}")

    def buscar(self, isbn): # Método para buscar un libro por ISBN
        if self.isbn == isbn:
            self.mostrar()
            return True
        return False
    
libros = [] # Lista para almacenar los libros

def agregar_libro(): # Función para agregar un nuevo libro
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    
    # Creamos un nuevo objeto Libro y lo agregamos a la lista
    nuevo_libro = Libro(titulo, autor, isbn)
    libros.append(nuevo_libro)
    nuevo_libro.agregar()

def prestar_libro(): # Función para prestar un libro
    isbn = input("Ingresa el ISBN: ")
    
    for libro in libros: # Buscamos el libro por ISBN
        if libro.buscar(isbn):
            libro.prestar()
            return
    print("Libro no encontrado.")

def devolver_libro(): # Función para devolver un libro
    isbn = input("Ingresa el ISBN: ")
    
    for libro in libros: # Buscamos el libro por ISBN
        if libro.buscar(isbn):
            libro.devolver()
            return
    print("Libro no encontrado.")

def mostrar_libros(): # Función para mostrar todos los libros
    if not libros:
        print("No hay libros en la biblioteca.")
    else:
        for libro in libros:
            libro.mostrar()

def buscar_libro(): # Función para buscar un libro por ISBN
    isbn = input("Ingresa el ISBN: ")
    
    for libro in libros: # Buscamos el libro por ISBN
        if libro.buscar(isbn):
            return
    print("Libro no encontrado.")

# Menú principal
def menu():
    while True:
        print("\nBienvenido a la Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            mostrar_libros()
        elif opcion == "5":
            buscar_libro()
        elif opcion == "6":
            print("Que tengas un grán día...")
            break
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 6.")

menu()