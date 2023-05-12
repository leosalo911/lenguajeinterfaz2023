from tienda.modulos import db

class Usuario(db.Model):
    __tablename__="Usuarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(255))
    contra = db.Column(db.String(255))

    def __init__(self, usuario,contra):
        self.usuario = usuario
        self.contra = contra

    def __repr__(self):
        return f"({self.id}) {self.usuario}{self.contra}"

