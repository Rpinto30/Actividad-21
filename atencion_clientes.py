from collections import deque
queue_ = deque()
while True:
    print("1) Entró un cliente!\n2) Atender al cliente\n3) Cerrar")
    op = input("Selecciona: ")
    match op:
        case '1':
            name = input("Como se llama el cliente?: ")
            queue_.append(name)
            print(f"\nEntró {name}!\n")
        case '2':
            if queue_:
                u = queue_.popleft()
                print(f"\nSe tiene que atender a {u}\n")
            else: print("\nNo hay clientes! ¿Es bueno o malo?\n")
        case '3': break
        case _: pass
