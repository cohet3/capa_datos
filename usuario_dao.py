
from logger_base import log
from cursor_del_pool import CursorDelPool
from usuario import Usuario

class UsuarioDAO:
    """
    DAo- Data Acces OBjecte para la tabla de usuario
    CRUD- CREATe- Read- Update- Delete para la tabla usuario
    """
    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario '
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario eliminado: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount


# if __name__ == '__main__':
    # insertar un registro
    # usuario1 = Usuario(username='Pepoto', password=1234)
    # usuarios_insertardas = UsuarioDAO.insertar(usuario1)
    # log.debug(f'Usuarios insertadas: {usuarios_insertardas}')

    # actualizar un registro
    # usuario1 = Usuario(1, 'Don', 'Pepito')
    # usuarios_actualizadas = UsuarioDAO.actualizar(usuario1)
    # log.debug(f'Usuarios actualizadas: {usuarios_actualizadas}')

    # eliminar un registro
    # usuario1 = Usuario(1)
    # usuarios_eliminadas = UsuarioDAO.eliminar(usuario1)
    # log.debug(f'Usuarios eliminadas: {usuarios_eliminadas}')

    # seleccionar obejtos
    # usuarios = UsuarioDAO.seleccionar()
    # for usuario in usuarios:
    #     log.debug(usuario)