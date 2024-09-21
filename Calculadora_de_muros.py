import tkinter as tk
from tkinter import messagebox, Menu, ttk, font
import threading
import time

class CalculadoraMaterialesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Construcción")
        self.root.configure(bg='#333333')
        self.centrar_ventana(390, 500)
        self.root.resizable(True, True)

        self.nombre = tk.StringVar()

        self.crear_menu()
        self.crear_pantalla_inicio()

    def centrar_ventana(self, ancho, alto):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (ancho / 2))
        y_cordinate = int((screen_height / 2) - (alto / 2))
        self.root.geometry(f"{ancho}x{alto}+{x_cordinate}+{y_cordinate}")

    # CONFIGURACION DE MENU DESPLEGABLE Y ACERCA DE
    def crear_menu(self):
        menu_bar = Menu(self.root)

        menu_deplegable = Menu(menu_bar, tearoff=0)
        menu_deplegable.add_command(label="Acerca de...", command=self.acerca_de)
        menu_deplegable.add_separator()
        menu_deplegable.add_command(label="Salir", command=self.root.quit)

        menu_bar.add_cascade(label="Menú ▼", menu=menu_deplegable)

        self.root.config(menu=menu_bar)

    def acerca_de(self):
        messagebox.showinfo("Acerca de", "Calculadora de materiales de Construcción para muros\n\nComisión 6 - Grupo 7 \nIntegrantes:\nBrian Alexander Czajka\nEduardo Lopez Goitia\nDavid\nDenise\nLucas Leonczyk\nRosana Mandziuk")
    # def acerca_de(self):
    #     messagebox.showinfo("Acerca de", "Calculadora de materiales de Construcción para muros\n\nIntegrantes:\nBrian Alexander Czajka\nEduu Lopez Goitia\nDavid\nDenise\nLucas Leonczyk\nRosana Mandziuk")

    # Fin configuracion de menu desplegable y acerca de

    def crear_pantalla_inicio(self):
        frame_inicio = tk.Frame(self.root, bg='#333333', padx=5, pady=5)
        frame_inicio.pack(fill="both", expand=True)

        tk.Label(frame_inicio, text="Bienvenido a la calculadora de materiales de muros \n \nPor favor ingrese su nombre:", bg='#333333', fg='white').pack(pady=10)
        nombre_entry = tk.Entry(frame_inicio, textvariable=self.nombre)
        nombre_entry.pack(pady=5)

        comenzar_btn = tk.Button(frame_inicio, text="Comenzar", command=self.abrir_calculadora, bg='#FFE500', fg='black', activebackground='#939598')
        comenzar_btn.pack(pady=20)

    def abrir_calculadora(self):
        nombre = self.nombre.get()
        if not nombre:
            messagebox.showerror("Error", "Bienvenido a la calculadora de materiales de muros \nPor favor ingrese su nombre.")
            return

        self.root.withdraw()

        calculadora_root = tk.Toplevel(self.root)
        calculadora = CalculadoraMateriales(calculadora_root, nombre)
        calculadora_root.mainloop()

        # Al iniciar la segunda ventana, Cierra la primera
        self.root.destroy()

class CalculadoraMateriales:
    def __init__(self, root, nombre):
        self.root = root
        self.root.title(f"Calculadora de Materiales para Muros - Bienvenido {nombre}")
        self.root.configure(bg='#333333')
        self.centrar_ventana(390, 500)
        self.root.resizable(True, True)

        self.tipo_muro_var = tk.StringVar(value="Elija una opción")
        self.tipo_material_var = tk.StringVar(value="Elija una opción")

        self.crear_menu()
        self.crear_interfaz(nombre)

    def centrar_ventana(self, ancho, alto):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (ancho / 2))
        y_cordinate = int((screen_height / 2) - (alto / 2))
        self.root.geometry(f"{ancho}x{alto}+{x_cordinate}+{y_cordinate}")

    def crear_menu(self):
        menu_bar = Menu(self.root)

        menu_deplegable = Menu(menu_bar, tearoff=0)
        menu_deplegable.add_command(label="Acerca de...", command=self.acerca_de)
        menu_deplegable.add_separator()
        menu_deplegable.add_command(label="Salir", command=self.root.quit)

        menu_bar.add_cascade(label="Menú ▼", menu=menu_deplegable)

        self.root.config(menu=menu_bar)

    def acerca_de(self):
        messagebox.showinfo("Acerca de", "Calculadora de materiales de Construcción para muros\n\nComisión 6 - Grupo 7 \nIntegrantes:\nBrian Alexander Czajka\nEduardo Lopez Goitia\nAlejandro David Jara\nDenise Drocezesky\nLucas Leonczyk\nRosana Mandziuk")

    def crear_interfaz(self, nombre):
        frame = tk.Frame(self.root, bg='#333333', padx=5, pady=5)
        frame.pack(fill="both", expand=True)

        saludo_label = tk.Label(frame, text=f"Hola {nombre}, calculemos!!!", bg='#333333', fg='white', font=("Roboto", 18))
        saludo_label.pack(pady=10)

        tk.Label(frame, text="Seleccione el tipo de muro:", bg='#333333', fg='white').pack(pady=5)
        menu_tipo_muro = ttk.Combobox(frame, textvariable=self.tipo_muro_var, values=["Exterior", "Interior"])
        menu_tipo_muro.pack(pady=5)
        menu_tipo_muro.configure(font=("Roboto Italic", 10))

        tk.Label(frame, text="Seleccione el tipo de material:", bg='#333333', fg='white').pack(pady=5)
        menu_tipo_material = ttk.Combobox(frame, textvariable=self.tipo_material_var, values=["Ladrillos Comunes", "Ladrillos Huecos"])
        menu_tipo_material.pack(pady=5)
        menu_tipo_material.configure(font=("Roboto Italic", 10))

        tk.Label(frame, text="Ingrese la superficie a construir en m2:", bg='#333333', fg='white').pack(pady=5)
        self.superficie_entry = tk.Entry(frame)
        self.superficie_entry.pack(pady=5)

        calcular_btn = tk.Button(frame, text="Calcular", command=self.iniciar_calculo, bg='#FFE500', fg='black', activebackground='#939598')
        calcular_btn.pack(pady=10)

        limpiar_btn = tk.Button(frame, text="Limpiar", command=self.limpiar, bg='#FF6F6F', fg='white', activebackground='#939598')
        limpiar_btn.pack(pady=5)

        self.resultado_label = tk.Label(frame, text="", justify="left", bg='#333333', fg='white')
        self.resultado_label.pack(pady=10)

        # Barra de progreso
        self.progress = ttk.Progressbar(frame, mode="determinate", length=200)
        self.progress.pack(pady=10)
        self.progress.pack_forget()

    def iniciar_calculo(self):
        self.progress.pack()
        self.progress.start()

        # Se Inicia la barra de progreso con delay para mostrar el resultado
        threading.Thread(target=self.calcular_con_delay, daemon=True).start()

    def calcular_con_delay(self):
        # Delay
        for _ in range(70):
            time.sleep(0.025)
            self.root.after(0, self.progress.step, 1)

        # Llamo al método de calcular y detengo la barra de progreso
        self.root.after(0, self.calcular)
        self.root.after(0, self.detener_progreso)

    # Método para detener la barra de progreso
    def detener_progreso(self):
        self.progress.stop()
        self.progress.pack_forget()

    def calcular(self):
        tipo_muro = self.tipo_muro_var.get().lower()
        tipo_material = self.tipo_material_var.get().lower()
        if tipo_muro == "Elija una opción" or tipo_material == "Elija una opción":
            messagebox.showerror("Error", "Por favor, elija el tipo de muro y el material.")
            return

        try:
            m2 = float(self.superficie_entry.get())
        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor ingrese un número válido para la superficie.")
            return

        # Calcular los materiales
        materiales = self.calcular_materiales(tipo_muro, tipo_material, m2)
        if materiales:
            self.mostrar_resultado(materiales)
        else:
            messagebox.showerror("Error", "Error en el cálculo de materiales.")
            
    def centrar_ventana_resultados(self, ventana, ancho, alto):
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (ancho / 2))
        y_cordinate = int((screen_height / 2) - (alto / 2))
        ventana.geometry(f"{ancho}x{alto}+{x_cordinate}+{y_cordinate}")      
         
    # Ventana emergente personalizada
    def mostrar_resultado(self, materiales):
        ventana_resultado = tk.Toplevel(self.root)
        ventana_resultado.title("Resultado")
        ventana_resultado.configure(bg='#333333')  # Fondo de la ventana
        
        # Tamaño de la ventana emergente
        ancho_ventana = 300
        alto_ventana = 200   
         
        # Centrar la ventana
        self.centrar_ventana_resultados(ventana_resultado, ancho_ventana, alto_ventana) 
        
        # Etiqueta con el resultado
        resultado_label = tk.Label(ventana_resultado, text="Ud. necesitará:", bg='#333333', fg='white', font=("Roboto", 12))
        resultado_label.pack(pady=10)

        # Lista de materiales con estilo
        materiales_text = f"- {materiales['ladrillos']} unidades de ladrillos\n" \
                        f"- {materiales['cemento']} kg de cemento\n" \
                        f"- {materiales['cal']} kg de cal\n" \
                        f"- {materiales['arena']} m³ de arena"

        materiales_label = tk.Label(ventana_resultado, text=materiales_text, bg='#333333', fg='white', justify="left")
        materiales_label.pack(pady=10)

        # Botón de cerrar
        cerrar_btn = tk.Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy)
        cerrar_btn.pack(pady=10)

    # Función de cálculo de materiales
    def calcular_materiales(self, tipo_muro, tipo_material, m2):
        factor_ladrillos = 60 if tipo_material == "ladrillos comunes" else 45
        factor_cemento = 7
        factor_cal = 3
        factor_arena = 0.05

        ladrillos = int(m2 * factor_ladrillos)
        cemento = int(m2 * factor_cemento)
        cal = int(m2 * factor_cal)
        arena = round(m2 * factor_arena, 2)

        return {
            "ladrillos": ladrillos,
            "cemento": cemento,
            "cal": cal,
            "arena": arena
        }

    def limpiar(self):
        self.tipo_muro_var.set("Elija una opción")
        self.tipo_material_var.set("Elija una opción")
        self.superficie_entry.delete(0, tk.END)
        self.resultado_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraMaterialesApp(root)
    root.mainloop()
