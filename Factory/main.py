from PersonFactory import PersonFactory

if __name__=="__main__":
    person = PersonFactory.get_Person("European")
    print(person.get_characteristics())
    otherPerson = PersonFactory.get_Person("Africa")
    print(otherPerson.get_characteristics())

