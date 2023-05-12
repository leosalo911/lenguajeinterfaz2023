from flask import Blueprint, render_template, request, session, redirect, url_for

bp_login = Blueprint("login", __name__)

@bp_login.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        cdx = {
            'tipo': None
        }
        return render_template("login/login.html", cdx=cdx)

    elif request.method == 'POST':

        usuario = request.form.get("usuario")
        contra = request.form.get("contra")

        if usuario == 'Administrador':
            if contra == 'arelygaleana125':
                # tipo = 'admin'
                session['usuario'] = usuario
                return  render_template("home/index.html")
            else:
                return "Contraseña incorrecta, intente de nuevo."

        elif usuario == 'Empleado':
            if contra == 'arely2023':
                # tipo = 'empleado'
                session['usuario'] = usuario
                return render_template("home/index.html")
            else:
                return "Contraseña incorrecta, intente de nuevo.."
        elif usuario == 'Usuario':
            if contra == 'rootpassword':
                session['usuario'] = usuario
                return render_template("home/index.html")
        else:
            return "Usuario incorrecto, intente de nuevo."

@bp_login.route('/logout', methods=['GET', 'POST'])
@bp_login.route('/')
def logout():
    if 'usuario' in session:
        session.pop('usuario')
    return redirect(url_for('login.login'))