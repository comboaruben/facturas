

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
        self.btnBorrarVenta=b.get_object("btnBorrarVenta")
        #combo y listcombo
        self.cmbProducto=b.get_object("cmbProducto")
        self.listCmbProducto=b.get_object("listCmbProducto")
        #listStore y treeView
        self.listVentaProducto=b.get_object("listVentaProducto")
        self.idTreeVenta=b.get_object("idTreeVenta")
        #listStore y treeView
        self.listaFactura=b.get_object("listaFactura")
        self.idTreeFactura=b.get_object("idTreeFactura")
        #---------Producto---------
        self.idNombreProducto=b.get_object("idNombreProducto")
        self.idPrecioProducto=b.get_object("idPrecioProducto")
        self.idStockProducto=b.get_object("idStockProducto")
        #botones
        self.btnAltaProducto=b.get_object("btnAltaProducto")
        self.btnModificarProducto=b.get_object("btnModificarProducto")
        self.btnBajaProducto=b.get_object("btnBajaProducto")
        #listStore y treeView
        self.listaProducto=b.get_object("listaProducto")
        self.idTreeProducto=b.get_object("idTreeProducto")
        
        dic={"on_btnBaja_clicked":self.bajaCliente,"on_btnAlta_clicked":self.altaCliente,"on_idtreeCLiente_cursor_changed":self.cargarCLiente,
        "on_btnModificar_clicked":self.modificarCliente,"on_btnIniciarFactura_clicked":self.altaFactura,"on_btnBorrarFactura_clicked":self.bajaFactura,
        "on_btnAltaProducto_clicked":self.altaProducto,"on_idTreeProducto_cursor_changed":self.cargarProducto,"on_btnModificarProducto_clicked":self.modificarProducto,
        "on_btnBajaProducto_clicked":self.bajaProducto,"on_cmbProducto_changed":self.cargaCmbProducto,
        "on_btnGrabarVenta_clicked":self.altaVentaProducto,"on_idTreeFactura_cursor_changed":self.cargarFactura,"on_btnBorrarVenta_clicked":self.bajaVenta,}
        
        
        b.connect_signals(dic)
        self.idVentanaPrincipal.show()
        self.refrescarCliente()
        self.refrescarFactura()
        self.refrescarProducto()
        self.refrescarCmbProducto()
        self.siClickEnFactura=1
       #prueba
    
    #------------PRODUCTO------------
    def altaProducto(self,widget):
        nombre=self.idNombreProducto.get_text()
        idPrecioProducto=self.idPrecioProducto.get_text()
        idStockProducto=self.idStockProducto.get_text()
        if nombre != "" or idPrecioProducto!=""or idStockProducto!="":
            fila=(nombre,idPrecioProducto,idStockProducto)
            Conexion.insertarp(fila)
            self.listaProducto.clear()
            self.listCmbProducto.clear()
            self.refrescarProducto()
            self.refrescarCmbProducto()
            Operaciones.limpiarp(self)
            self.idinformativo.set_text("Has dado de alta el producto "+nombre+" con un stock de "+idStockProducto)
        else :
            self.idinformativo.set_text("Has dejado algún campo vacio compruebe y prueba de nuevo")
    def modificarProducto(self,widget):
        nombre=self.idNombreProducto.get_text()
        idPrecioProducto=self.idPrecioProducto.get_text()
        idStockProducto=self.idStockProducto.get_text()
        if nombre != "" or idPrecioProducto!="" or idStockProducto!="":
            Conexion.modificap(idPrecioProducto,idStockProducto,self.snombre)
            self.listaProducto.clear()
            self.refrescarProducto()
            self.refrescarCmbProducto()
            Operaciones.limpiarp(self)
            self.idinformativo.set_text("Has modificado el producto "+nombre)
        else :
            self.idinformativo.set_text("Has dejado algún campo vacio compruebe y prueba de nuevo")
    def bajaProducto(self,widget):
        model,iter= self.idTreeProducto.get_selection().get_selected()
        nombreProducto=model.get_value(iter,1)
        if(nombreProducto!=""):
            Conexion.bajap(nombreProducto)
            self.listaProducto.clear()
            self.refrescarProducto()
            self.refrescarCmbProducto()
            self.listCmbProducto.clear()
            Operaciones.limpiarp(self)
            self.idinformativo.set_text("Has dado de baja un producto")
    def refrescarProducto(self):
        lista = Conexion.listarp()
        for registro in lista:
            self.listaProducto.append(registro)
    def cargarProducto(self,widget):
        model,iter= self.idTreeProducto.get_selection().get_selected()
        if iter!=None:
            self.snombre=model.get_value(iter,1)
            sprecio=model.get_value(iter,2)
            sstock=model.get_value(iter,3)
            self.idNombreProducto.set_text(self.snombre)
            self.idPrecioProducto.set_text(sprecio)
            self.idStockProducto.set_text(sstock)
    #-------------FACTURA------------
        #-----ComboProducto----------
    def cargaCmbProducto(self,widget):
        index = self.cmbProducto.get_active()
        model =self.cmbProducto.get_model()
        self.nombre=model[index][0]
        
        listado=Conexion.cargarCmbP(self.nombre)
        for row in listado:
            self.idProducto=row[0]
            self.nombre=row[1]
            self.idPrecio.set_text(row[2])
            self.stock=row[3]
    def refrescarCmbProducto(self):
        lista = Conexion.listarCmbP()
        for registro in lista:
            self.listCmbProducto.append(registro)
        #--------------------------------
        #-------Lista venta------------
    def altaVentaProducto(self,widget,data=None):
        stockPide=int(self.idCantidad.get_text())
        stockReal= int(self.stock)-int(stockPide)

        if stockReal>=0 and stockPide>=1 and self.siClickEnFactura==0:
            precio=float(stockPide)*float(self.idPrecio.get_text())
            fila=(self.numeroFactura,int(self.idProducto),int(stockPide),int(precio))
            Conexion.insertarV(fila)
            Conexion.actualizarP(self.idProducto,stockReal)
            self.listVentaProducto.clear()
            self.refrescarVenta()
            self.listaProducto.clear()
            self.refrescarProducto()
            self.idCantidad.set_text("")
            listado=Conexion.cargarCmbP(self.nombre)
            for row in listado:
                self.idProducto=row[0]
                self.nombre=row[1]
                self.idPrecio.set_text(row[2])
                self.stock=row[3]
            
        else:
            if stockReal<0:
                self.idinformativo.set_text("No puedes pedir tanto de ese producto")
            else:
                self.idinformativo.set_text("Primero selecciona una factura")
    def refrescarVenta(self):
        lista = Conexion.listarV(self.numeroFactura)
        for registro in lista:
            self.listVentaProducto.append(registro)

    def bajaVenta(self,widget):
        model,iter= self.idTreeVenta.get_selection().get_selected()
        idVenta=model.get_value(iter,0)
        producto=model.get_value(iter,2)
        sumarStock=model.get_value(iter,3)
        if(idVenta>0):
            Conexion.bajaV(idVenta,producto,sumarStock)
            self.listVentaProducto.clear()
            self.refrescarVenta()
            self.listaProducto.clear()
            self.refrescarProducto()
            self.idinformativo.set_text("Has dado de baja un producto de una venta")
        else:
            self.idinformativo.set_text("Primero seleccionada una venta")
        #------------------------------------------
    def cargarFactura(self,widget):
        model,iter= self.idTreeFactura.get_selection().get_selected()
        self.numeroFactura=model.get_value(iter,0)
        self.siClickEnFactura=0;
        self.listVentaProducto.clear()
        self.refrescarVenta()
        
      
        #---------------------
    def altaFactura(self,widget):
        tiempo=time.strftime("%d/%m/%y")
        dni=self.dniClienteFacturacion.get_text()
        if dni!="":
            fila=(tiempo,dni)
            Conexion.insertarf(fila)
            self.listaFactura.clear()
            self.refrescarFactura()
            self.idinformativo.set_text("Has dado de alta una factura")
        else :
            self.idinformativo.set_text("Tienes que seleccionar antes un cliente")
    def bajaFactura(self,widget):
        model,iter= self.idTreeFactura.get_selection().get_selected()
        nFactura=model.get_value(iter,0)
        if(nFactura!=""):
            Conexion.bajaf(nFactura)
            self.listaFactura.clear()
            self.refrescarFactura()
            self.idinformativo.set_text("Has dado de baja una factura")
           
    def refrescarFactura(self):
        lista = Conexion.listarf()
        for registro in lista:
            self.listaFactura.append(registro)
    #------------CLIENTE---------
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
        else :
            self.idinformativo.set_text("Has dejado algún campo vacio compruebe y prueba de nuevo")
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

