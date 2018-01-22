

__author__ = "a16rubenav"
__date__ = "$Jan 8, 2018 11:13:17 AM$"

import os
import gi
import Conexion
import Operaciones
import time
os.environ['UBUNTU_MENUPROXY']='0'
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class factura():
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file("cliente.glade")
        self.idVentanaPrincipal=b.get_object("idVentanaPrincipal")
        #id de los label
        
        self.idDni=b.get_object("idDni")
        self.idNombre=b.get_object("idNombre")
        self.idApellido=b.get_object("idApellido")
        self.idDireccion=b.get_object("idDireccion")
        self.idLocalidad=b.get_object("idLocalidad")
        self.idTelefono=b.get_object("idTelefono")
        self.idEmail=b.get_object("idEmail")
        self.idinformativo=b.get_object("idinformativo")
        #botones
        self.btnAlta=b.get_object("btnAlta")
        self.btnBaja=b.get_object("btnBaja")
        self.btnModificar=b.get_object("btnModificar")
        #listStore y TreeView
        self.listaClientes=b.get_object("listaClientes")
        self.idtreeCLiente=b.get_object("idtreeCLiente")
        #----------Facturas---------
        self.dniClienteFacturacion=b.get_object("dniClienteFacturacion")
        self.idFactura=b.get_object("idFactura")
        self.idCantidad=b.get_object("idCantidad")
        self.idPrecio=b.get_object("idPrecio")
        #botones
        self.btnIniciarFactura=b.get_object("btnIniciarFactura")
        self.btnBorrarFactura=b.get_object("btnBorrarFactura")
        self.btnGrabarVenta=b.get_object("btnGrabarVenta")
        
        #listStore y treeView
        self.listaFactura=b.get_object("listaFactura")
        self.idTreeFactura=b.get_object("idTreeFactura")
        dic={"on_btnBaja_clicked":self.bajaCliente,"on_btnAlta_clicked":self.altaCliente,"on_idtreeCLiente_cursor_changed":self.cargarCLiente,
        "on_btnModificar_clicked":self.modificarCliente,"on_btnIniciarFactura_clicked":self.altaFactura,"on_btnBorrarFactura_clicked":self.bajaFactura,}
        
        
        b.connect_signals(dic)
        self.idVentanaPrincipal.show()
        self.refrescarCliente()
        self.refrescarFactura()
    def altaFactura(self,widget):
        tiempo=time.strftime("%d/%m/%y")
        dni=self.dniClienteFacturacion.get_text()
        fila=(tiempo,dni)
        Conexion.insertarf(fila);
        self.listaFactura.clear();
        self.refrescarFactura()
        self.idinformativo.set_text("Has dado de alta una factura")
    def bajaFactura(self,widget):
        model,iter= self.idTreeFactura.get_selection().get_selected()
        nFactura=model.get_value(iter,0)
        if(nFactura!=""):
            Conexion.bajaf(nFactura)
            self.listaFactura.clear();
            self.refrescarFactura()
            self.idinformativo.set_text("Has dado de baja una factura")
           
    def refrescarFactura(self):
        lista = Conexion.listarf()
        for registro in lista:
            self.listaFactura.append(registro)
    def altaCliente(self,widget):
        self.dni = self.idDni.get_text()
        self.nombre = self.idNombre.get_text()
        self.apellido = self.idApellido.get_text()
        self.direccion = self.idDireccion.get_text()
        self.localidad = self.idLocalidad.get_text()
        self.telefono = self.idTelefono.get_text()
        self.email = self.idEmail.get_text()
        if self.dni != "" or self.nombre!=""or self.apellido!="":
            fila=(self.dni,self.nombre,self.apellido,self.direccion,self.telefono,self.localidad,self.email)
            Conexion.insertarc(fila)
            self.listaClientes.clear()
            self.refrescarCliente()
            Operaciones.limpiarc(self)
            self.idinformativo.set_text("Has dado de alta reciente a "+self.nombre+" "+self.apellido)
        else:
            print ("algun error")
    def refrescarCliente(self):
        lista = Conexion.listarc()
        for registro in lista:
            self.listaClientes.append(registro)
    def cargarCLiente(self,widget):
        model,iter= self.idtreeCLiente.get_selection().get_selected()
        if iter!=None:
            sdni=model.get_value(iter,0)
            self.snombre=model.get_value(iter,1)
            self.sapellido=model.get_value(iter,2)
            sdireccion=model.get_value(iter,3)
            stelefono=model.get_value(iter,4)
            slocalidad=model.get_value(iter,5)
            semail=model.get_value(iter,6)
            self.idDni.set_text(sdni)
            self.idNombre.set_text(self.snombre)
            self.idApellido.set_text(self.sapellido)
            self.idDireccion.set_text(sdireccion)
            self.idLocalidad.set_text(slocalidad)
            self.idTelefono.set_text(stelefono)
            self.idEmail.set_text(semail)
            #dni que lo metemos en la vista de facturación
            self.dniClienteFacturacion.set_text(sdni)
            

                
    def bajaCliente(self,widget):
        self.dni=self.idDni.get_text()
        
        if self.dni!="":
            Conexion.bajac(self.dni)
            self.listaClientes.clear()
            self.refrescarCliente()
            self.idinformativo.set_text("Has dado de baja reciente a "+self.snombre+" "+self.sapellido)
            Operaciones.limpiarc(self)   
    def modificarCliente(self,widget):
        self.dni = self.idDni.get_text()
        self.nombre = self.idNombre.get_text()
        self.apellido = self.idApellido.get_text()
        self.direccion = self.idDireccion.get_text()
        self.localidad = self.idLocalidad.get_text()
        self.telefono = self.idTelefono.get_text()
        self.email = self.idEmail.get_text()
        if self.dni != "" or self.nombre!=""or self.apellido!="":
            Conexion.modificac(self.dni,self.nombre,self.apellido,self.direccion,self.telefono,self.localidad,self.email)
            self.listaClientes.clear()
            self.refrescarCliente()
            self.idinformativo.set_text("Has modificado reciente a "+self.snombre+" "+self.sapellido)
            Operaciones.limpiarc(self)   
if __name__ == "__main__":
    main = factura()
    Gtk.main()

