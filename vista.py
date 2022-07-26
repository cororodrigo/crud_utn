import modelo
from modelo import *
import tkinter as tk
from tkinter import DISABLED, END, NORMAL 
from tkinter import Button, Entry, Label
from tkinter import Menu, Scrollbar, messagebox
from tkinter import ttk
from decorador import advertencia



class home_app():
    def __init__(self, root):
        self.home = root
        self.home.title("App Dbase jugadores Lima Pro")
        self.home.geometry("680x540")
        self.barra_menu = tk.Menu (self.home)
        self.home.config(
            menu=self.barra_menu, 
            width=780, 
            height=620, 
            bg="green"
        )
        self.dbase = modelo.BaseModel()
        self.dbase_operativo = modelo.lbf_registros()
        self.la_base = modelo.base_lbf()
        
        
        #------ barra menu
        self.a_menu = Menu (self.home, 
        tearoff=0
        )
        self.a_menu.add_command(
            label= "Salir de la APP", 
            command=self.salir_app
        )        
        self.barra_menu.add_cascade(
            label="Archivo", 
            menu=self.a_menu
        )

         #----Labels y Entrys
        self.l_dni = Label(
            self.home, 
            text="D.N.I.: ", 
            font=("calibri", 13, "bold"), 
            fg="white",
            bg="green"
        )
        self.l_dni.grid(
            row=0, 
            column=0, 
            padx=10, 
            pady=10
        )
        self.dni = tk.IntVar(value=1)
        self.dni.set(
            "Ingrese DNI sin puntos"
        )
        self.e_dni = Entry(self.home, 
        textvariable=self.dni
        )
        self.e_dni.config(
            font=("calibri", 10), 
            state=DISABLED
        )
        self.e_dni.grid(
            row=0, 
            column=1
        )
        self.e_dni.bind("<Double-1>",
                lambda event: self.habilita_entry_dni()
            )
        self.l_ape = Label(
            self.home, text="Apellido: ", 
            font=("calibri", 13, "bold"), 
            fg="white",
            bg="green"
        )
        self.l_ape.grid(
            row=1, 
            column=0
        )
        self.ap = tk.StringVar()
        self.e_ape = Entry(self.home, 
        textvariable=self.ap
        )
        self.e_ape.grid(
            row=1, 
            column=1
        )
        self.e_ape.config(
            font=("calibri", 10)
        )
        self.ap.trace_add("write", lambda *args:
            self.ap.set(self.ap.get().upper()))
        
        self.l_nomb = Label(
            self.home, text="Nombre: ", 
            font=("calibri", 13, "bold"), 
            fg="white", 
            bg="green"
        )
        self.l_nomb.grid(
            row=1, 
            column=3
        )

        self.nomb = tk.StringVar()        
        self.e_nomb = Entry(self.home, 
        textvariable=self.nomb
        )
        self.e_nomb.config(
            font=("calibri", 10)
        )
        self.e_nomb.grid(
            row=1, 
            column=4
        )
        self.nomb.trace_add("write", lambda *args:
            self.nomb.set(self.nomb.get().capitalize()))

        self.l_fnac = Label(self.home, 
            text="Fecha Nac: ", 
            font=("calibri", 13, "bold"), 
            fg="white",
            bg="green"
        )
        self.l_fnac.grid(
            row=0, 
            column=3
        )
        self.fnac = tk.StringVar()
        self.fnac.set("DD-MM-AAAA")         
        self.e_fnac = Entry(self.home, 
        textvariable=self.fnac
        )
        self.e_fnac.grid(
            row=0, 
            column=4, 
            padx=10, 
            pady=10
        )
        self.e_fnac.config(
            font=("calibri", 10), 
            state=DISABLED)
        self.e_fnac.bind("<Double-1>",
                lambda event: self.habilita_entry_fecha())       
        
        #----Botones
        self.b_agregar = Button(self.home,
            text="Agregar Jugador",
            font=("calibri", 12),
            bg="yellowgreen",
            fg="white",
            cursor="hand2",
            command=self.agregar_jugador
        )
        self.b_agregar.grid(
            row=4, 
            column=0, 
            padx=10, 
            pady=10
        )

        self.b_modificar = Button(
            self.home,
            text="Modificar datos",
            font=("calibri", 12),
            bg="yellowgreen",
            fg="white",
            cursor="hand2",
            command=self.modificar_jugador
        )
        self.b_modificar.grid(
            row=4, 
            column=5, 
            padx=10, 
            pady=10
        )

        self.b_eliminar = Button(self.home,
            text="Borrar Jugador", 
            font=("calibri", 12),
            bg="yellowgreen",
            fg="white",
            cursor="hand2",
            command=self.eliminar_jugador
        )
        self.b_eliminar.grid(
            row=6, 
            column=5, 
            padx=10, 
            pady=10
        )

        self.b_panel = Button(self.home,
            text="Panel en blanco", 
            font=("calibri", 12),
            bg="yellowgreen",
            fg="white",
            cursor="hand2",
            command=self.borra_panel_de_los_entry
        )
        self.b_panel.grid(
            row=6, 
            column=0, 
            padx=10, 
            pady=10
        )
         #---Tabla
        self.style = ttk.Style(self.home)
        self.style.theme_use("clam")
        self.style.configure(
            "Treeview", 
            background="white", 
            fieldbackground="white", 
            foreground="black"
        )
        self.style.configure(
            "Treeview.Heading",
            background="green",
            fieldbackground="#5FE884",
            foreground="white",
            font=("Calibri", 10, "bold"),
        )
        self.tabla_lbf = ttk.Treeview(self.home, 
            height=15
            )
        self.tabla_lbf ["columns"] = ("dni","nomb", "ape", "fnac")
        self.tabla_lbf.grid(
            row=5, 
            column=0, 
            padx=10, 
            pady=10, 
            columnspan=7
        )
        self.tabla_lbf.column("#0", 
            width=50
        )
        self.tabla_lbf.heading("#0", 
            text="ID"
        )
        self.tabla_lbf.column("dni", 
            width=100
        )
        self.tabla_lbf.heading("dni", 
            text="DNI"
        )
        self.tabla_lbf.column("nomb", 
            width=190
        )
        self.tabla_lbf.heading("nomb", 
            text="Nombre"
        )
        self.tabla_lbf.column("ape", 
            width=190
        )
        self.tabla_lbf.heading("ape", 
            text="Apellido"
        )
        self.tabla_lbf.column("fnac", 
            width=100,
        )
        self.tabla_lbf.heading("fnac", 
            text="Fecha Nac"
            )
        self.scroll = Scrollbar(
            self.home, 
            command=self.tabla_lbf.yview
        )
        self.scroll.grid(
            row=5, 
            column=8,
            sticky="nsew", 
        )
        self.tabla_lbf.config(
            yscrollcommand=self.scroll.set
        )
        self.actualizar_tabla()
        self.tabla_lbf.bind("<ButtonRelease>", 
            self.visualizar_seleccion
        )

       #----Metodos
    def abre_ventana_mensaje(self, texto):
        """Abre ventana emergente estandar"""
        messagebox.showinfo("Atención!", texto)

    def borra_panel_de_los_entry(self):
        """Pone el panel de entrys en blanco"""
        self.e_dni.delete(0, "end")
        self.e_nomb.delete(0, "end")
        self.e_ape.delete(0, "end")
        self.e_fnac.delete(0, "end")

    def actualizar_tabla(self):
        """Actualiza la informaciín del panel en la tabla"""
        for records in self.tabla_lbf.get_children():
            self.tabla_lbf.delete(records)

        mi_jugador = self.la_base.select()

        for registro in mi_jugador:
            self.tabla_lbf.insert(
                "",
                0,
                text=registro.id,
                values=(
                registro.dni, 
                registro.apellido, 
                registro.nombre,
                registro.fecha
                )
            )
    
    def agregar_jugador(self):
        """Check de datos obligatorios e ingreso de registros"""
        if self.e_dni.get() != "":
            if self.e_fnac.get() == "":
                self.e_fnac.insert(0, "01-01-1900")
            jug_nuevo = (
                self.e_dni.get(),
                self.e_nomb.get(),
                self.e_ape.get(),
                self.e_fnac.get(),
            )
            self.dbase_operativo.insertar_nuevo_jugador(jug_nuevo)
            self.borra_panel_de_los_entry()
            self.actualizar_tabla()
            self.reinicia_panel_a_inicio()
        else:
            self.abre_ventana_mensaje(
                "Por Favor ingresar todos los datos"
            )

    def visualizar_seleccion(self,event):
        """Completa el panel con la seleccion de la tabla"""
        item_1 = self.tabla_lbf.focus()
        self.borra_panel_de_los_entry()
        self.borra_datos_preestablecidos()
        self.e_dni.insert(0,
            self.tabla_lbf.item(item_1,"values")[0]
        )
        self.e_nomb.insert(0,
            self.tabla_lbf.item(item_1,"values")[1]
        )
        self.e_ape.insert(0,
            self.tabla_lbf.item(item_1,"values")[2]
        )
        self.e_fnac.insert(0,
            self.tabla_lbf.item(item_1,"values")[3]
        )
    
    @advertencia
    def modificar_jugador(self):
        """Toma las modificaciones realizadas en el panel y las registra"""
        if self.e_dni.get() !="":
            if self.e_fnac.get() == "":
                   self.e_fnac.insert(0,"01-01-1900") 
            jug_modificado = (
                self.e_dni.get(),
                self.e_nomb.get(),
                self.e_ape.get(),
                self.e_fnac.get()
            )
            self.dbase_operativo.modificar_registro(jug_modificado)
            self.borra_panel_de_los_entry()
            self.actualizar_tabla()
            self.reinicia_panel_a_inicio()
        else:
            self.abre_ventana_mensaje(
                "Para modificar debe completar todos los datos"
            )         
    @advertencia
    def eliminar_jugador(self):
        """Elimina de los registros la seleccion"""
        item_1 = str(self.tabla_lbf.item(self.tabla_lbf.selection())['text'])
        if item_1 !="":
            self.dbase_operativo.borrar_jugador(item_1)
            self.borra_panel_de_los_entry()
            self.actualizar_tabla()
            self.reinicia_panel_a_inicio()
        else:
            self.abre_ventana_mensaje(
                "Seleccione un jugador para eliminar"
            )      

    def salir_app(self):
        """Cierra la ventana de la app"""
        valor = messagebox.askokcancel(
            "salir de la APP", "Desea salir del programa?"
            )
        if valor== True:

            self.home.destroy()

    def habilita_entry_dni(self,):
        """habilita el entry DNI para ingreso"""
        self.e_dni.config(state=NORMAL)
        self.e_dni.delete(0, END)

    def habilita_entry_fecha(self,):
        """habilita el entry fecha de nacimiento para ingreso"""
        self.e_fnac.config(state=NORMAL)
        self.e_fnac.delete(0, END)

    def borra_datos_preestablecidos(self):
        """Borra datos de los entrys para no superponer datos con 
        la seleccion de tabla"""
        self.e_dni.config(state=NORMAL)
        self.e_dni.delete(0, END)
        self.e_fnac.config(state=NORMAL)
        self.e_fnac.delete(0, END)

    def reinicia_panel_a_inicio(self):
        """Reinicia la condicion de los entrys obligatorios"""
        self.e_dni.config(state=DISABLED)
        self.dni.set("Ingrese DNI sin puntos")
        self.e_fnac.config(state=DISABLED)
        self.fnac.set("DD-MM-AAAA")


   