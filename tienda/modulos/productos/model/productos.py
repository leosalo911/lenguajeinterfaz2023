from tienda.modulos import db

class Producto(db.Model):
    __tablename__="Productos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255))
    precio = db.Column(db.Float)
    existencia = db.Column(db.Integer)

    def __init__(self, nombre, precio, existencia):
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def __repr__(self):
        return f"({self.id}) {self.nombre}{self.apellido}"

