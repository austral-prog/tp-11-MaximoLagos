def read_file_to_dict(filename):
    """Lee un archivo de ventas y agrupa los montos por producto."""
    ventas = {}
    with open(filename, "r") as file:
        linea = file.readline().strip()
        partes = linea.split(";")
        for venta in partes:
            if venta:  # evita strings vacíos
                nombre, monto = venta.split(":")
                monto = float(monto)
                if nombre in ventas:
                    ventas[nombre].append(monto)
                else:
                    ventas[nombre] = [monto]
    return ventas


def process_dict(data):
    """Imprime total y promedio de ventas por producto."""
    for nombre in data:
        lista = data[nombre]
        total = sum(lista)
        promedio = total / len(lista)
        print(f"{nombre}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
