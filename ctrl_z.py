op_editor = ['Escribir texto', 'insertar imagen', 'escalar imagen', 'mover imagen', 'cambiar color', 'pincel']

while True:
    print("1) Realizar acción\n2) CTRL+Z\n3) Consultar acciones realizadas\n4) Salir")
    op = input("Selecciona una opción: ")
    match op:
        case '1':
            for n,i in enumerate(op_editor,1):
                print('\t',f"{n}) ", i)
        case '4': break
        case _: pass