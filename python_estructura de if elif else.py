# ===== zona de funciones =====

def leer_numero():
    """esta funcion lee un numero ingresado"""
    numero = int(input("digita un numero ➡️ :"))
    return numero

def idintificar_numero(numero):
    """esta funcion identifica si es positivo o negavito """
    if numero > 0:
        resultado = " el numero es positivo  ➕ ."
    elif numero == 0:
        resultado = "el numero es neutro  🟰 ."
    else:
        resultado = "el numero es negativo ➖ ."
    return resultado

def mostrar_resultado(resultado):
    """solo se encarga de mostrar el resultado"""
    print(resultado)

# codigo principal del programa


def main():
    num = leer_numero()
    resultado = idintificar_numero(num)
    mostrar_resultado(resultado)

# zona de ejecucion

main()