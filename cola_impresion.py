from random import randint
from time import sleep, time
from collections import deque
queue_ = deque()
while True:
    print("1) Mandar a imprimir un doc.\n2) Imprimir\n3) Salir")
    op = input("Selecciona: ")
    match op:
        case '1':
            name = input("Nombre del documento: ")
            queue_.append(name)
            print(f"\nEn cola de impresión:  {name}!\n")
        case '2':
            if queue_:
                print("*"*50)
                start = time()
                u = queue_.popleft()
                for i in range(randint(3,7)):
                    t = f"Imprimiendo {u}"
                    for j in range(4):
                        print(t+"."*j)
                        sleep(0.5)
                    print()
                print(f"\nSe ha impreso {u}!\n")
            else: print("\nNada en cola de impresión\n")
        case '3': break
        case _: pass

