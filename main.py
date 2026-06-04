import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import time

# Configuración de apariencia profesional y accesible
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class GymPythonApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gym Python - Entrenamiento para Principiantes")
        self.geometry("1000x800")

        self.conceptos = [
            {"nombre": "Planificación de Lógica (Comentarios)", "explicacion": "El símbolo '#' se utiliza para escribir comentarios. Estos son ignorados por Python y sirven para planificar la estructura del código.", "codigo": "# Paso 1: Definir las variables de entrada"},
            {"nombre": "Mostrar Información (print)", "explicacion": "La función print() muestra texto o resultados en la pantalla.", "codigo": 'print("Iniciando aplicacion de calculadora...")'},
            {"nombre": "Almacenar Datos (Variables)", "explicacion": "Las variables se usan para guardar datos en la memoria. El signo '=' asigna valores.", "codigo": 'primer_numero = 10'},
            {"nombre": "Recibir Datos (input)", "explicacion": "La función input() pausa el programa y espera a que el usuario escriba algo.", "codigo": 'opcion = input("Seleccione una operacion (1-4): ")'},
            {"nombre": "Números con Decimales (float)", "explicacion": "Convierte texto en números decimales para realizar operaciones matemáticas.", "codigo": 'valor = float(input("Escriba un numero: "))'},
            {"nombre": "Valores Lógicos (Booleanos)", "explicacion": "Tipos de datos que solo pueden ser True o False. Controlan el estado del programa.", "codigo": 'continuar_programa = True'},
            {"nombre": "Condiciones y Decisiones (if)", "explicacion": "Evalúa si una condición es verdadera para ejecutar un bloque de código.", "codigo": 'if opcion == "1":'},
            {"nombre": "Repetición Continua (while True)", "explicacion": "Crea un bucle infinito para que el programa sea persistente.", "codigo": 'while True:'},
            {"nombre": "Terminar Ejecución (break)", "explicacion": "Instrucción para salir inmediatamente de un bucle.", "codigo": 'break'}
        ]

        self.indice_actual = 0
        self.repeticiones_actuales = 0
        self.meta_repeticiones = 15

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.header = ctk.CTkFrame(self)
        self.header.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        self.label_titulo = ctk.CTkLabel(self.header, text="MODO DE ENTRENAMIENTO", font=("Segoe UI", 22, "bold"))
        self.label_titulo.pack(pady=15)

        self.container = ctk.CTkFrame(self)
        self.container.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        
        self.setup_ui()

    def setup_ui(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        self.label_concepto = ctk.CTkLabel(self.container, text="", font=("Segoe UI", 20, "bold"), text_color="#3b8ed0")
        self.label_concepto.pack(pady=10)

        self.text_explicacion = ctk.CTkTextbox(self.container, height=100, font=("Segoe UI", 15), wrap="word")
        self.text_explicacion.pack(fill="x", padx=60, pady=10)

        self.label_codigo = ctk.CTkLabel(self.container, text="", font=("Consolas", 24), fg_color="#1a1a1a", corner_radius=8)
        self.label_codigo.pack(pady=20, padx=60, fill="x")

        self.progreso_rep = ctk.CTkProgressBar(self.container, width=600, progress_color="#2ecc71")
        self.progreso_rep.pack(pady=10)

        self.label_contador = ctk.CTkLabel(self.container, text="0/15")
        self.label_contador.pack()

        self.entry_input = ctk.CTkEntry(self.container, placeholder_text="Escriba el código aquí...", width=600, height=45, font=("Consolas", 18))
        self.entry_input.pack(pady=20)
        self.entry_input.bind("<Return>", self.verificar)
        self.entry_input.focus()

        self.cargar()

    def cargar(self):
        if self.indice_actual < len(self.conceptos):
            c = self.conceptos[self.indice_actual]
            self.label_concepto.configure(text=c["nombre"])
            self.text_explicacion.delete("1.0", tk.END)
            self.text_explicacion.insert("1.0", c["explicacion"])
            self.label_codigo.configure(text=f" {c['codigo']} ")
            self.repeticiones_actuales = 0
            self.actualizar_stats()
        else:
            self.setup_mision_calculadora()

    def verificar(self, event=None):
        objetivo = self.conceptos[self.indice_actual]["codigo"]
        intento = self.entry_input.get().strip()

        if intento == "cd..":
            self.indice_actual += 1
            self.cargar()
            self.entry_input.delete(0, tk.END)
            return

        if intento == objetivo:
            self.repeticiones_actuales += 1
            self.actualizar_stats()
            self.entry_input.delete(0, tk.END)
            if self.repeticiones_actuales >= self.meta_repeticiones:
                self.indice_actual += 1
                self.cargar()
        else:
            self.label_codigo.configure(fg_color="#4a1a1a")
            self.after(150, lambda: self.label_codigo.configure(fg_color="#1a1a1a"))

    def actualizar_stats(self):
        p = self.repeticiones_actuales / self.meta_repeticiones
        self.progreso_rep.set(p)
        self.label_contador.configure(text=f"Repeticiones completadas: {self.repeticiones_actuales}/{self.meta_repeticiones}")

    def setup_mision_calculadora(self):
        for widget in self.container.winfo_children():
            widget.destroy()

        self.label_titulo.configure(text="RETO FINAL: CONSTRUCCIÓN DE SCRIPT")
        
        texto_instrucciones = "Siga los comentarios (#) como guía. Escriba 'reveal' para ver el código o 'hide' para ocultarlo."
        ctk.CTkLabel(self.container, text=texto_instrucciones, font=("Segoe UI", 15)).pack(pady=10)

        self.txt_calculadora = ctk.CTkTextbox(self.container, height=400, font=("Consolas", 14))
        self.txt_calculadora.pack(fill="both", padx=60, pady=10, expand=True)
        self.txt_calculadora.bind("<KeyRelease>", self.check_commands)
        
        self.guia_inicial = (
            "# PISTA: Para convertir este script a ejecutable (.exe) se utiliza la librería: pyinstaller\n"
            "\n"
            "# 1. Iniciar un bucle infinito para que el programa sea persistente\n\n\n"
            "# 2. Solicitar al usuario la operación deseada (+, -, *, /) o salir (s)\n\n\n"
            "# 3. Implementar la salida del programa mediante break\n\n\n"
            "# 4. Capturar dos números del usuario y convertirlos a tipo float\n\n\n"
            "# 5. Utilizar if y elif para procesar el cálculo y mostrar el resultado con print\n"
        )
        self.txt_calculadora.insert("1.0", self.guia_inicial)

        self.btn_probar = ctk.CTkButton(self.container, text="EJECUTAR SCRIPT", command=self.consola_interactiva, fg_color="#2ecc71", font=("Segoe UI", 14, "bold"))
        self.btn_probar.pack(pady=20)

    def check_commands(self, event=None):
        content = self.txt_calculadora.get("1.0", tk.END).strip()
        if content.endswith("reveal"):
            solucion = (
                "# CODIGO COMPLETO REVELADO\n"
                "while True:\n"
                "    op = input('Operacion (+, -, *, /) o s para salir: ')\n"
                "    if op == 's':\n"
                "        break\n"
                "    n1 = float(input('Numero 1: '))\n"
                "    n2 = float(input('Numero 2: '))\n"
                "    if op == '+':\n"
                "        print('Resultado:', n1 + n2)\n"
                "    elif op == '-':\n"
                "        print('Resultado:', n1 - n2)\n"
                "    elif op == '*':\n"
                "        print('Resultado:', n1 * n2)\n"
                "    elif op == '/':\n"
                "        if n2 != 0: print('Resultado:', n1 / n2)\n"
                "        else: print('Error: Div por cero')\n"
            )
            self.txt_calculadora.delete("1.0", tk.END)
            self.txt_calculadora.insert("1.0", solucion)
        elif content.endswith("hide"):
            self.txt_calculadora.delete("1.0", tk.END)
            self.txt_calculadora.insert("1.0", self.guia_inicial)

    def consola_interactiva(self):
        # Ventana de consola realmente interactiva
        win = ctk.CTkToplevel(self)
        win.title("Consola de Sistema - Ejecución Interactiva")
        win.geometry("600x500")
        win.attributes("-topmost", True)

        log = ctk.CTkTextbox(win, fg_color="black", text_color="white", font=("Consolas", 12), height=350)
        log.pack(fill="x", padx=20, pady=10)
        log.insert(tk.END, "> Iniciando calculadora.py...\n")

        # Frame para entrada del usuario
        input_frame = ctk.CTkFrame(win, fg_color="black")
        input_frame.pack(fill="x", padx=20)

        lbl_prompt = ctk.CTkLabel(input_frame, text=">>> ", text_color="#00FF00", font=("Consolas", 12))
        lbl_prompt.pack(side="left")

        user_entry = ctk.CTkEntry(input_frame, fg_color="#1a1a1a", text_color="white", font=("Consolas", 12), border_width=0)
        user_entry.pack(side="left", fill="x", expand=True)
        user_entry.focus()

        # Estado de la calculadora simulada
        self.sim_step = "op"
        self.sim_op = ""
        self.sim_n1 = 0.0

        def procesar_input(event=None):
            val = user_entry.get().strip()
            user_entry.delete(0, tk.END)
            
            if self.sim_step == "op":
                log.insert(tk.END, f"Operacion (+, -, *, /) o s para salir: {val}\n")
                if val == 's':
                    log.insert(tk.END, "> Programa finalizado.\n")
                    user_entry.configure(state="disabled")
                else:
                    self.sim_op = val
                    self.sim_step = "n1"
            elif self.sim_step == "n1":
                log.insert(tk.END, f"Numero 1: {val}\n")
                try:
                    self.sim_n1 = float(val)
                    self.sim_step = "n2"
                except: log.insert(tk.END, "Error: Ingrese un numero valido.\n")
            elif self.sim_step == "n2":
                log.insert(tk.END, f"Numero 2: {val}\n")
                try:
                    n2 = float(val)
                    res = 0.0
                    if self.sim_op == '+': res = self.sim_n1 + n2
                    elif self.sim_op == '-': res = self.sim_n1 - n2
                    elif self.sim_op == '*': res = self.sim_n1 * n2
                    elif self.sim_op == '/': 
                        if n2 != 0: res = self.sim_n1 / n2
                        else: res = "Error (Div por cero)"
                    
                    log.insert(tk.END, f"Resultado: {res}\n\n")
                    self.sim_step = "op"
                except: log.insert(tk.END, "Error: Ingrese un numero valido.\n")
            
            log.see(tk.END)

        user_entry.bind("<Return>", procesar_input)

if __name__ == "__main__":
    app = GymPythonApp()
    app.mainloop()
