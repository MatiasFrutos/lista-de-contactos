# Libreta de Contactos en Python con Tkinter

Una aplicación de escritorio simple para gestionar contactos, desarrollada en Python con una interfaz gráfica creada usando Tkinter. Permite agregar, ver, actualizar, eliminar y guardar contactos en un archivo JSON.

La aplicación se lanza a través de una pantalla de inicio que también utiliza Tkinter.

## Características Implementadas

* **Pantalla de Inicio:** Una ventana principal que permite lanzar la aplicación de Libreta de Contactos.
* **Agregar Contactos:** Permite ingresar nombre, teléfono y email para un nuevo contacto.
* **Ver Contactos:** Muestra una lista de todos los contactos guardados.
* **Mostrar Detalles:** Al seleccionar un contacto de la lista, sus detalles se muestran en los campos de edición.
* **Actualizar Contactos:** Modificar la información de un contacto existente.
* **Eliminar Contactos:** Borrar un contacto de la libreta (con confirmación).
* **Persistencia de Datos:** Los contactos se guardan en un archivo `contactos.json`, permitiendo que la información persista entre sesiones.
* **Interfaz Gráfica de Usuario (GUI):** Creada con Tkinter para una interacción más amigable.

## Tecnologías Utilizadas

* **Python 3**
* **Tkinter:** Para la interfaz gráfica de usuario.
* **JSON:** Para el almacenamiento y persistencia de los datos de contacto.

## Requisitos

* Python 3.x instalado en tu sistema.

## Cómo Ejecutar la Aplicación

1.  **Clona o descarga este repositorio:**
    ```bash
    # Si usas git
    git clone URL_DE_TU_REPOSITORIO
    cd NOMBRE_DE_LA_CARPETA_DEL_PROYECTO
    ```
    O simplemente descarga los archivos `.py` en una carpeta en tu computadora.

2.  **Asegúrate de que los archivos `inicio.py` y `libreta_contactos.py` estén en la misma carpeta.**

3.  **Abre una terminal o símbolo del sistema** en esa carpeta.

4.  **Ejecuta el script de inicio:**
    ```bash
    python inicio.py
    ```
    o si tienes configurado `python3`:
    ```bash
    python3 inicio.py
    ```
5.  Esto abrirá la ventana de "Programa de Inicio". Desde allí, podrás lanzar la "Libreta de Contactos".

## Estructura de Archivos

* `inicio.py`: Script principal que lanza la aplicación. Contiene la GUI de inicio.
* `libreta_contactos.py`: Módulo que contiene toda la lógica y la GUI de la aplicación de libreta de contactos.
* `contactos.json`: Archivo de datos donde se guardan los contactos (se crea automáticamente al guardar por primera vez).

## Posibles Mejoras Futuras (TODO)

* [ ] Implementar funcionalidad de búsqueda/filtrado de contactos.
* [ ] Añadir un botón "Limpiar Campos" en el formulario de contactos.
* [ ] Mejorar las validaciones para los campos de teléfono y email.
* [ ] Permitir ordenar los contactos en la lista (por nombre, etc.).
* [ ] Añadir más campos de información para cada contacto (dirección, cumpleaños, etc.).
* [ ] Refactorizar el código de `libreta_contactos.py` utilizando clases para una mejor organización.

---

Desarrollado por: Matias Frutos
Fecha de última actualización: 21 de Mayo, 2025.
