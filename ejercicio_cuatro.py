"""
crear un diccionario que tenga dos registros de un alumno
1. crear un funcion que me imprima los registro,
2. crear una funcion que me permita editar uno de los campos del registro
"""

#Diccionario con dos registros de un alumno
alumnos = {
    1: {"nombre": "Juan", "apellido": "Cordova", "edad": 18, "curso": "lenguaje de programación"},
    2: {"nombre": "Maria", "apellido": "Lucana", "edad": 18, "curso": "desarrollo de software"}
}

# Función para imprimir los registros de los alumnos
def imprimir_registros():
    for alumno_id, datos in alumnos.items():
        print(f"Registro {alumno_id}: {datos}")

# Función para editar un campo específico de un registro de un alumno
def editar_campo_registro(alumno_id, campo, nuevo_valor):
    if alumno_id in alumnos and campo in alumnos[alumno_id]:
        alumnos[alumno_id][campo] = nuevo_valor
        print(f"Campo '{campo}' editado correctamente para el registro {alumno_id}")

# Ejemplo de uso
print("Registros de los alumnos:")
imprimir_registros()

# Editar el apellido del segundo registro
editar_campo_registro(2, "apellido", "Gonzalez")

print("Registros actualizados de los alumnos:")
imprimir_registros()

