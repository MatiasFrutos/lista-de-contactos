# libreta_contactos.py
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ARCHIVO_CONTACTOS = "contactos.json"
contactos = [] 


entry_nombre, entry_telefono, entry_email, listbox_contactos = None, None, None, None

def cargar_contactos_desde_archivo():
    global contactos
    try:
        with open(ARCHIVO_CONTACTOS, 'r') as archivo:
            contactos = json.load(archivo)
    except FileNotFoundError:
        contactos = []
    except json.JSONDecodeError:
        contactos = []
     

def guardar_contactos_al_archivo():
    try:
        with open(ARCHIVO_CONTACTOS, 'w') as archivo:
            json.dump(contactos, archivo, indent=4)
        messagebox.showinfo("Guardado", "Contactos guardados exitosamente.", parent=get_active_window()) 
    except IOError:
        messagebox.showerror("Error de Guardado", "No se pudo guardar los contactos.", parent=get_active_window())



def gui_agregar_contacto():
    if entry_nombre is None: return 

    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    email = entry_email.get()

    if not nombre or not telefono:
        messagebox.showwarning("Campos Vacíos", "Nombre y teléfono son obligatorios.", parent=get_active_window())
        return

    nuevo_contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(nuevo_contacto)

    entry_nombre.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_nombre.focus_set()
    actualizar_lista_contactos_gui()

def gui_actualizar_contacto():
    if listbox_contactos is None or entry_nombre is None: return

    seleccion_indices = listbox_contactos.curselection()
    if not seleccion_indices:
        messagebox.showwarning("Sin Selección", "Por favor, seleccione un contacto para actualizar.", parent=get_active_window())
        return
    
    index_seleccionado = seleccion_indices[0]

    if not (0 <= index_seleccionado < len(contactos)):
        messagebox.showerror("Error", "Selección inválida.", parent=get_active_window())
        return

    nombre_actualizado = entry_nombre.get()
    telefono_actualizado = entry_telefono.get()
    email_actualizado = entry_email.get()

    if not nombre_actualizado or not telefono_actualizado:
        messagebox.showwarning("Campos Vacíos", "Nombre y teléfono son obligatorios.", parent=get_active_window())
        return

    confirmar = messagebox.askyesno("Confirmar Actualización", 
                                     f"¿Actualizar '{contactos[index_seleccionado]['nombre']}'?", parent=get_active_window())
    if confirmar:
        contactos[index_seleccionado]['nombre'] = nombre_actualizado
        contactos[index_seleccionado]['telefono'] = telefono_actualizado
        contactos[index_seleccionado]['email'] = email_actualizado
        actualizar_lista_contactos_gui()
        messagebox.showinfo("Actualizado", "Contacto actualizado.", parent=get_active_window())
        listbox_contactos.selection_set(index_seleccionado)
        listbox_contactos.see(index_seleccionado)

def gui_eliminar_contacto():
    if listbox_contactos is None: return

    seleccion_indices = listbox_contactos.curselection()
    if not seleccion_indices:
        messagebox.showwarning("Sin Selección", "Por favor, seleccione un contacto para eliminar.", parent=get_active_window())
        return

    index_seleccionado = seleccion_indices[0]
    if not (0 <= index_seleccionado < len(contactos)):
        messagebox.showerror("Error", "Selección inválida.", parent=get_active_window())
        return

    nombre_contacto_a_eliminar = contactos[index_seleccionado]['nombre']
    confirmar = messagebox.askyesno("Confirmar Eliminación", 
                                     f"¿Eliminar a '{nombre_contacto_a_eliminar}'?", parent=get_active_window())
    
    if confirmar:
        del contactos[index_seleccionado]
        actualizar_lista_contactos_gui()
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        messagebox.showinfo("Eliminado", f"Contacto '{nombre_contacto_a_eliminar}' eliminado.", parent=get_active_window())

def actualizar_lista_contactos_gui():
    if listbox_contactos is None: return
    listbox_contactos.delete(0, tk.END)
    if not contactos:
        listbox_contactos.insert(tk.END, " (No hay contactos) ")
    else:
        for i, contacto in enumerate(contactos):
            listbox_contactos.insert(tk.END, f"{i+1}. {contacto['nombre']} - {contacto['telefono']}")

def mostrar_detalle_contacto(event):
    if listbox_contactos is None or entry_nombre is None: return

    seleccion_indices = listbox_contactos.curselection()
    if not seleccion_indices: return
    
    index_seleccionado = seleccion_indices[0]
    
    entry_nombre.delete(0, tk.END) 
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    if contactos and index_seleccionado < len(contactos):
        contacto_seleccionado = contactos[index_seleccionado]
        entry_nombre.insert(0, contacto_seleccionado['nombre'])
        entry_telefono.insert(0, contacto_seleccionado['telefono'])
        entry_email.insert(0, contacto_seleccionado['email'])

def construir_ui_contactos(parent_window):
    """Construye la UI de la libreta de contactos dentro de la parent_window dada."""
    global entry_nombre, entry_telefono, entry_email, listbox_contactos

    parent_window.title("Libreta de Contactos")
    parent_window.geometry("550x480")

    frame_entradas = ttk.LabelFrame(parent_window, text="Nuevo / Editar Contacto", padding=(10, 5))
    frame_entradas.pack(pady=10, padx=10, fill="x")

    ttk.Label(frame_entradas, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_nombre = ttk.Entry(frame_entradas, width=40)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    ttk.Label(frame_entradas, text="Teléfono:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_telefono = ttk.Entry(frame_entradas, width=40)
    entry_telefono.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    ttk.Label(frame_entradas, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_email = ttk.Entry(frame_entradas, width=40)
    entry_email.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    
    frame_entradas.columnconfigure(1, weight=1)

    frame_botones_accion = ttk.Frame(parent_window, padding=(0, 5))
    frame_botones_accion.pack(fill="x", padx=10)

    btn_agregar = ttk.Button(frame_botones_accion, text="Agregar Contacto", command=gui_agregar_contacto)
    btn_agregar.pack(side="left", padx=5)
    btn_actualizar = ttk.Button(frame_botones_accion, text="Actualizar Seleccionado", command=gui_actualizar_contacto)
    btn_actualizar.pack(side="left", padx=5)
    btn_eliminar = ttk.Button(frame_botones_accion, text="Eliminar Seleccionado", command=gui_eliminar_contacto)
    btn_eliminar.pack(side="left", padx=5)

    frame_lista = ttk.LabelFrame(parent_window, text="Contactos Guardados", padding=(10, 5))
    frame_lista.pack(pady=10, padx=10, fill="both", expand=True)

    scrollbar_contactos = ttk.Scrollbar(frame_lista, orient="vertical")
    listbox_contactos = tk.Listbox(frame_lista, yscrollcommand=scrollbar_contactos.set, height=10)
    scrollbar_contactos.config(command=listbox_contactos.yview)
    listbox_contactos.pack(side="left", fill="both", expand=True)
    scrollbar_contactos.pack(side="right", fill="y")
    listbox_contactos.bind("<<ListboxSelect>>", mostrar_detalle_contacto)

    btn_guardar_todo = ttk.Button(parent_window, text="Guardar Cambios en Archivo", command=guardar_contactos_al_archivo)
    btn_guardar_todo.pack(pady=(5,10))

    cargar_contactos_desde_archivo() 
    actualizar_lista_contactos_gui() 

_active_contact_window = None
def get_active_window():
    return _active_contact_window


if __name__ == "__main__":
    root_test = tk.Tk()
    _active_contact_window = root_test 
    construir_ui_contactos(root_test)
    root_test.mainloop()