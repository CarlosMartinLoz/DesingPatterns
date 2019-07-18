class Singleton:
    _instance = None

    #metodo estatico que sera llamado al inicializar el objeto
    @staticmethod
    def getInstance():
        if Singleton._instance==None:
            Singleton()
            return Singleton._instance
        else:
            return Singleton._instance

    #en caso de que sea la primera instancia se apunta hacia la misma direccion de memoria
    def __init__(self):
        if Singleton._instance==None:
            Singleton._instance=self
