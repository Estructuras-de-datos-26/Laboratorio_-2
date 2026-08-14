if __name__ == "__main__":
# Crear la lista doblemente enlazada
    lista = ListaDoblemente()
    try:
        with open("datos.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                # Evitar líneas vacías
                if linea != "":
                    valor = int(linea)
                    # Insertar el valor en la lista
                    lista.insertarAlInicio(valor)
                    lista.imprimirAdelante()
                    print(f"Cantidad de elementos: {lista.cantidadElementos()}")

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")
        exit()

    except ValueError:
        print("Error: el archivo contiene un dato que no es entero.")
        exit()

    with open("Reporte.txt", "w") as archivo:
            archivo.write("====================================\n")
            archivo.write("    REPORTE DE PALABRAS\n")
            archivo.write("====================================\n\n")
            archivo.write(
                "Cantidad de temperaturas: "
                + str(lista.cantidadElementos())
                + "\n"
            )
