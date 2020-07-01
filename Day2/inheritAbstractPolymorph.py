from abc import abstractmethod


# superclass
class Bird:
    fly = True

    def noise(self):
        print("Birdnoise")

    babies = 0

    def reproduce(self):
        self.babies += 1

    # abstract method must be defined by subclasses, cannot be ignored
    @abstractmethod
    def eat(self):
        pass

    extinct = False


# subclass
class Owl(Bird):
    # using polymorphism to override the
    # funcitonality of the reproduce method
    def reproduce(self):
        self.babies += 6

    # using abstraction to define the abstract method of the parent class
    def eat(self):
        print("Peck Peck")


class Dodo(Bird):
    fly = False
    extinct = True

    def eat(self):
        print("Nom Nom")

    def reproduce(self):
        if not self.extinct:
            self.babies += 1
        else:
            print("No more dodo's")


