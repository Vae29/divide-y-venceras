import csv
#Funcion Merge Sort 
def merge_sort(lista, key):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    izquierda = merge_sort(lista[:mid], key)
    derecha = merge_sort(lista[mid:], key)

    return merge(izquierda, derecha, key)

def merge(izquierda, derecha, key):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if key(izquierda[i]) <= key(derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def ordenar_productos_csv(archivo_entrada, archivo_salida):
    productos = []

    with open(archivo_entrada, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['precio'] = float(row['precio'])
            row['calificacion'] = float(row['calificacion'])
            row['stock'] = int(row['stock'])
            productos.append(row)


    productos_ordenados = merge_sort(
        productos, key=lambda x: (-x['calificacion'], x['precio'])
    )

    with open(archivo_salida, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['id', 'nombre', 'precio', 'calificacion', 'stock']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(productos_ordenados)

    print(f"Archivo ordenado guardado en: {archivo_salida}")


if __name__ == "__main__":
    entrada = input("Ingrese el nombre del archivo CSV de entrada: ")
    salida = input("Ingrese el nombre del archivo CSV de salida: ")
    ordenar_productos_csv(entrada, salida)
