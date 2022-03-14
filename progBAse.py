import tkinter

ventana = tkinter.Tk()
ventana.title("Calculadora")
ventana.geometry("300x300")


def operacion():
    #result.delete(0, tkinter.END)
    #result.insert(0, int(txtnumb1.get())+int(txtnumb2.get()))
    lbNumb2.config(text="Su resultado es:"+str(int(txtnumb1.get())+int(txtnumb2.get())))


lbNumb1 = tkinter.Label(ventana, text="Número 1")
lbNumb1.pack()
txtnumb1 = tkinter.Entry(ventana)
txtnumb1.pack()
lbNumb2 = tkinter.Label(ventana, text="Número 2")
lbNumb2.pack()
txtnumb2 = tkinter.Entry(ventana)
txtnumb2.pack()
lbNumb2 = tkinter.Label(ventana, text="Resultado")
lbNumb2.pack()

btResolver = tkinter.Button(ventana, text="Resolver", command=operacion)
btResolver.pack()
btResolver = tkinter.Button(ventana, text="Salir", command= exit)
btResolver.pack()
ventana.mainloop()
