"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def es_primos(num):
    if num < 2:
        return False
    for i in range (2,int(num**0,5)+1):
        if num %1==0:
            return False
    return True

def filtrar_numero_primo(numero):
    numeros_primos=list(filter(es_primos,numero))
    return numeros_primos