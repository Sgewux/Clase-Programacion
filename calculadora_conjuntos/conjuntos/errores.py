class ErrorElementoRepetido(Exception):
    def __init__(self, elemento):
        super().__init__(
            f'Los conjuntos no pueden tener elementos repetidos, {elemento} ya esta en el conjunto.\
 Vuelva a inicar el programa.'
            )
    