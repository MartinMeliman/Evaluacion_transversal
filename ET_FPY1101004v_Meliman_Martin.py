# productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']

}
# stock = {modelo: [precio, stock], ...]
stock = {
    '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
    'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

# stock marca 
def stock_marca(marca):
    marca = marca.lower() 
    total = 0 # contador de stock
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            if modelo in stock:
                total += stock[modelo][1] # stock total
    print(f"El stock de: {total}")


# Busqueda de precio
def busqueda_precio(p_min, p_max):
    resultados = [] # Lista donde se guardarán los resultados que cumplan con las condiciones
    for modelo, (precio, cantidad) in stock.items():
        if cantidad > 0 and p_min <= precio <= p_max:
            if modelo in productos:
                marca = productos[modelo][0]
                resultados.append(f"{marca}--{modelo}")
    
    # Si se encontraron resultados que cumplen con las condiciones
    if resultados:
        resultados.sort() #ordenado alfabeticamete
        print(f"Los notebooks entre los precios consultas son: {resultados}")
    else:
        print("No hay notebooks en ese rango de precios.")

# actualizar precios 
def actualizar_precio(modelo, p):
    if modelo in stock:  # Verificamos si el modelo existe en el diccionario
        stock[modelo][0] = p # Actualizamos el precio
        return True  # Indicamos que la actualización fue exitosa
    else:
        return False  # El modelo no existe
    
# Menú principal
def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        opcion = input("Ingrese opción: ")

        # stock marca
        if opcion == "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)
        
        # busqueda por precio
        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    busqueda_precio(p_min, p_max)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
        #Actualizar precio
        elif opcion == "3":
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese precio nuevo: "))
                    if actualizar_precio(modelo, nuevo_precio):
                        print("Precio actualizado!!")
                    else:
                        print("El modelo no existe!!")
                except ValueError:
                    print("Debe ingresar un precio válido.")
                
                repetir = input("Desea actualizar otro precio (s/n)?: ").lower()
                if repetir != "si":
                    break
        # Salir
        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")

# Ejecutar el programa
main()