# zona de funciones

def mostar_menu():
    """opciones para poder escoger"""
    print("\n---💠💠.menú principal💠💠---.")
    print("A. actualizar sistema")
    print("B. eliminar catalogo")
    print("C. crear producto")
    print("S. salir del programa\n")
    


def leer_opcion():
    letra = input("digite letra del menu:").upper()
    return letra


def procesar_opcion(letra):
    """procesa las opciones del menu para dar una respesta"""
    if letra == "A":
        print("selecionaste la opcion: actualizando sistema\n")
    elif letra == "B":
        print("selecionaste la opcion: eliminar catalogo\n")
    elif letra == "C":
        print("selecionaste la opcion: crear producto\n")
    elif letra == "S":
        print("finalizado con exito.\n")
        return False # termina el ciclo del codigo
    else:
        print("opcion no valida. intenta denuevo\n")
    return True # lo continua


# codigo principal

def main():
    continuar = True
    while continuar:
        mostar_menu()
        letra = leer_opcion()
        continuar = procesar_opcion(letra)

    print( "el Do-While ha finalizado.\n" )

# ejecucion

main()