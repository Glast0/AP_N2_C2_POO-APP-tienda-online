class Sesion:
    _usuario = None

    @classmethod
    def iniciar(cls, usuario):
        cls._usuario = usuario

    @classmethod
    def cerrar(cls):
        cls._usuario = None

    @classmethod
    def usuario_actual(cls):
        return cls._usuario

    @classmethod
    def activa(cls) -> bool:
        return cls._usuario is not None