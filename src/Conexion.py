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
        cur.execute("insert into Cliente(dni,nombre,apellido,direccion,email,telefono,localidad) values (?,?,?,?,?,?,?)",registro)
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
