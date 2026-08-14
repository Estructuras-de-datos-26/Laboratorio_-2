class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  #Nos permite movernos hacia la derecha
        self.anterior = None   #Nos permite movernos hacia la izquierda

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None  #Inicio de la lista
        self.cola = None    #Fin de la lista
        self.tamano = 0      #Tamaño de la lista

    def listaVacia(self):
        return self.cabeza is None  #Verifica si la lista está vacía

    def insertarAlInicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.listaVacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamano += 1

    def imprimirAtras(self):
        if self.listaVacia():
            print("La lista está vacía.")
            return
        actual = self.cola
        while actual:
            print(actual.dato, end=" ")
            actual = actual.anterior
        print("None")  # Nueva línea al final

    def imprimirAdelante(self):
        if self.listaVacia():
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print("None")  # Nueva línea al final

    def cantidadElementos(self): #Cantidad de Nodos
        return self.tamano  #Devuelve el tamaño de la lista

    def eliminarFinal(self):
        if self.listaVacia():
            print("La lista está vacía. No se puede eliminar ningún elemento.")
            return
        if self.cabeza == self.cola:  # Si hay un solo nodo
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        self.tamano -= 1


    def imprimirLista(self):
        if self.listaVacia():
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print("None")  # Nueva línea al final

    def buscarElemento(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                return "Elemento encontrado en la posición: " + str(posicion)
            actual = actual.siguiente
            posicion += 1
        return "Elemento no encontrado."

    def insertarAlFinal(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.listaVacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamano += 1

    def insertar_medio(self, valor, posicion):
        if posicion < 0 or posicion > self.tamano:
            print("Posición inválida.")
            return

        if posicion == 0:
            self.insertarAlInicio(valor)
            return

        if posicion == self.tamano:
            self.insertarAlFinal(valor)
            return

        nuevo_nodo = Nodo(valor)
        actual = self.cabeza
        for i in range(posicion):
            actual = actual.siguiente

        anterior = actual.anterior
        nuevo_nodo.anterior = anterior
        nuevo_nodo.siguiente = actual

        anterior.siguiente = nuevo_nodo
        actual.anterior = nuevo_nodo

        self.tamano += 1

    def eliminar_inicio(self):
        if self.listaVacia():
            print("No se puede eliminar: la lista está vacía.")
            return None

        valor_eliminado = self.cabeza.dato
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

        self.tamano -= 1
        return valor_eliminado

    def eliminar_medio(self, posicion):
        if self.listaVacia():
            print("No se puede eliminar: la lista está vacía.")
            return None

        if posicion < 0 or posicion >= self.tamano:
            print("Posición inválida.")
            return None

        if posicion == 0:
            return self.eliminar_inicio()

        if posicion == self.tamano - 1:
            self.eliminarFinal()
            return None

        actual = self.cabeza
        for i in range(posicion):
            actual = actual.siguiente

        valor_eliminado = actual.dato
        anterior = actual.anterior
        siguiente = actual.siguiente

        anterior.siguiente = siguiente
        siguiente.anterior = anterior

        self.tamano -= 1
        return valor_eliminado

    # ---------- Punto 9: cargar datos desde el archivo ----------
    def cargarDesdeArchivo(self, nombre_archivo):
        """Lee un archivo de texto (un nombre por línea) y lo inserta al final de la lista."""
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                nombre = linea.strip()
                if nombre:  # ignora líneas vacías
                    self.insertarAlFinal(nombre)

    # ---------- Punto 11: buscar un nombre y determinar su posición ----------
    def buscarNombre(self, nombre):
        """Devuelve la posición (índice) del nombre, o -1 si no está en la lista."""
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == nombre.strip().title():
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    def contarApariciones(self, nombre):
        """Cuenta cuántas veces aparece un nombre en la lista."""
        actual = self.cabeza
        contador = 0
        while actual:
            if actual.dato == nombre.strip().title():
                contador += 1
            actual = actual.siguiente
        return contador

    # ---------- Punto 12: sustituir un valor en una posición ----------
    def sustituir(self, posicion, palabra):
        """Reemplaza el dato en 'posicion' por 'palabra'. Devuelve el valor anterior o None si la posición es inválida."""
        if posicion < 0 or posicion >= self.tamano:
            print("Posición inválida.")
            return None

        actual = self.cabeza
        for i in range(posicion):
            actual = actual.siguiente

        valor_anterior = actual.dato
        palabra = palabra.strip().title() 
        actual.dato = palabra
        return valor_anterior

    # ---------- Punto 13: ordenar la lista ----------
    def ordenar(self):
        """Ordena la lista doblemente enlazada alfabéticamente (bubble sort intercambiando datos)."""
        if self.listaVacia():
            return
        fin = None
        while fin != self.cabeza:
            actual = self.cabeza
            while actual.siguiente != fin:
                if actual.dato > actual.siguiente.dato:
                    actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                actual = actual.siguiente
            fin = actual

    def obtenerComoTexto(self):
        """Devuelve la lista como string 'a <-> b <-> c <-> None', igual al formato del reporte."""
        if self.listaVacia():
            return "None"
        partes = []
        actual = self.cabeza
        while actual:
            partes.append(str(actual.dato))
            actual = actual.siguiente
        partes.append("None")
        return " <-> ".join(partes)


if __name__ == "__main__":
    NOMBRES_ESTUDIANTES = "Daniela Valenciano Vargas - Christopher Blanco Solano"          
    ARCHIVO_DATOS = "datos.txt"
    ARCHIVO_REPORTE = "Reporte.txt"

    lista = ListaDobleEnlazada()

    # Punto 9-10: cargar los 100 nombres desde el archivo
    lista.cargarDesdeArchivo(ARCHIVO_DATOS)
    print("Se cargaron", lista.cantidadElementos(), "nombres desde", ARCHIVO_DATOS)

    # Punto 11: buscar un nombre
    palabra_buscar = input("Digite una palabra para buscar: ")
    posicion_encontrada = lista.buscarNombre(palabra_buscar)
    veces = lista.contarApariciones(palabra_buscar)

    if posicion_encontrada != -1:
        print("La palabra está en la posición:", posicion_encontrada)
    else:
        print("La palabra no se encontró en la lista.")
    print("La palabra aparece", veces, "veces")

    # Punto 12: sustituir
    posicion_reemplazar = int(input("Digite posición a reemplazar: "))
    nueva_palabra = input("Digite nueva palabra: ")
    palabra_anterior = lista.sustituir(posicion_reemplazar, nueva_palabra)

    # Guardamos la lista ANTES de ordenar (se necesita para el reporte)
    lista_antes_de_ordenar = lista.obtenerComoTexto()

    # Punto 13: ordenar
    lista.ordenar()
    lista_ordenada = lista.obtenerComoTexto()

    # Punto 14-17: escribir el Reporte.txt con el formato pedido
    with open(ARCHIVO_REPORTE, "w", encoding="utf-8") as reporte:
        reporte.write("Digite una palabra para buscar: " + palabra_buscar + "\n")
        if posicion_encontrada != -1:
            reporte.write("La palabra está en la posición: " + str(posicion_encontrada) + "\n")
        else:
            reporte.write("La palabra no se encontró en la lista.\n")
        reporte.write("La palabra aparece " + str(veces) + " veces\n\n")

        reporte.write("Digite posición a reemplazar: " + str(posicion_reemplazar) + "\n")
        reporte.write("Digite nueva palabra: " + nueva_palabra + "\n")
        reporte.write("Se reemplazó: " + str(palabra_anterior) + " por " + nueva_palabra + "\n\n")

        reporte.write("Lista antes de ordenar:\n")
        reporte.write(lista_antes_de_ordenar + "\n\n")

        reporte.write("Lista después de ordenar:\n")
        reporte.write(lista_ordenada + "\n\n")

        reporte.write("Estudiantes: " + NOMBRES_ESTUDIANTES + "\n")

    print("\nReporte generado en '" + ARCHIVO_REPORTE + "'")