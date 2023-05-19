import csv

# Función para procesar los datos del archivo CSV
def procesar_archivo_csv(archivo_csv):
    # Diccionario para almacenar los IDs por technical_name
    datos_procesados = {}

    # Abrir el archivo CSV
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        # Leer el archivo CSV usando el módulo csv
        datos_csv = csv.DictReader(archivo)

        # Iterar sobre las filas del archivo CSV
        for fila in datos_csv:
            id = fila['id']
            technical_name = fila['technical_name']

            # Agregar el ID al technical_name correspondiente
            if technical_name in datos_procesados:
                datos_procesados[technical_name].append(id)
            else:
                datos_procesados[technical_name] = [id]

    # Crear un nuevo archivo CSV para almacenar los resultados
    nuevo_archivo_csv = 'nuevo_archivo.csv'  # Nombre del nuevo archivo CSV

    # Escribir los datos procesados en el nuevo archivo CSV
    with open(nuevo_archivo_csv, 'w', encoding='utf-8', newline='') as archivo_nuevo:
        # Definir los nombres de las columnas
        nombres_columnas = ['ids', 'technical_name']

        # Crear el escritor CSV
        escritor_csv = csv.writer(archivo_nuevo)
        escritor_csv.writerow(nombres_columnas)

        # Escribir los datos procesados en el nuevo archivo CSV
        for technical_name, ids in datos_procesados.items():
            escritor_csv.writerow([ids, technical_name])

    print(f"Se ha creado el archivo CSV '{nuevo_archivo_csv}' con los datos procesados.")

# Ruta del archivo CSV de entrada
archivo_csv = 'modulos_tickets_orden.csv'  # Reemplaza con la ruta correcta de tu archivo CSV

# Llamar a la función para procesar el archivo CSV
procesar_archivo_csv(archivo_csv)
