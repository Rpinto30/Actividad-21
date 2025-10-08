import msvcrt #Solo para hacer el chiste que sí es un ctrl+z XD

while True:
    if msvcrt.kbhit(): #Se está presionando algo
        k = msvcrt.getch()
        print(k)
        if k == b'\x1b': break


op_editor = ['Escribir texto, insertar imagen, escalar imagen, mover imagen, cambiar color, pincel, ']