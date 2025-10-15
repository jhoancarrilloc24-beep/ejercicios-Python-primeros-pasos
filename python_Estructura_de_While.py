# zona de funciones


def leer_numero():
    """solo lee el numero"""
    numero = int(input("digita un numero ➡️. (0 para salir): "))
    return numero


def verifica_par_o_impar(numero):
    """verifica si el numero es par o impar"""
    if numero % 2 == 0:
        print("el numero es par ✅. \n")
    else:
        print("el numero es impar 🔺. \n")

# funcion muy importante "p"

def ejecutar():
    """controla el ciclo"""
    num = 1 # valor inicial diferente a 0
    while num != 0:
        num = leer_numero()
        if num != 0:
            verifica_par_o_impar(num)
        else:
            print("finalizado el programa ♻️ .✅. \0")


# codigo principal

def main():
    """funcion principal"""
    ejecutar()

# ejecucion
main()