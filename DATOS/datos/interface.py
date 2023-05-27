from tkinter import *
from database import drop_filmes_table

#Funciones
def click_button(str):
    file_name = str
    content = open(file_name).read()
    exec(content)

ventana = Tk()
ventana.title("API to MySQL")

bt_create_db = Button(ventana, 
                      text="Pulsar", 
                      width=5, 
                      height=2, 
                      command=lambda: click_button("main.py"), 
                      background='#28a745', 
                      foreground='white', 
                      activebackground='#218838', 
                      activeforeground='white')

bt_drop_db = Button(ventana, 
                    text="Pulsar2", 
                    width=5, 
                    height=2, 
                    command=lambda: drop_filmes_table(), 
                    background='#dc3545', 
                    foreground='white', 
                    activebackground='#c82333', 
                    activeforeground='white')


bt_create_db.grid(row=1, column=1, padx=100, pady=200)
bt_drop_db.grid(row=1, column=2, padx=100, pady=200)

ventana.mainloop()
