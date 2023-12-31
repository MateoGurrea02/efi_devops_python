from app import ma
from marshmallow import fields


class PostSchema(ma.Schema):
  id =  fields.Integer(dump_only=True)
  titulo = fields.String()
  contenido = fields.String()
  fecha_creacion = fields.Date()
  autor_id = fields.Integer()
  categoria_id = fields.Integer()

    
class UsuarioSchema(ma.Schema):
  id =  fields.Integer(dump_only=True)
  nombre = fields.String()
  correo = fields.String()
  clave = fields.String()

class ComentarioSchema(ma.Schema):
  id =  fields.Integer(dump_only=True)
  texto_comentario = fields.String()
  fecha_creacion = fields.Date()
  autor_id = fields.Integer()
  post_id = fields.Integer()