class Base:

    instance = None
    def __init__(self):
        from app import mongodb
        self.instance = mongodb