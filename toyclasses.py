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
        print(f"\nHowdy, I'm {self.name}!")


class Meeter(Person):
    '''
    Simple class that introduces itself to another person and says hello

    This class inherits from the Person class, so when you call it you need
    to include a name parameter.  For example:

        >>>shane = Meeter("Shane")

    '''

    def greet(self):
        # This is a method to introduce yourself, ask a name, and greet a person
        person_name = input(f"\nNice to meet you, my name is {self.name}. What's your name? ")
        print(f"\n{person_name}, huh?  That's an ok name--I guess.  Not as good as {self.name}, but sufficient.")


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

    def __len__(self):
        # returns the number of people in the group
        return len(self.people)

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

    shane = Person("Shane")

    midcap = Group(shane)

    nikhil = Person("Nikhil")

    midcap = midcap.add_member(nikhil)

    matt = Person("Matt")

    midcap = midcap.add_member(matt)

    joanne = Person("Joanne")

    midcap = midcap.add_member(joanne)

    #trying to merge Matt's branch back to the master

    
    print(midcap)
    bode = Person("Bode")
    midcap = midcap.add_member(bode)

