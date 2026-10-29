import tkinter as tk
from tkinter import ttk, messagebox

# --- CLASE BASE: COLA ---
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# --- FUNCIÓN DEL PROBLEMA 1 ---
def sumar_colas(cola_a, cola_b):
    cola_resultado = Cola()
    temp_a = Cola()
    temp_b = Cola()
    
    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        val_a = cola_a.desencolar()
        val_b = cola_b.desencolar()
        cola_resultado.encolar(val_a + val_b)
        temp_a.encolar(val_a)
        temp_b.encolar(val_b)
        
    while not temp_a.esta_vacia():
        cola_a.encolar(temp_a.desencolar())
    while not temp_b.esta_vacia():
        cola_b.encolar(temp_b.desencolar())
        
    return cola_resultado


# --- VENTANA GRÁFICA PRINCIPAL ---
class AppColasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Colas - Aplicación Gráfica")
        self.root.geometry("680x480")
        self.root.config(bg="#f4f6f9")

        # 1. INICIALIZAR LAS VARIABLES PRIMERO (¡Aquí estaba el detalle!)
        self.colas_seguros = {}
        self.turnos_totales = {}

        # Estilo visual
        style = ttk.Style()
        style.theme_use("clam")

        # Pestañas principales de la ventana
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True, padx=12, pady=12)

        self.tab1 = ttk.Frame(notebook)
        self.tab2 = ttk.Frame(notebook)
        
        notebook.add(self.tab1, text=" 🧮 Problema 1: Suma de Colas ")
        notebook.add(self.tab2, text=" 🏢 Problema 2: Compañía de Seguros ")

        self.setup_tab1()
        self.setup_tab2()

    # ================= PESTAÑA 1 =================
    def setup_tab1(self):
        lbl_title = tk.Label(self.tab1, text="Suma de Dos Colas Elemento a Elemento", font=("Arial", 12, "bold"), bg="#f4f6f9", fg="#333")
        lbl_title.pack(pady=15)

        frame_inputs = ttk.LabelFrame(self.tab1, text=" Datos de Entrada (separados por comas) ")
        frame_inputs.pack(fill="x", padx=20, pady=10)

        tk.Label(frame_inputs, text="Cola A:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.entry_a = ttk.Entry(frame_inputs, width=45, font=("Arial", 10))
        self.entry_a.insert(0, "3, 4, 2, 8, 12")
        self.entry_a.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame_inputs, text="Cola B:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.entry_b = ttk.Entry(frame_inputs, width=45, font=("Arial", 10))
        self.entry_b.insert(0, "6, 2, 9, 11, 3")
        self.entry_b.grid(row=1, column=1, padx=10, pady=10)

        btn_calcular = ttk.Button(self.tab1, text="Calcular Suma en Cola", command=self.calcular_suma)
        btn_calcular.pack(pady=10)

        frame_results = ttk.LabelFrame(self.tab1, text=" Resultados ")
        frame_results.pack(fill="both", expand=True, padx=20, pady=10)

        self.lbl_res_a = tk.Label(frame_results, text="Cola A: [ ]", font=("Arial", 11), bg="white", anchor="w")
        self.lbl_res_a.pack(fill="x", padx=15, pady=8)

        self.lbl_res_b = tk.Label(frame_results, text="Cola B: [ ]", font=("Arial", 11), bg="white", anchor="w")
        self.lbl_res_b.pack(fill="x", padx=15, pady=8)

        self.lbl_res_final = tk.Label(frame_results, text="Cola Resultado: [ ]", font=("Arial", 11, "bold"), bg="white", fg="#0056b3", anchor="w")
        self.lbl_res_final.pack(fill="x", padx=15, pady=10)

    def calcular_suma(self):
        try:
            vals_a = [int(x.strip()) for x in self.entry_a.get().split(",") if x.strip()]
            vals_b = [int(x.strip()) for x in self.entry_b.get().split(",") if x.strip()]

            cola_a = Cola()
            for v in vals_a: cola_a.encolar(v)

            cola_b = Cola()
            for v in vals_b: cola_b.encolar(v)

            res = sumar_colas(cola_a, cola_b)

            self.lbl_res_a.config(text=f"Cola A:         {cola_a.items}")
            self.lbl_res_b.config(text=f"Cola B:         {cola_b.items}")
            self.lbl_res_final.config(text=f"Cola Resultado: {res.items}")
        except Exception as e:
            messagebox.showerror("Error de Formato", f"Ingresa solo números enteros separados por comas.\nDetalle: {e}")

    # ================= PESTAÑA 2 =================
    def setup_tab2(self):
        lbl_title = tk.Label(self.tab2, text="Simulador de Turnos - Compañía de Seguros", font=("Arial", 12, "bold"), bg="#f4f6f9", fg="#333")
        lbl_title.pack(pady=15)

        frame_control = ttk.LabelFrame(self.tab2, text=" Panel de Operaciones ")
        frame_control.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_control, text="Servicio (Ej: 1, 2...):", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=12)
        self.entry_servicio = ttk.Entry(frame_control, width=10, font=("Arial", 10))
        self.entry_servicio.insert(0, "1")
        self.entry_servicio.grid(row=0, column=1, padx=10, pady=12)

        btn_llegada = ttk.Button(frame_control, text="➕ Llegada Cliente (C)", command=self.gui_llegada)
        btn_llegada.grid(row=0, column=2, padx=10, pady=12)

        btn_atender = ttk.Button(frame_control, text="📢 Atender Siguiente (A)", command=self.gui_atender)
        btn_atender.grid(row=0, column=3, padx=10, pady=12)

        frame_display = ttk.LabelFrame(self.tab2, text=" Clientes en Espera por Servicio ")
        frame_display.pack(fill="both", expand=True, padx=20, pady=10)

        self.txt_estado = tk.Text(frame_display, height=7, width=65, font=("Courier New", 10))
        self.txt_estado.pack(padx=10, pady=10, fill="both", expand=True)
        self.actualizar_vista_seguros()

    def gui_llegada(self):
        srv = self.entry_servicio.get().strip()
        if not srv.isdigit():
            messagebox.showwarning("Advertencia", "El número de servicio debe ser numérico.")
            return
        
        if srv not in self.colas_seguros:
            self.colas_seguros[srv] = Cola()
            self.turnos_totales[srv] = 0

        self.turnos_totales[srv] += 1
        ticket = self.turnos_totales[srv]
        self.colas_seguros[srv].encolar(ticket)
        self.actualizar_vista_seguros()

    def gui_atender(self):
        srv = self.entry_servicio.get().strip()
        if srv not in self.colas_seguros or self.colas_seguros[srv].esta_vacia():
            messagebox.showinfo("Aviso", f"No hay clientes en espera para el Servicio {srv}.")
            return
        
        ticket = self.colas_seguros[srv].desencolar()
        messagebox.showinfo("Atención en Curso", f"Llamando al cliente número #{ticket} del Servicio {srv}")
        self.actualizar_vista_seguros()

    def actualizar_vista_seguros(self):
        self.txt_estado.delete("1.0", tk.END)
        if not self.colas_seguros:
            self.txt_estado.insert(tk.END, "No hay servicios activos registrados.\nHaz clic en 'Llegada Cliente' para comenzar.")
            return
        
        for s, cola in self.colas_seguros.items():
            self.txt_estado.insert(tk.END, f"• Servicio [{s}] -> Clientes formados: {cola.items}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = AppColasGUI(root)
    root.mainloop()