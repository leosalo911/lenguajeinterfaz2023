from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('configuration.DevelopmentConfig')
db = SQLAlchemy(app)

from tienda.modulos.home.views import bp_home
from tienda.modulos.empleados.views import bp_empleados
from tienda.modulos.puestos.views import bp_puestos
from tienda.modulos.venta.views import bp_venta
from tienda.modulos.login.views import bp_login
from tienda.modulos.productos.views import bp_productos

app.register_blueprint(bp_home)
app.register_blueprint(bp_empleados)
app.register_blueprint(bp_puestos)
app.register_blueprint(bp_venta)
app.register_blueprint(bp_login)
app.register_blueprint(bp_productos)

with app.app_context():
    db.create_all()
