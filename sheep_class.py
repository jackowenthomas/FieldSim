from animal_class import *

class Sheep(Animal):
    """A representation of a sheep"""

    #constructor
    def __init__(self,name):
        #call super class constructor
        #growth rate = 1; food need = 7; water need = 3
        super().__init__(1,5,7,name)
        self._type = "Sheep"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need:
                self._weight += self._growth_rate * 1.15
            elif self._status == "Poor" and water > self._water_need:
                self._weight += self._growth_rate * 1.75
            else:
                self._weight += self._growth_rate
        #increament day growing
        self._days_growing += 1
        #update the status
        self._update_status()

def main():
    name = None
    sheep_animal = Sheep()
    print(sheep_animal.report())
    #manually grow the crop
    manual_grow(sheep_animal)
    print(sheep_animal.report())

if __name__ == "__main__":
    main()
