from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def donnerAmanger(self):
        pass

class cheval(Animal):
    def autre_nom(self):
        print("bonjour cheval!")
    def donnerAmanger(self):
        return super().donnerAmanger()

if __name__ == '__main__':
    po = cheval()
    po.autre_nom()