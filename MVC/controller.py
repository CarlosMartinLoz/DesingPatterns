from model import Person
import view


def showAll():
    people_in_db = Person.getAll()

    return

def start():
    view.startView()
    view.showAllInView(showAll())
    view.endView()


