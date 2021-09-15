from cursor_del_pool import CursorDelPool
from looger_base import log
from Conexion import Conexion
from usuario import Usuario

class UsuarioDAO:
    """
    DAO (Data Acces Object)
    CRUD (Creae Read Update Delete)
    """
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(nombre, ip, usuario, contraseña) VALUES(%s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET nombre=%s, ip=%s, usuario=%s, contraseña=%s  WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2], registro[3], registro[4])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.nombre, usuario.ip, usuario.usuario, usuario.contraseña)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'usuario a Insertar: {usuario}')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.nombre, usuario.ip, usuario.usuario,usuario.contraseña, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuario eliminada: {usuario}')
            return cursor.rowcount
                
if __name__== '__main__':

    #Instertar un registro
    # usuario1 = Usuario(nombre='Camara de ejes C2', ip='192.168.74.52', usuario='admin', contraseña='Ftsuser,420')
    # usuarios_instertados = UsuarioDAO.insertar(usuario1)
    # log.debug(f'Personas insertadas: {usuarios_instertados}')
    
    # Actualizar un registro
    # usuario1 = Usuario(id_usuario=3, nombre='Camara Ejes C2', ip='192.168.74.52', usuario='admin', contraseña='Ftsuser420')
    # usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
    # log.debug(f'Personas actualizadas: {usuarios_actualizados}')
    
    # Elimiar un registro
    # usuario1 = Usuario(id_usuario=4)
    # usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
    # log.debug(f'Personas eliminadas: {usuarios_eliminados}')

    # Seleccionar un registro
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
         log.debug(usuario)
