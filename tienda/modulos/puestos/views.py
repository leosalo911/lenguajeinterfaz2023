from flask import Blueprint, render_template, redirect, request
from tienda.modulos.puestos.model.puestos import Puesto
from tienda.modulos.empleados.model.empleados import Empleado
from sqlalchemy import not_, or_
from tienda.modulos import db

bp_puestos = Blueprint("puestos", __name__)


@bp_puestos.route('/puestos')
def puestos():
    # for clave,valor in EMPLEADOS.items():
    #   print(f"{clave}>{valor}")
    cdx = {
        "puestos": Puesto.query.all()
    }
    return render_template("puestos/puestos.html", cdx=cdx)


@bp_puestos.route('/puestos/nuevo', methods=['GET', 'POST'])
def alta():
    if request.method == 'GET':
        cdx = {
            'tipo': 'alta',
            'empleados': Empleado.query.all()
        }
        return render_template("/puestos/ABC_puestos.html", cdx=cdx)
    elif request.method == 'POST':
        nombre = request.form.get("nombre")
        # Este "empleado" es solo el id, así que se tiene que validar con la bd
        empleado = int(request.form.get("empleado"))
        empleado = Empleado.query.get({'id': empleado})
        puesto = Puesto(
            puesto=nombre,
            empleado=empleado
        )
        db.session.add(puesto)
        db.session.commit()
        return redirect('/puestos')


@bp_puestos.route('/baja/<int:id>', methods=['GET', 'POST'])
def baja(id):
    if request.method == 'GET':
        cdx = {
            'tipo': 'baja',
            'empleado': Puesto.query.get({'id': id})
        }
        return render_template("/puestos/ABC_puestos.html", cdx=cdx)
    elif request.method == 'POST':
        e = Puesto.query.get({'id': id})
        if e:
            db.session.delete(e)
            db.session.commit()
        return redirect("/puestos")
    else:
        return "ERROR"
