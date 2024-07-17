"""
Crear una funcion que me me retorne un diccionario con los datos personales de un alumno
ejm:
entrada: ("jose","alvarez","30","APSTI","III")
salida: {nombre:"jose",apellido:"alvarez",edad:"30",programa_estudio:"APSTI",semestre:"III"}
"""
def datos_alumno(nombre, edad, curso, direccion):
    alumno = {
        "Nombre": nombre,
        "Edad": edad,
        "Curso": curso,
        "Dirección": direccion
    }
    return alumno

alumno1 = datos_alumno("Juan Cordova", 18, "II semestre", "Jr. lucanas")
print(alumno1)