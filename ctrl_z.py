from tkinter import Tk
def callback(e): #Ni modo, gracias stackoverflow por la idea x'd
    global key
    key = e.keysym
def on_press():
    global key
    print(key)
    try:
        if key == 'Escape': raise KeyboardInterrupt()
    except KeyboardInterrupt:
        print('Adios!')
        r.destroy()

r = Tk()
key = ''
r.bind("<Key>", lambda e: callback(e))
on_press()
r.mainloop()


op_editor = ['Escribir texto, insertar imagen, escalar imagen, mover imagen, cambiar color, pincel, ']