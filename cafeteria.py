from collections import deque
queue_ = deque()

tipos_cafe = [ #Esto se lo pedí a la IA, no se me ocurrian XDD
    "Espresso",
    "Americano",
    "Latte",
    "Cappuccino",
    "Mocha",
    "Macchiato"
]

while True:
    print("1) Atender al cliente!\n2) Dar pedido\n3) Cerrar")
    op = input("Selecciona: ")
    match op:
        case '1':
            name = input("A quien está el nombre del pedido?: ")
            print("Muy bien!")
            try:
                print("Que desea pedir?: ")
                for n,i in enumerate(tipos_cafe,1): print(f"\t {n}) {i}")
                op_c = input("Ingresa la opción que deseas pedir: ")
                if 1<= int(op_c) <= len(tipos_cafe):
                    queue_.append({name: tipos_cafe[int(op_c)-1]})
                    print(f"Sale un {tipos_cafe[int(op_c)-1]} para {name}!!")
                else: raise  ValueError()
            except ValueError: print("Lo siento... algo pasó :c")
        case '2':
            if queue_:
                u = queue_.popleft()
                print(f"\nUn {list(u.values())[0]} para el señor {list(u.keys())[0]}\n")
            else: print("\nNo hay clientes! ¿Es bueno o malo?\n")
        case '3': break
        case _: pass

