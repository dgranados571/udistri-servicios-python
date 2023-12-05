from flask import Flask
import mysql.connector
app=Flask(__name__)

@app.route("/bdserver/vistaEdicion/<string:vista>/<string:idElement>")
def bdserver1(vista, idElement):

    formObject = []

    conexion = mysql.connector.connect(user='root', password='Mysql_bdb1', host='localhost', database='udistri_tienda_online', port='3306')
    cur = conexion.cursor()

    match vista:
        case 'categorias':
            cur.execute("SELECT id_categoria, nombre_categoria, descripcion_categoria FROM categorias WHERE id_categoria = " + idElement)
            for id_categoria, nombre_categoria, descripcion_categoria in cur.fetchall():
                formObject.append({
                    'column1': id_categoria, 
                    'column2': nombre_categoria, 
                    'column3': descripcion_categoria
                    })
        case 'productos':
            cur.execute("SELECT id_producto, nombre_producto, descripcion_producto, valor_unitario_producto, categorias_id_categoria FROM productos WHERE id_producto = " + idElement)
            for id_producto, nombre_producto, descripcion_producto, valor_unitario_producto, categorias_id_categoria in cur.fetchall():
                formObject.append({
                    'column1': id_producto, 
                    'column2': nombre_producto, 
                    'column3': descripcion_producto,
                    'column4': valor_unitario_producto, 
                    'column5': categorias_id_categoria
                    })
        case 'clientes':
            cur.execute("SELECT id_cliente, nombre_cliente, direccion_cliente, telefono_cliente, email_cliente FROM clientes WHERE id_cliente = " + idElement)
            for id_cliente, nombre_cliente, direccion_cliente, telefono_cliente, email_cliente in cur.fetchall():
                formObject.append({
                    'column1': id_cliente, 
                    'column2': nombre_cliente, 
                    'column3': direccion_cliente,
                    'column4': telefono_cliente, 
                    'column5': email_cliente
                    })
        case 'ventas':
            cur.execute("SELECT id_venta, fecha_venta, clientes_id_cliente, productos_id_producto, cantidad_vendida FROM ventas WHERE id_venta = " + idElement)
            for id_venta, fecha_venta, clientes_id_cliente, productos_id_producto, cantidad_vendida in cur.fetchall():
                formObject.append({
                    'column1': id_venta, 
                    'column2': fecha_venta, 
                    'column3': clientes_id_cliente,
                    'column4': productos_id_producto, 
                    'column5': cantidad_vendida
                    })
        case _:
            print('ES DEFAULT')

    return formObject


@app.route("/bdserver/obtieneListaVista/<string:vista>")
def bdserver(vista):
    formObject = []

    conexion = mysql.connector.connect(user='root', password='Mysql_bdb1', host='localhost', database='udistri_tienda_online', port='3306')
    cur = conexion.cursor()

    match vista:
        case 'categorias':
            cur.execute("SELECT id_categoria, nombre_categoria, descripcion_categoria FROM categorias")
            for id_categoria, nombre_categoria, descripcion_categoria in cur.fetchall():
                formObject.append({
                    'column1': id_categoria, 
                    'column2': nombre_categoria, 
                    'column3': descripcion_categoria
                    })
        case 'productos':
            cur.execute("SELECT id_producto, nombre_producto, descripcion_producto, valor_unitario_producto, categorias_id_categoria FROM productos")
            for id_producto, nombre_producto, descripcion_producto, valor_unitario_producto, categorias_id_categoria in cur.fetchall():
                formObject.append({
                    'column1': id_producto, 
                    'column2': nombre_producto, 
                    'column3': descripcion_producto,
                    'column4': valor_unitario_producto, 
                    'column5': categorias_id_categoria
                    })
        case 'clientes':
            cur.execute("SELECT id_cliente, nombre_cliente, direccion_cliente, telefono_cliente, email_cliente FROM clientes")
            for id_cliente, nombre_cliente, direccion_cliente, telefono_cliente, email_cliente in cur.fetchall():
                formObject.append({
                    'column1': id_cliente, 
                    'column2': nombre_cliente, 
                    'column3': direccion_cliente,
                    'column4': telefono_cliente, 
                    'column5': email_cliente
                    })
        case 'ventas':
            cur.execute("SELECT id_venta, fecha_venta, clientes_id_cliente, productos_id_producto, cantidad_vendida FROM ventas")
            for id_venta, fecha_venta, clientes_id_cliente, productos_id_producto, cantidad_vendida in cur.fetchall():
                formObject.append({
                    'column1': id_venta, 
                    'column2': fecha_venta, 
                    'column3': clientes_id_cliente,
                    'column4': productos_id_producto, 
                    'column5': cantidad_vendida
                    })
        case _:
            print('ES DEFAULT')
    conexion.close()
    return formObject   

@app.route("/suma/<string:a>/<string:b>")
def suma(a, b):
    resultado = float(a) + float(b)
    if (resultado.is_integer()):
        return str(int(resultado))
    else:
        return str(resultado)

@app.route("/resta/<string:a>/<string:b>")
def resta(a, b):
    resultado = float(a) - float(b)
    if (resultado.is_integer()):
        return str(int(resultado))
    else:
        return str(resultado)

@app.route("/multiplicacion/<string:a>/<string:b>")
def multiplicacion(a, b):
    resultado = float(a) * float(b)
    if (resultado.is_integer()):
        return str(int(resultado))
    else:
        return str(resultado)

@app.route("/division/<string:a>/<string:b>")
def division(a, b):
    if (int(float(b)) == 0):
        return "División entre 0 no es posible"
    resultado = float(a) / float(b)
    if (resultado.is_integer()):
        return str(int(resultado))
    else:
        return str(resultado)

@app.route("/potenciacion/<string:a>/<string:b>")
def potenciacion(a, b):
    resultado = float(a) ** float(b)
    if (resultado.is_integer()):
        return str(int(resultado))
    else:
        return str(resultado)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=81)