from flask import Blueprint, render_template,redirect, request
from tienda.modulos.empleados.model.empleadosOld import EMPLEADOS
from tienda.modulos.empleados.model.empleados import Empleado
from sqlalchemy import not_,or_
from tienda.modulos import db
bp_empleados = Blueprint("empleados", __name__)

@bp_empleados.route('/empleados')
def empleados():
    #for clave,valor in EMPLEADOS.items():
     #   print(f"{clave}>{valor}")
    cdx={
        "empleados": Empleado.query.all()
    }
    return render_template("empleados/empleados.html",cdx=cdx)

# @bp_empleados.route('/empleados/pruebas')
# def pruebas():
#     Empleado.query.limit(2).all()
#     Empleado.query.order_by(Empleado.salario.desc()).all()
#     Empleado.query.get({'id': 2})
#     Empleado.query.filter_by(nombre='Luis').all()
#     Empleado.query.filter(Empleado.nombre >= 'Luis').all()
#     Empleado.query.filter(or_(Empleado.nombre == 'Jose', Empleado.edad > 30)).all()
#     Empleado.query.filter(not_(Empleado.nombre == 'Jose')).all()
#
#     #e = Empleado(nombre='Pedro', apellido='Garcia', sexo='H', edad=29, puesto='Manager', salario=60000, comentarios='El jefe')
#     #db.session.add(e)
#     #db.session.commit()
#
#     e= Empleado.query.filter_by(nombre='Pedro').first()
#     if e:
#         db.session.delete(e)
#         db.session.commit()
#
#     cdx={
#         "empleados": Empleado.query.all()
#     }
#     return render_template("empleados/productos.html",cdx=cdx)

@bp_empleados.route('/comentarios/<int:id>')
def comentarios(id):
    #empleado = f"id={id}, tipo={type(id)}"
    empleado = Empleado.query.get({'id': id})
    return empleado.comentarios

@bp_empleados.route('/baja/<int:id>', methods =['GET','POST'])
def baja(id):
    if request.method=='GET':
        cdx = {
            'tipo': 'baja',
            'empleado': Empleado.query.get({'id': id})
        }
        return render_template("empleados/ABC_empleados.html",cdx=cdx)
    elif request.method == 'POST':
        e= Empleado.query.get({'id': id})
        if e:
            db.session.delete(e)
            db.session.commit()
        return redirect("/empleados")
    else:
        return "ERROR"


@bp_empleados.route('/cambio/<int:id>', methods =['GET','POST'])
def cambio(id):
    if request.method=='GET':
        cdx = {
            'tipo': 'cambio',
            'empleado': Empleado.query.get({'id': id})
        }

        return render_template("empleados/ABC_empleados.html",cdx=cdx)
    elif request.method == 'POST':
        e = Empleado.query.get({'id': id})
        if e:
            e.nombre= request.form.get("nombre")
            e.apellido = request.form.get("apellido")
            sexo = request.form.get("sexo")
            if sexo == '1':
                e.sexo = 'H'
            elif sexo == '2':
                e.sexo = 'M'
            else:
                e.sexo = 'N'
            e.puesto = request.form.get("puesto")
            e.edad = request.form.get("edad")
            salario = request.form.get("salario")
            salario = salario.replace('$','')
            salario = salario.replace(',','')
            e.salario=float(salario)
            e.comentarios = request.form.get("comentarios")
            db.session.add(e)
            db.session.commit()



        #EMPLEADOS[id]['nombre'] = request.form.get("nombre")
        #EMPLEADOS[id]['apellido'] = request.form.get("apellido")
        #EMPLEADOS[id]['sexo']= request.form.get("sexo")
        #EMPLEADOS[id]['edad'] = request.form.get("edad")
        #EMPLEADOS[id]['Puesto'] = request.form.get("Puesto")
        #salario=request.form.get("Salario")
        #salario= salario.replace('$','')
        #salario= salario.replace(',','')
        #EMPLEADOS[id]['Salario'] = float(salario)
        #EMPLEADOS[id]['comentarios'] = request.form.get("comentarios")
        return redirect("/empleados")
    else:
        return "ERROR"

@bp_empleados.app_template_filter('formato_moneda')
def formato_moneda(numero:float):
    if(numero):
        return f"${numero:0,.2f}"
    return f"${0:0,.2f}"


@bp_empleados.route('/empleado/alta', methods=['GET', 'POST'])
def alta():
    if request.method == 'GET':
        cdx = {
            'tipo': 'alta',
            'empleado': None
        }
        return render_template("empleados/ABC_empleados.html", cdx=cdx)
    elif request.method == 'POST':

        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        sexo = request.form.get("sexo")
        if sexo == '1':
            sexo = 'H'
        elif sexo == '2':
            sexo = 'M'
        else:
            sexo = 'N'
        puesto = request.form.get("puesto")
        edad = request.form.get("edad")
        salario = request.form.get("salario")
        salario = salario.replace('$', '')
        salario = salario.replace(',', '')
        salario = float(salario)
        comentarios = request.form.get("comentarios")

        e = Empleado(
            nombre=nombre,
            apellido=apellido,
            sexo=sexo,
            edad=edad,
            puesto=puesto,
            salario=salario,
            comentarios=comentarios,
        )
        db.session.add(e)
        db.session.commit()
        return redirect("/empleados")
    else:
        return "ERROR"