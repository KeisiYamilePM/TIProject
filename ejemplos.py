

def verificar_usuario(funcion):
    """Los decoradores agregan funcionalidad extra
    a algun metodo, clase o función

    Este decorador, puede ser utilizado
    para verificar que tipo de usuario es ingresado"""

    def encapsulador(usuario):
        #aqui agregamos la funcionalidad extra
        if usuario == 'keisi':
            print('admin')
        else:
            print('intruso')
        #aqui continuamos con la ejecucion normal
        return funcion(usuario)

    return encapsulador



@verificar_usuario
def iniciar_sesion(usuario):
    print('bienvenido')


iniciar_sesion('kei')
