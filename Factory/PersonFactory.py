from EuropeanPerson import EuropeanPerson
from AfricaPerson import AfricaPerson
class PersonFactory():
    @staticmethod
    def get_Person(personContinent):
        try:
            if personContinent=="European":
                return EuropeanPerson()
            elif personContinent=="Africa":
                return AfricaPerson()
            raise  AssertionError("Continent not found")
        except AssertionError as error:
            print(error)