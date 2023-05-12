from tienda.modulos import db

class Venta(db.Model):
    __tablename__="Ventas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.String(255))
    producto = db.Column(db.String(255))
    cantidad = db.Column(db.Integer)
    total = db.Column(db.Float)
    nombre = db.Column(db.String(255))
    telefono = db.Column(db.String(10))
    direccion = db.Column(db.String(255))


    def __init__(self, fecha, producto, cantidad, total, nombre, telefono="None", direccion="None"):
        self.fecha = fecha
        self.producto = producto
        self.cantidad = cantidad
        self.total = total
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def __repr__(self):
        return f"({self.id}) {self.nombre}{self.total}"

