"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filtrar_numero_primo(numero):
    prime_numbers = list(filter(es_primo, numero))
    return prime_numbers

# Ejemplo de uso
lista_numero = [2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_primos = filtrar_numero_primo(lista_numero)
print("Números primos en la lista:", numeros_primos)