from tkinter import mainloop, Tk
def callback(e): #Ni modo, gracias stackoverflow por la idea x'd
    try:
        print(e)
    except KeyboardInterrupt: pass

r = Tk()
r.bind("<Key>", lambda e: callback(e))
r.mainloop()

op_editor = ['Escribir texto, insertar imagen, escalar imagen, mover imagen, cambiar color, pincel, ']