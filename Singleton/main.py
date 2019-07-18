from singleton import Singleton

if __name__ == '__main__':
    #Las tres son iguales
    s = Singleton()
    print("primera direccion de memoria")
    print(s)

    s = Singleton().getInstance()
    print("segunda direccion de memoria")
    print(s)
    s = Singleton().getInstance()
    print("tercera direccion de memoria")
    print(s)