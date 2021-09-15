from looger_base import log
class Usuario:
    def __init__(self, id_usuario = None, nombre = None, ip= None, usuario=None, contraseña=None):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._ip= ip
        self._usuario = usuario
        self._contraseña = contraseña
        
    def __str__(self):
        return f'''
            Id Usuario: {self._id_usuario}, Nombre: {self._nombre}, Ip: {self._ip}, Usuario: {self._usuario}, Contraseña: {self._contraseña}
    '''
    
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @id_usuario.setter
    def id_persona(self, id_usuario):
        self._id_usuario = id_usuario
        
    @property
    def nombre(self):
        return self._nombre 
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre 
    
    @property
    def ip(self):
        return self._ip
    
    @ip.setter
    def ip(self, ip):
        self._ip = ip
    
    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def email(self, usuario):
        self._usuario = usuario

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def email(self, contraseña):
        self._contraseña = contraseña
    
if __name__=='__main__':

    usuario1 = Usuario(1, 'Camara ejes C2','192.168.74.52', 'admin', 'ftsuser420')
    log.debug(usuario1)
