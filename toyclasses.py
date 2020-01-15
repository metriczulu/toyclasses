class Person:
    '''
    Simple class to define a person and store their name
    '''
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        # This is a 'magic' attribute that allows the class to be called as a string
        return self.name

    def greet(self):
        # Method to greet the person
        print(f"Howdy {self.name}!")


class Introducer(Person):
    '''
    Simple class that introduces itself to another person and says hello

    This class inherits from the Person class, so when you call it you need
    to include a name parameter.  For example:

        >>>shane = Introducer("Shane")

    '''

    def introduce(self):
        # This is a method to introduce yourself, ask a name, and greet a person
        person_name = input(f"Nice to meet you, my name is {self.name}. What's your name? ")
        person = Person(person_name)
        person.greet()


class Group:
    '''
    This is a class to compose a bunch of people into a group of people. You include people
    by simply listing whoever you want as a parameter when defining the class.  For example:

        >>>midcap_management = Group(Person("Tammy"), Person("Dmitry"))

    '''
    def __init__(self, *people):
        self.people = list(people)

    def names(self):
        # returns a list of the names of everyone in the group
        return [str(person) for person in self.people]

    def __str__(self):
        # returns a string with the names of everyone in the group
        return ", ".join(self.names())

    def add_member(self, new_person):
        # add a new person to the group in-place
        self.people.append(new_person)
        return self

    def __add__(self, new_group):
        # concatenate two groups of people together and return a new group with both combined
        name_list = self.people + new_group.people
        new_group = Group()
        new_group.people = name_list
        return new_group


if __name__ == "__main__":
    # Define a person named "Shane" and greet him
    shane = Person("Shane")
    shane.greet()

    # Define an introducer named "Shane" and introduce himself to the user
    shane_introducer = Introducer("Shane")
    shane_introducer.introduce()

    # Create a person named Karthees
    karthees = Person("Karthees")

    # Create a group with Shane and Karthees
    team_1 = Group(shane, karthees)
    print(team_1)

    # Add Joanne to Shane and Karthees group
    team_1.add_member(Person("Joanne"))
    print(team_1)

    # Create a new group for the engineering management
    nikhil, bavani = Person("Nikhil"), Person("Bavani")
    scrum = Group(nikhil, bavani)
    print(scrum)

    # Combine the management and team_1 into a midcap group
    midcap = team_1 + scrum
    print(midcap)