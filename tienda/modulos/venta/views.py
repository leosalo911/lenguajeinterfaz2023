from flask import Blueprint, render_template, redirect, request
from tienda.modulos.productos.model.productos import Producto
from tienda.modulos.venta.model.venta import Venta
from sqlalchemy import not_, or_
from tienda.modulos import db
from datetime import datetime

bp_venta = Blueprint("venta", __name__)


@bp_venta.route('/venta')
def venta():
    cdx = {
        "ventas": Venta.query.all()
    }
    return render_template("venta/venta.html", cdx=cdx)


@bp_venta.route('/venta/nuevo', methods=['GET', 'POST'])
def alta():
    if request.method == 'GET':
        cdx = {
            'tipo': 'alta',
            'agregado': False,
            'productos': Producto.query.all(),
            'venta': None
        }


        return render_template("venta/ABC_ventas.html", cdx=cdx)
    elif request.method == 'POST':


        date = datetime.now()  # date.strftime("%d/%m/%y")
        fecha = str(date)
        producto = request.form.get("producto")
        cantidad = request.form.get("cantidad")
        total = 10
        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")
        direccion = request.form.get("direccion")

        # e = Producto.query.get({'nombre': producto})
        # if e:
        #     total = 3 * cantidad

        e = Venta(
            nombre=nombre,
            fecha=fecha,
            producto=producto,
            cantidad=cantidad,
            total=total,
            telefono=telefono,
            direccion=direccion
        )
        db.session.add(e)
        db.session.commit()
        return redirect("/venta")
    else:
        return "Ocurrió un error al registrar la venta."

#
# @bp_venta.route('/venta/nuevo/agregar', methods=['GET', 'POST'])
# def agregar():
#     if request.method == 'GET':
#         cdx = {
#             # 'tipo': 'alta',
#             'productos': Producto.query.all(),
#             # 'venta': None
#         }
#         return render_template("venta/ABC_agregarProducto.html",cdx=cdx)
#     elif request.method == 'POST':
#
#         producto = request.form.get("producto")
#         cantidad = request.form.get("cantidad")
#         # cantidad = int(cantidad)
#
#         cdx = {
#             'tipo': 'alta',
#             # 'productos': Producto.query.all(),
#             'venta': None,
#             'agregado':True,
#             'producto':producto,
#             'cantidad':cantidad
#         }
#         return render_template("venta/ABC_ventas.html", cdx=cdx)
#     else:
#         return "ERROR"

@bp_venta.route('/venta/baja/<int:id>', methods=['GET', 'POST'])
def baja(id):
    if request.method == 'GET':
        cdx = {
            'tipo': 'baja',
            'venta': Venta.query.get({'id': id})
        }
        return render_template("/venta/ABC_ventas.html", cdx=cdx)
    elif request.method == 'POST':
        e = Venta.query.get({'id': id})
        if e:
            db.session.delete(e)
            db.session.commit()
        return redirect("/venta")
    else:
        return "ERROR"

@bp_venta.route('/venta/cambio/<int:id>', methods=['GET', 'POST'])
def cambio(id):
    if request.method == 'GET':
        cdx = {
            'tipo': 'cambio',
            'venta': Venta.query.get({'id': id})
        }
        return render_template("/venta/ABC_ventas.html", cdx=cdx)
    elif request.method == 'POST':
        e = Venta.query.get({'id': id})
        if e:
            e.producto = request.form.get("producto")
            e.cantidad = request.form.get("cantidad")
            # e.total = request.form.get("total")
            e.total = 10
            e.nombre = request.form.get("nombre")
            e.direccion = request.form.get("direccion")
            e.telefono = request.form.get("telefono")
            db.session.add(e)
            db.session.commit()

        return redirect("/venta")
    else:
        return "ERROR"

@bp_venta.route('/venta/direccion/<int:id>')
def direccion(id):
    # empleado = f"id={id}, tipo={type(id)}"
    venta = Venta.query.get({'id': id})
    return venta.direccion