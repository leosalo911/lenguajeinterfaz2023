from flask import Blueprint, render_template, session

bp_home = Blueprint("home", __name__)

@bp_home.route('/menu')
def home():
    # if 'usuario' in session:
    #     tipo = session['usuario']
    tipo = 'Administrador'
    return render_template("home/index.html", tipo=tipo)
