"""
crear un funcion que me retorne un diccioonario de la cantidad de vocales que aparecen en un texto pasado por parametro el diccionario debera ser credo por comprension de diccionarios
ejm:
entrada: eucalipto
salida: {e:1,u:1,a:1,i:1,o:1}
"""
def contar_vocales(texto):
    vocales = "aeiou"
    vocales_count = {vocal: texto.lower().count(vocal) for vocal in vocales if vocal in texto.lower()}
    return vocales_count

texto_ejemplo = "hola,como estas"
resultado = contar_vocales(texto_ejemplo)
print(resultado) 
