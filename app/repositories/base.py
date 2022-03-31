class BaseRepository:
    __model = None

    def __init__(self, model=None):
        self.__model = model

    def get_all(self):
        return self.__model.get_all()
