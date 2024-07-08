#YEISON ALTAMAR, NATALIA PÉREZ, GERALDYNE ARIZA
#ADSO-7 2664531

import os

class SistemaNotas:
    def __init__(self, archivo_bd):
        self.archivo_bd = archivo_bd
        self.estudiantes = {}
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open(self.archivo_bd, "r") as archivo:
                for linea in archivo:
                    codigo, apellido, nombre, nota_1, nota_2, nota_3 = linea.strip().split(',')
                    self.estudiantes[codigo] = [apellido, nombre, float(nota_1), float(nota_2), float(nota_3)]
        except FileNotFoundError:
            print(f"El archivo {self.archivo_bd} no existe. Se creará al agregar estudiantes.")

    def guardar_datos(self):
        with open(self.archivo_bd, "w") as archivo:
            for codigo, datos in self.estudiantes.items():
                linea = f"{codigo},{datos[0]},{datos[1]},{datos[2]},{datos[3]},{datos[4]}\n"
                archivo.write(linea)

    def agregar_estudiante(self, codigo, apellido, nombre, nota_1, nota_2, nota_3):
        self.estudiantes[codigo] = [apellido, nombre, float(nota_1), float(nota_2), float(nota_3)]
        self.guardar_datos()
        print(f"Estudiante con código {codigo} agregado correctamente.")

    def actualizar_estudiante(self, codigo, apellido, nombre, nota_1, nota_2, nota_3):
        if codigo in self.estudiantes:
            self.estudiantes[codigo] = [apellido, nombre, float(nota_1), float(nota_2), float(nota_3)]
            self.guardar_datos()
            print(f"Estudiante con código {codigo} actualizado.")
        else:
            print("Estudiante no encontrado")

    def borrar_estudiante(self, codigo):
        if codigo in self.estudiantes:
            del self.estudiantes[codigo]
            self.guardar_datos()
            print(f"Estudiante con código {codigo} borrado.")
        else:
            print("Estudiante no encontrado")

    def listar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        else:
            print("Estudiantes:")
            for codigo, datos in self.estudiantes.items():
                print(f"Código: {codigo}, Apellido: {datos[0]}, Nombre: {datos[1]}, Nota_1: {datos[2]}, Nota_2: {datos[3]}, Nota_3: {datos[4]}")

    def estudiante_con_mayor_promedio(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados")
            return None

        max_promedio = float('-inf')
        estudiante_max = None

        for codigo in self.estudiantes:
            promedio = sum(self.estudiantes[codigo][2:]) / 3
            if promedio > max_promedio:
                max_promedio = promedio
                estudiante_max = codigo

        return estudiante_max

    def promedio_general_curso(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados")
            return None

        total_notas = sum(sum(datos[2:]) for datos in self.estudiantes.values())
        total_estudiantes = len(self.estudiantes)

        promedio_general = total_notas / (total_estudiantes * 3)
        return promedio_general

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar estudiante")
    print("2. Actualizar estudiante")
    print("3. Borrar estudiante")
    print("4. Listar estudiantes")
    print("5. Mostrar estudiante con el promedio más alto")
    print("6. Mostrar promedio general del curso")
    print("7. Salir")
    print("****************************************DESARROLLADO BY : NATALIA PEREZ & YEISON ALTAMAR & GERALDYNE ARIZA***********************************")

# Ejemplo de uso del sistema con menú
archivo_bd = "base_datos.txt"
sistema_notas = SistemaNotas(archivo_bd)

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-7): ")

    if opcion == "1":
        codigo = input("Ingrese el código del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        nota_1 = float(input("Ingrese la Nota 1 del estudiante: "))
        nota_2 = float(input("Ingrese la Nota 2 del estudiante: "))
        nota_3 = float(input("Ingrese la Nota 3 del estudiante: "))
        sistema_notas.agregar_estudiante(codigo, apellido, nombre, nota_1, nota_2, nota_3)

    elif opcion == "2":
        codigo = input("Ingrese el código del estudiante a actualizar: ")
        apellido = input("Ingrese el nuevo apellido del estudiante: ")
        nombre = input("Ingrese el nuevo nombre del estudiante: ")
        nota_1 = float(input("Ingrese la nueva Nota 1 del estudiante: "))
        nota_2 = float(input("Ingrese la nueva Nota 2 del estudiante: "))
        nota_3 = float(input("Ingrese la nueva Nota 3 del estudiante: "))
        sistema_notas.actualizar_estudiante(codigo, apellido, nombre, nota_1, nota_2, nota_3)

    elif opcion == "3":
        codigo = input("Ingrese el código del estudiante a borrar: ")
        sistema_notas.borrar_estudiante(codigo)

    elif opcion == "4":
        sistema_notas.listar_estudiantes()

    elif opcion == "5":
        estudiante_max = sistema_notas.estudiante_con_mayor_promedio()
        if estudiante_max:
            print(f"Estudiante con el promedio más alto: {sistema_notas.estudiantes[estudiante_max][1]} {sistema_notas.estudiantes[estudiante_max][0]}")

    elif opcion == "6":
        promedio_general = sistema_notas.promedio_general_curso()
        if promedio_general:
            print(f"Promedio general del curso: {promedio_general}")

    elif opcion == "7":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

