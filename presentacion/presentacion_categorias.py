from negocio.negocio_categoria import crear_categoria

def solicitar_datos_categoria():
    nombre = ''
    while nombre == '':
        nombre = input('Ingrese nombre de la categoría: ')

    # La descripción es opcional (null=True en el modelo)
    descripcion = input('Ingrese descripción (puede dejarla vacía): ')
    if descripcion == '':
        descripcion = None

    crear_categoria(nombre, descripcion)