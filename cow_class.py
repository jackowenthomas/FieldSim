from animal_class import *

class Cow(Animal):
    """A representation of a cow"""

    #constructor
    def __init__(self, name):
        #call super class constructor
        #growth rate = 1; food need = 6; water need = 4
        super().__init__(1,6,4, name)
        self._type = "Cow"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need:
                self._weight += self._growth_rate * 1.8
            elif self._status == "Poor" and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            else:
                self._weight += self._growth_rate
        #increament day growing
        self._days_growing += 1
        #update the status
        self._update_status()

def main():
    name = None
    cow_animal = Cow(name)
    print(cow_animal.report())
    #manually grow the animal
    manual_grow(cow_animal)
    print(cow_animal.report())

if __name__ == "__main__":
    main()
