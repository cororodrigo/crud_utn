from enum import unique
from peewee import *
from tkinter import messagebox
from observa import sujeto


try:
    db = SqliteDatabase('nivel_avanzado.db')

    class BaseModel(Model):
        class Meta:
            database = db

    class base_lbf(BaseModel):
        id = AutoField()
        dni = CharField(unique = True)
        apellido = TextField()
        nombre = TextField()
        fecha = DateTimeField(formats="DD-MM-YYYY")
    db.connect()
    db.create_tables([base_lbf])

except:
    print("lpqvlpev")



class lbf_registros(base_lbf, sujeto):
    def __init__(self,):
        pass
 
    def insertar_nuevo_jugador(self, nuevo):
            """Genera un nuevo registro en el Dbase"""
            self.lista = []
            for variable in nuevo:
                self.lista.append(variable)
            self.lbf = base_lbf()
            self.lbf.dni = self.lista[0]
            self.lbf.apellido = self.lista[1]
            self.lbf.nombre = self.lista[2]
            self.lbf.fecha = self.lista[3]
            self.lbf.save()
            self.notificar(self.lbf.dni,
                self.lbf.apellido,
                self.lbf.nombre,
                self.lbf.fecha
                )

    def modificar_registro(self, jug_modificado):
        """Modifica el Dbase"""     
        self.lista = []
        for registro in jug_modificado:
            self.lista.append(registro)
        modificar = base_lbf.update(dni=self.lista[0], 
                                    apellido=self.lista[1],
                                    nombre=self.lista[2], 
                                    fecha=self.lista[3]).where(
                                    base_lbf.id == self.lista[0]
                                    )
        modificar.execute()             

  
    def borrar_jugador(self, registros):
        """Borra un registro del Dbase"""
        self.lista = []
        for registro in registros:
            self.lista.append(registro)
        self.lbf = base_lbf.get(base_lbf.id == self.lista [0])
        self.lbf.delete_instance()

    def seleccionar_de_la_tabla(self,):
        """Selecciona un registro del Dbase"""
        self.lbf = base_lbf()
        jugador = self.lbf.select(self.lbf.id, 
                                 self.lbf.dni, 
                                 self.lbf.apellido, 
                                 self.lbf.nombre, 
                                 self.lbf.fecha).where(self.lbf.id == id)
        return jugador
                

