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

                print(f"Mandando a imprimir: {u}")
                print(f"En cola de impresión:")
                for n, i in enumerate(queue_,1): print(f"\t{n}) {i}")
                sleep(2.5)
                print()
                for i in range(randint(2,5)):
                    t = f"Imprimiendo {u}"
                    for j in range(4):
                        print(t+"."*j)
                        sleep(0.2)
                    print()
                    sleep(1)
                print(f"\nSe ha impreso {u}!\n")
            else: print("\nNada en cola de impresión\n")
        case '3': break
        case _: pass

