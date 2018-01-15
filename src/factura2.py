

__author__ = "a16rubenav"
__date__ = "$Jan 8, 2018 11:13:17 AM$"

import os
import gi
import Conexion
import Operaciones
os.environ['UBUNTU_MENUPROXY']='0'
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class factura():
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file("cliente.glade")
        self.idVentanaPrincipal=b.get_object("idVentanaPrincipal")
        self.idDni=b.get_object("idDni")
        self.idNombre=b.get_object("idNombre")
        self.idApellido=b.get_object("idApellido")
        self.idDireccion=b.get_object("idDireccion")
        self.idLocalidad=b.get_object("idLocalidad")
        self.idTelefono=b.get_object("idTelefono")
        self.idEmail=b.get_object("idEmail")
        self.btnAlta=b.get_object("btnAlta")
        self.btnBaja=b.get_object("btnBaja")
        self.listaClientes=b.get_object("listaClientes")
        self.idListaCliente=b.get_object("idListaCliente")
       
        dic={"on_btnBaja_clicked":self.bajaCliente,"on_btnAlta_clicked":self.altaCliente,}
        b.connect_signals(dic)
        self.idVentanaPrincipal.show()
    def altaCliente(self,widget):
        self.dni = self.idDni.get_text()
        self.nombre = self.idNombre.get_text()
        self.apellido = self.idApellido.get_text()
        self.direccion = self.idDireccion.get_text()
        self.localidad = self.idLocalidad.get_text()
        self.telefono = self.idTelefono.get_text()
        self.email = self.idEmail.get_text()
        if self.dni != "" or self.nombre!=""or self.apellido!="":
            fila=(self.dni,self.nombre,self.apellido,self.direccion,self.email,self.telefono,self.localidad)
            Conexion.insertarc(fila)
            self.listaClientes().clear()
            self.refrescarCliente()
            Operaciones.limpiarc(self.dni,self.nombre,self.apellido,self.direccion,self.email,self.telefono,self.localidad)
        else:
            print ("algun error")
    def refrescarCliente(self):
        lista = conexion.listarc()
        for registro in lista:
            self.listclientes.append(registro)
    
    def bajaCliente(self,widget):
        c=a
if __name__ == "__main__":
    main = factura()
    Gtk.main()

