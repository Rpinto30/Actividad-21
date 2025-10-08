from collections import deque
op_editor = ['Escribir texto', 'insertar imagen', 'escalar imagen', 'mover imagen', 'cambiar color', 'pincel']
events = deque()

while True:
    print("1) Realizar acción\n2) CTRL+Z\n3) Consultar acciones realizadas\n4) Salir")
    op = input("Selecciona una opción: ")
    match op:
        case '1':
            print('*'*50)
            for n,i in enumerate(op_editor,1):
                print('\t',f"{n}) ", i)
            op_e = input('Selecciona una opción: ')
            try:
                if 1<= int(op_e) <= len(op_editor):
                    events.append(op_editor[int(op_e)-1])
                    print(f'\nSe realizó: {op_editor[int(op_e)-1]}\n')
                else: print("\nNinguna acción realizada\n")
            except ValueError: print("\nEntrada no valida\n")
        case '2':
            print('*' * 50)
            if events:
                print(f"\nSe eliminó: {events[-1]}")
                events.pop()
            else: print("Sin acciones previas...")
        case '3':
            print('*'*50)
            if events:
                for n, i in enumerate(reversed(events), 1):
                    print('\t', f"{n}) ", i)
                print()
            else: print("Sin acciones previas...")
        case '4': break
        case _: pass