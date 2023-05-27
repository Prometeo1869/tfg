from tkinter import *

#Función
def click_button(str):
    file_name = str
    content = open(file_name).read()
    exec(content)

ventana = Tk()
ventana.title("API to MySQL")

boton = Button(ventana, text="Pulsar", width=5, height=2, command=lambda: click_button("main.py"))
boton2 = Button(ventana, text="Pulsar2", width=5, height=2, command=lambda: click_button("app.py"))

boton.grid(row=1, column=1, padx=100, pady=200)
boton2.grid(row=1, column=2, padx=100, pady=200)

ventana.mainloop()
