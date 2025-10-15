# funcion 1: pedir una cantidad

def pedir_cantidad():
    cantidad = int(input("digita una cantidad de numeros para sumar ➡️ : "))
    return cantidad

# funcion 2: realiza una suma
def sumar_numeros(cantidad):
    suma = 0
    for i in range(cantidad):
        numero = int(input("digita el numero ➡️. " + str(i + 1) + ": "))
        suma += numero
    return suma


# funcion 3: mostrar el resultado 

def mostrar_resultado(suma):
    print("la suma total es 🟰 : ", suma)


# funcion principal 
#codigo principal

def main():
    cantidad = pedir_cantidad()
    resultado = sumar_numeros(cantidad)
    mostrar_resultado(resultado)

# ejecucion 

main()