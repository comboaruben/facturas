try:
    import sqlite3 
    bbdd = 'bbddfactura.sqlite'
    conex = sqlite3.connect(bbdd)
    cur = conex.cursor()
    print('conexion hecha')
   
except:
    print ("Posibles errores de importacion")
  
       
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
def insertarf(fila):
    try: 
        registro = fila
        cur.execute("insert into Factura(dni_cliente,fecha) values (?,?)",registro)
        print('insertado')
        conex.commit()
    except:
        print("hubo un error alta clientes")
        conex.rollback()        
def listarc():
    try:
        cur.execute("select * from Cliente")
        listado = cur.fetchall()
        return listado
    except:
        print ("er.message en cliente")
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
        conex.commit()
    except:
        print ("Problemas con el borrado")
        conex.rollback()
