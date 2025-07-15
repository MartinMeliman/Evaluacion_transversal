#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]
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
#stock = {modelo: [precio, stock], ...]
stock = {
    '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
    'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def stock_marca(marca):
    marca =  marca.lower()
    total = 0

    for modelo, datos in productos.items():
        if datos[0] == marca:
            total += stock[modelo][1]

    print(f"El stock es: '{marca.capitalize()}': {total}")


#Busqueda de precio
def busqueda_precio(p_min, p_max):
    resultados = []  # Lista donde se guardarán los resultados que cumplan con las condiciones
    for modelo, (precio, cantidad) in stock.items():
         if cantidad > 0 and p_min <= precio <= p_max:
            marca = modelo[marca][0]
            resultados.append(f"{marca}--{modelo}") # Marca--Modelo”.
    # Si se encontraron resultados que cumplen con las condiciones
    if resultados:
        # Ordenamos alfabéticamente 
        for item in sorted(resultados):
            print(item)
    else:
        # Si la lista está vacía, significa que no hay stock disponibles en ese rango de precio
        print("No hay notebooks en ese rango de precios.")

# actualizar precios 
def actualizar_precio(modelo, p):
    if modelo in stock:  # Verificamos si el modelo existe en el diccionario
        stock[modelo][0] = p # Actualizamos el precio
        return True  # Indicamos que la actualización fue exitosa
    else:
        return False  # El modelo no existe
    
def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir")
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        #elif opcion == "2":

main()