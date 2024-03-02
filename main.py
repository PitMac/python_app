import tkinter as tk
from tkinter import messagebox
from datetime import date

class AplicacionTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Primera Pantalla")
        self.root.geometry("900x700")

        # Crear un botón en la primera pantalla
        # btn_ir_a_solicitud = tk.Button(root, text="Crear solicitud", command=self.ir_a_solicitud)
        # btn_ir_a_solicitud.pack(pady=20)

        self.item_var = tk.StringVar()
        self.fecha_var = tk.StringVar(value=date.today().strftime("%Y-%m-%d"))
        self.proyecto_var = tk.StringVar()
        self.solicitante_var = tk.StringVar()
        self.cantidad_postes_var = tk.StringVar()
        self.cantidad_transformadores_var = tk.StringVar()

        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=(20, 5), padx=20, anchor="w")  # Alinear a la izquierda


        self.crear_entry_y_etiqueta(main_frame, "Item:", self.item_var)
        self.crear_entry_y_etiqueta(main_frame, "Fecha:", self.fecha_var)
        self.crear_entry_y_etiqueta(main_frame, "Proyecto:", self.proyecto_var)
        self.crear_entry_y_etiqueta(main_frame, "Solicitante:", self.solicitante_var)
        self.crear_entry_y_etiqueta(main_frame, "Cantidad de Postes:", self.cantidad_postes_var, solo_numero=True)
        self.crear_entry_y_etiqueta(main_frame, "Cantidad de Transformadores:", self.cantidad_transformadores_var, solo_numero=True)


    def crear_entry_y_etiqueta(self, frame, texto, variable, solo_numero=False):
            sub_frame = tk.Frame(frame)
            sub_frame.pack(pady=5, side="top")

            etiqueta = tk.Label(sub_frame, text=texto, font=(12))
            etiqueta.grid(row=0, column=0, sticky="w", padx=5)

            if solo_numero:
                entry = tk.Entry(sub_frame, textvariable=variable, validate="key", validatecommand=(frame.register(self.validate_numero), "%P"), font=(12))
            else:
                entry = tk.Entry(sub_frame, textvariable=variable, font=(12))

            entry.grid(row=0, column=1, padx=5)

    def validate_numero(self, valor):
        # Validar que solo se ingresen números en los Entry de cantidad
        if valor == "" or valor.isdigit():
            return True
        return False


    def ir_a_solicitud(self):
        # Ocultar la primera pantalla
        self.root.withdraw()

        # Crear la segunda pantalla
        segunda_pantalla = tk.Toplevel(self.root)
        SegundaPantalla(segunda_pantalla)

class SegundaPantalla:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x700")
        self.root.title("Segunda Pantalla")

        # Crear un formulario en la segunda pantalla
        etiqueta_nombre = tk.Label(root, text="Nombre:")
        etiqueta_nombre.pack(pady=10)

        entry_nombre = tk.Entry(root)
        entry_nombre.pack(pady=10)

        btn_enviar = tk.Button(root, text="Enviar", command=lambda: self.enviar_formulario(entry_nombre.get()))
        btn_enviar.pack(pady=10)

    def enviar_formulario(self, nombre):
        messagebox.showinfo("Formulario Enviado", f"Nombre: {nombre}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTkinter(root)
    root.mainloop()
