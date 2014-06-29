from crop_class import *

class Wheat(Crop):
    """A representation of a wheat crop"""

    #constructor
    def __init__(self):
        #call super class constructor
        #growth rate = 1; light need = 5; water need = 7
        super().__init__(1,5,7)
        self._type = "Wheat"

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.75
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            else:
                self._growth += self._growth_rate
        #increament day growing
        self._days_growing += 1
        #update the status
        self._update_status()

def main():
    wheat_crop = Wheat()
    print(wheat_crop.report())
    #manually grow the crop
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == "__main__":
    main()
