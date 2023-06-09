# Importar librerías y módulos necesarios
from tkinter import Tk, Button, ttk
from database import drop_filmes_table, get_filmes_data
from PIL import Image, ImageTk
import urllib.request
import io

# Variables globales
tree = None
df_images = None
label = None


# Funciones
# Crear tabla de la base de datos
def create_db():
    # Mostrar un mensaje al usuario
    status_label.config(text="  Trabajando...  ")
    ventana.update()
    
    try:
        file_name = 'datos_init.py'
        content = open(file_name).read()
        exec(content)
        
        # Actualizar el mensaje al usuario
        status_label.config(text="  Listo  ")
        show_data()
    except Exception as e:
        # Mostrar un mensaje de error al usuario
        status_label.config(text="  La tabla ya existe  ")
        show_data()

# Borra la tabla de la base de datos
def delete_db():
    global image, url, label
    # Mostrar un mensaje al usuario
    status_label.config(text="  Trabajando...  ")
    ventana.update()

    drop_filmes_table()
    # Actualizar el mensaje al usuario
    status_label.config(text="  Listo  ")
    show_data()

    # Vuelve a la imagen de inicio de la aplicación
    Image.open(url)
    # Crear un objeto PhotoImage a partir de la imagen
    photo = ImageTk.PhotoImage(image)
    # Actualizar la imagen del widget Label
    label.config(image=photo)
    label.image = photo

# Crear una tabla que muestra los datos de la tabla filmes de la base de datos
def show_data():
    global tree, df_images, label
    df = get_filmes_data()
    df_images = df.copy()
    columns = list(df.columns)
    del columns[4]  # Excluir la quinta columna (índice 4)
    if tree is None:
        # Crear el widget Treeview solo una vez
        tree = ttk.Treeview(ventana, columns=columns, show='headings')
        tree_scrollbar = ttk.Scrollbar(ventana, orient='vertical', command=tree.yview)
        for col in columns:
            tree.heading(col, text=col)
            tree.column("id", width=30)
            tree.column("title", width=250)
            tree.column("rating", width=50)
            tree.column("year", width=50)
            tree.column("genre", width=70)
            tree.column("director", width=150) 
        # Asociar una función al evento <ButtonRelease-1> del widget Treeview
        tree.bind('<ButtonRelease-1>', on_tree_select)
        tree.configure(yscrollcommand=tree_scrollbar.set)
        tree.pack(padx=50, pady=50)
        tree.place(x=230, y=50)
        tree_scrollbar.place(x=230+tree.winfo_reqwidth(), y=50, height=tree.winfo_reqheight())
    else:
        # Eliminar todos los elementos existentes en el widget Treeview
        for item in tree.get_children():
            tree.delete(item)
    for index, row in df.iterrows():
        values = list(row)
        del values[4]  # Excluir el quinto valor de cada fila (índice 4)
        tree.insert('', 'end', values=values)
    # Estilos del widget Treeview
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    font=("Helvetica", 10)
                    )
    style.configure("Treeview.Heading", 
                    background="#1B3045", 
                    foreground="white",
                    font=("Helvetica", 10, "bold"),
                    borderwidth=0
                    )


# Cambiar imagen a la imagen de la fila seleccionada
def on_tree_select(event):
    global tree, label, df_images
    item = tree.selection()[0]
    values = tree.item(item, 'values')
    if values:
        # Obtener el índice de la fila seleccionada en el DataFrame df_images
        index = int(values[0])
        # Obtener la URL de la imagen de la fila seleccionada
        url = df_images.iloc[index]['image']
        with urllib.request.urlopen(url) as response:
            data = response.read()
        # Cargar la imagen desde la URL
        image = Image.open(io.BytesIO(data))
        # Cambiar el tamaño de la imagen
        new_size = (156, 222)
        image = image.resize(new_size)
        # Crear un objeto PhotoImage a partir de la imagen
        photo = ImageTk.PhotoImage(image)
        # Actualizar la imagen del widget Label
        label.config(image=photo)
        label.image = photo


ventana = Tk()
ventana.title("API to MySQL")
# Cambiar el color de fondo de la ventana princiapl
ventana.configure(background='#2b3e50')
# Cambiar el tamaño de la ventana principal
ventana.geometry("905x550")

# Cargar la imagen desde la URL
url = "./img/sala-cine.jpg"
image = Image.open(url)

# Cambiar el tamaño de la imagen
new_size = (156, 222)
image = image.resize(new_size)
# Crear un objeto PhotoImage a partir de la imagen
photo = ImageTk.PhotoImage(image)

# Crear un widget Label para mostrar la imagen
label = ttk.Label(ventana, image=photo)
label.pack(padx=20, pady=20)
label.place(x=50, y= 50)

# Crear un widget Label para mostrar el estado del programa
status_label = ttk.Label(ventana, 
                         text="  TFG Juan Cebrián Pareja  ", 
                         background='#007bff', 
                         foreground='white',
                         font=('Helvetica', 12, "italic bold")
                         )
status_label.pack()
status_label.place(x=50, y=340)

# Botones
# Crear un botón para crear la base de datos
bt_create_db = Button(ventana,
                      text='CREAR BASE DE DATOS',  # Texto del botón
                      width=60,  # Ancho del botón
                      height=1,  # Altura del botón
                      padx=10,  # Relleno horizontal del botón
                      command=lambda: create_db(),  # Función a llamar cuando se hace clic en el botón
                      background='#5cb85c',  # Color de fondo del botón
                      foreground='white',  # Color del texto del botón
                      activebackground='#218838',  # Color de fondo del botón cuando se hace clic en él
                      font=('Helvetica', 16, "bold"),  # Fuente del texto del botón
                      borderwidth=0)  # Ancho del borde del botón
# Colocar el botón para crear la base de datos en la ventana principal
bt_create_db.place(x=50, y=385)

# Crear un botón para borrar la base de datos
bt_drop_db = Button(ventana,
                    text="BORRAR BASE DE DATOS",  # Texto del botón
                    width=60,  # Ancho del botón
                    height=1,  # Altura del botón
                    padx=10,  # Relleno horizontal del botón
                    command=lambda: delete_db(),  # Función a llamar cuando se hace clic en el botón
                    background='#d9534f',  # Color de fondo del botón
                    foreground='white',  # Color del texto del botón
                    activebackground='#c82333',  # Color de fondo del botón cuando se hace clic en él
                    font=("Helvetica", 16, "bold"),  # Fuente del texto del botón
                    borderwidth=0)  # Ancho del borde del botón
# Colocar el botón para borrar la base de datos en la ventana principal
bt_drop_db.place(x=50, y=440)

# Llamar a la función show_data para mostrar los datos de la base de datos
show_data()
# Entrar en el bucle principal del programa
ventana.mainloop()

