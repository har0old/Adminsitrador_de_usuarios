from UsuarioDao import UsuarioDAO
from looger_base import log
from usuario import Usuario

opcion =None
while opcion !=5:
    print(f'''
        Opciones: 
        1. Listar usuarios
        2. Agregar usuarios
        3. Modificar usuarios
        4. Eliminar usuarios
        5. Salir
    ''')
    opcion = int(input('Ingrese el numero de la opción a escoger(1 - 5):\n'))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

    elif opcion == 2:
        nombre_var = input('Ingrese el nombre de referencia: ')
        ip_var = input('Ingrese la ip del dispositivo: ')
        usuario_var = input('Ingrese el nombre de usuario: ')
        contraseña_var = input('Ingrese la contraseña: ')
        usuario = Usuario(nombre=nombre_var, ip=ip_var, usuario=usuario_var, contraseña=contraseña_var)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f'usuarios ingresados satisfactoriamente: {usuarios_insertados}')

    elif opcion ==3:
        id_usuario_var = int(input('Ingrese el id_usuario a modificar: '))
        nombre_var = input('Ingrese nuevo el nombre de referencia: ')
        ip_var = input('Ingrese la nueva ip del dispositivo: ')
        usuario_var = input('Ingrese el nuevo nombre de usuario: ')
        contraseña_var = input('Ingrese la nueva contraseña: ')
        usuario = Usuario(id_usuario=id_usuario_var, nombre=nombre_var, ip=ip_var, usuario=usuario_var, contraseña=contraseña_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuarios actualizados satisfactoriamente: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Ingrese el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'usuarios eliminados satisfactoriamente: {usuarios_eliminados}')

    else:
        log.info('Saliste de la aplicacion!')