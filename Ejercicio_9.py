def pro_iva(productos):

    """
     se genera un diccionario con los nombres de los productos y los precios con iva includio
    """

    return {i["nombre"]: round(i["precio"] * 1.19, 2) for i in productos}

if __name__ == "__main__":
    list_productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]

    precios_con_iva = pro_iva(list_productos)
    print("Precios con IVA:", precios_con_iva)