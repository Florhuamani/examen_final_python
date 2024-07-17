"""
Crear un diccionario de 5 registros de tiendas comerciales
y crear las siguientes funciones para el procesamiento de su informacion
1. funcion que me permita editar el nombre de una las tiendas comerciales
2. funcion que me permita actualizar el horario de atencion.
3. funcion que me permita eliminar una tienda comercial.
"""
tiendas = {
    1: {"nombre": "Tienda 1", "horario": "9:00 - 18:00"},
    2: {"nombre": "Tienda 2", "horario": "8:30 - 19:30"},
    3: {"nombre": "Tienda 3", "horario": "10:00 - 17:00"},
    4: {"nombre": "Tienda 4", "horario": "9:30 - 20:00"},
    5: {"nombre": "Tienda 5", "horario": "8:00 - 21:00"}
}

# Función para editar el nombre de una tienda comercial
def editar_nombre_tienda(tienda_id, nuevo_nombre):
    if tienda_id in tiendas:
        tiendas[tienda_id]["nombre"] = nuevo_nombre
        return True
    return False

# Función para actualizar el horario de atención de una tienda comercial
def actualizar_horario_tienda(tienda_id, nuevo_horario):
    if tienda_id in tiendas:
        tiendas[tienda_id]["horario"] = nuevo_horario
        return True
    return False

# Función para eliminar una tienda comercial.
def eliminar_tienda(tienda_id):
    if tienda_id in tiendas:
        del tiendas[tienda_id]
        return True
    return False

# Ejemplos de uso de las funciones
print("Tiendas antes de la edición:")
print(tiendas)

# Editar el nombre de la Tienda B
editar_nombre_tienda(2, "Nueva Tienda 2")

# Actualizar el horario de la Tienda C
actualizar_horario_tienda(3, "10:30 - 18:00")

# Eliminar la Tienda D
eliminar_tienda(4)

print("\nTiendas después de la edición:")
print(tiendas)