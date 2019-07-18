from model import Person

def showAllInView(list):
    print(len(list))
    for person in list:
        print(person.name())

def startView():
    print ('Ejemplo estructura MVC en python')

def endView():
    print('Se acabo')