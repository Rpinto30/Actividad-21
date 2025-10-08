from tkinter import Tk
def callback(e): #Ni modo, gracias stackoverflow por la idea x'd
    global key
    key = e.keysym
def on_press():
    global key
    if key:
        print(key)
        try:
            if key == 'Escape': raise KeyboardInterrupt()
            elif key == 'Control_L':
                if key == 'z': print('zasdasd')
        except KeyboardInterrupt:
            print('Adios!')
            r.destroy()
    r.after(100, on_press) # Como si fuese recursión, la llamo a sí misma

r = Tk()
key = ''
keys = [] #Cola de teclas (quize agregarlo)
r.bind("<Key>", lambda e: callback(e))
on_press()
r.mainloop()


op_editor = ['Escribir texto, insertar imagen, escalar imagen, mover imagen, cambiar color, pincel, ']