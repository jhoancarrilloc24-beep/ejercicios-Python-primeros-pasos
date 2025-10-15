# zona de funciones

def leer_mes():
    """solo se encarga de leer el numero para determinar el mes del año 1 < 12"""
    num = int(input("pon un numero del 1 al 12 ➡️ :"))
    return num


def mostrar_mes(num):
    """se encarga de mostrar el mes segun el numero ingresado"""
    match num:
        case 1:
            input("enero \n")
        case 2:
            input("febrero \n")
        case 3:
            print("marzo \n")
        case 4:
            print("abrir \n")
        case 5:
            print("mayo \n")
        case 6:
            print("junio \n")
        case 7:
            print("julio \n")
        case 8:
            print("agosto \n")
        case 9:
            print("septiembre \n")
        case 10:
            print("octubre \n")
        case 11:
            print("noviembre \n")
        case 12:
            print("disiembre \n")
        case _:
            print("numero exedido ❌. maximo ✅. del 1 a 12 \n")


def ejecutar():
    """llama al las dos funciones anteriores"""
    num = leer_mes()
    mostrar_mes(num)


# codigo principal

def main():
    """es la funcion principal"""
    ejecutar()

# ejecucion final

main()