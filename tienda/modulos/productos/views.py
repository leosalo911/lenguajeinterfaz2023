from flask import Blueprint, render_template,redirect, request
from tienda.modulos.productos.model.productos import Producto
from tienda.modulos import db

bp_productos = Blueprint("productos", __name__)

@bp_productos.route('/productos')
def mostrar():
    cdx={
        "productos": Producto.query.all()
    }
    return render_template("productos/productos.html",cdx=cdx)


@bp_productos.route('/productos/alta', methods=['GET', 'POST'])
def alta():
    if request.method == 'GET':
        cdx = {
            'tipo': 'alta',
            'productos': None
        }
        return render_template("productos/ABC_productos.html", cdx=cdx)
    elif request.method == 'POST':

        nombre = request.form.get("nombre")
        precio = request.form.get("precio")
        precio = precio.replace('$', '')
        precio = precio.replace(',', '')
        precio = float(precio)
        existencia = request.form.get("existencia")


        p = Producto(
            nombre=nombre,
            precio=precio,
            existencia=existencia
        )
        db.session.add(p)
        db.session.commit()
        return redirect("/productos")
    else:
        return "ERROR"

@bp_productos.route('/productos/baja/<int:id>', methods =['GET','POST'])
def baja(id):
    if request.method=='GET':
        cdx = {
            'tipo': 'baja',
            'productos': Producto.query.get({'id': id})
        }
        return render_template("productos/ABC_productos.html",cdx=cdx)
    elif request.method == 'POST':
        e= Producto.query.get({'id': id})
        if e:
            db.session.delete(e)
            db.session.commit()
        return redirect("/productos")
    else:
        return "ERROR"

#
@bp_productos.route('/productos/cambio/<int:id>', methods =['GET','POST'])
def cambio(id):
    if request.method=='GET':
        cdx = {
            'tipo': 'cambio',
            'productos': Producto.query.get({'id': id})
        }

        return render_template("productos/ABC_productos.html",cdx=cdx)
    elif request.method == 'POST':
        e = Producto.query.get({'id': id})
        if e:
            e.nombre= request.form.get("nombre")
            precio = request.form.get("precio")
            precio = precio.replace('$','')
            precio = precio.replace(',','')
            e.precio=float(precio)
            e.existencia = request.form.get("existencia")
            db.session.add(e)
            db.session.commit()

        return redirect("/productos")
    else:
        return "ERROR"

@bp_productos.app_template_filter('formato_moneda')
def formato_moneda(numero:float):
    if(numero):
        return f"${numero:0,.2f}"
    return f"${0:0,.2f}"