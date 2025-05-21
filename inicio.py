# inicio.py
import tkinter as tk
from tkinter import ttk
import libreta_contactos 

ventana_contactos_actual = None

def abrir_libreta_de_contactos():
    global ventana_contactos_actual, root_inicio 

    if ventana_contactos_actual is not None and ventana_contactos_actual.winfo_exists():
        ventana_contactos_actual.lift()
        ventana_contactos_actual.focus_set()
        return

    ventana_contactos_actual = tk.Toplevel(root_inicio)
    
    libreta_contactos._active_contact_window = ventana_contactos_actual 


    libreta_contactos.construir_ui_contactos(ventana_contactos_actual)

    ventana_contactos_actual.protocol("WM_DELETE_WINDOW", lambda: cerrar_ventana_contactos(ventana_contactos_actual))

def cerrar_ventana_contactos(ventana):
    global ventana_contactos_actual
    ventana.destroy()
    ventana_contactos_actual = None
  


def configurar_gui_inicio():
    global root_inicio 

    root_inicio = tk.Tk()
    root_inicio.title("Programa de Inicio")
    root_inicio.geometry("300x200")

    style = ttk.Style()
    style.configure("TButton", padding=6, relief="flat", font=('Helvetica', 12))

    main_frame = ttk.Frame(root_inicio, padding="20")
    main_frame.pack(expand=True, fill="both")

    titulo_label = ttk.Label(main_frame, text="Panel Principal", font=("Helvetica", 16, "bold"))
    titulo_label.pack(pady=10)

    btn_abrir_libreta = ttk.Button(main_frame, text="Abrir Libreta de Contactos", 
                                   command=abrir_libreta_de_contactos)
    btn_abrir_libreta.pack(pady=20)


    root_inicio.mainloop()

if __name__ == "__main__":
    configurar_gui_inicio()