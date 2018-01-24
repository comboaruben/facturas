try:
    import sqlite3 
    bbdd = 'bbddfactura.sqlite'
    conex = sqlite3.connect(bbdd)
    cur = conex.cursor()
    print('conexion hecha')
   
except:
    print ("Posibles errores de importacion")
  
 #-----CLIENTE-----      
def insertarc(fila):
    try: 
        registro = fila
        cur.execute("insert into Cliente(dni,nombre,apellido,direccion,telefono,localidad,email) values (?,?,?,?,?,?,?)",registro)
        print('insertado')
        conex.commit()
    except:
        print("hubo un error alta clientes")
        conex.rollback()
        
def bajac(var):  
    try:
        dni=var
        cur.execute("delete from Cliente where dni=?",(dni,))
        conex.commit()
    except:
        print ("Problemas con el borrado")
        conex.rollback()
        
def modificac(dni,nombre,apellido,direccion,telefono,localidad,email):
    try:
        
        cur.execute("update Cliente set nombre=?, apellido=?, direccion=?, telefono=?, localidad=?, email=? WHERE dni=?", (nombre,apellido,direccion,telefono,localidad,email,dni))
        conex.commit()
    except:
        print("hubo un error en modificar clientes")
        conex.rollback()
def listarc():
    try:
        cur.execute("select * from Cliente")
        listado = cur.fetchall()
        return listado
    except:
        print ("er.message en cliente")
        conex.rollback()
    #------FACTURA----
        #------ComboProducto---
def cargarCmbP(nombre):
    try:
        cur.execute("select * from Producto where nombre=?",(nombre,))
        listado = cur.fetchall()
        return listado
    except:
        print ("er.message en Producto")
        conex.rollback()         
def listarCmbP():
    try:
        cur.execute("select nombre from Producto")
        listado = cur.fetchall()
        return listado
    except:
        print ("er.message en Producto")
        conex.rollback()   
def listarV(factura):
    try:
        cur.execute("select * from Ventas where id_facturas=?",(factura,))
        listado = cur.fetchall()
        return listado
    except:
        print ("er.message en Ventas")
        conex.rollback()  
def insertarV(fila):
    try: 
        registro = fila
        cur.execute("insert into Ventas(id_facturas,id_producto,cantidad,precio) values (?,?,?,?)",registro)
        print('insertado')
        conex.commit()
    except:
        print("hubo un error alta factura")
        conex.rollback()        
def bajaV(idVenta,producto,sumarStock):  
    try:
        
        cur.execute("delete from Ventas where num_ventas=?",(idVenta,))
        cur.execute("select stock from Producto WHERE id_producto=?",(producto,))
        listado = cur.fetchall()
        
        for row in listado:
            stockActual=row[0]
            stockReal=int(sumarStock)+int(stockActual)
            print (stockReal)
        cur.execute("update Producto set stock=? WHERE id_producto=?", (stockReal,producto))
        
        conex.commit()
    except :
        conex.rollback()
def actualizarP(id,stockReal):
    try:
        
        cur.execute("update Producto set stock=? WHERE id_producto=?", (stockReal,id))
        conex.commit()
    except:
        print("hubo un error en modificar Producto")
        conex.rollback()
def insertarf(fila):
    try: 
        registro = fila
        cur.execute("insert into Factura(dni_cliente,fecha) values (?,?)",registro)
        print('insertado')
        conex.commit()
    except:
        print("hubo un error alta factura")
        conex.rollback()        

def listarf():
    try:
        cur.execute("select * from Factura")
        listado = cur.fetchall()
        return listado
    except:
        print ("er.message en Factura")
        conex.rollback()  
def bajaf(var):  
    try:
        factura=var
        cur.execute("delete from Factura where num_factura=?",(factura,))
        cur.execute("select sum(cantidad)from Ventas where id_facturas=?",(factura))
        listado=cur.fetchall()
        
        for row in listado:
            stockActual=row[0]
            stockReal=int(sumarStock)+int(stockActual)
            print (stockReal)
        conex.commit()
    except:
        print ("Problemas con el borrado")
        conex.rollback()
#-------PRODUCTO----
def insertarp(fila):
    try: 
        registro = fila
        cur.execute("insert into Producto(nombre,precio,stock) values (?,?,?)",registro)
        print('insertado')
        conex.commit()
    except:
        print("hubo un error alta Producto")
        conex.rollback()  
def listarp():
    try:
        cur.execute("select * from Producto")
        listado = cur.fetchall()
        return listado
    except:
        print ("er.message en Factura")
        conex.rollback() 
def modificap(precio,stock,nombre):
    try:
        
        cur.execute("update Producto set precio=?, stock=? WHERE nombre=?", (precio,stock,nombre,))
        conex.commit()
    except:
        print("hubo un error en modificar clientes")
        conex.rollback()
def bajap(var):  
    try:
        nombreProducto=var
        cur.execute("delete from Producto where nombre=?",(nombreProducto,))
        conex.commit()
    except:
        print ("Problemas con el borrado en Producto")
        conex.rollback()