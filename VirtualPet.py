class VirtualPet:
    """ a representation of a pet"""
    #Constructor - run automatically when you create a new instance
    def __init__(self,name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        print ("I have been born - my name is {0}!".format(self.name))

    #Methods
    def talk(self):
        print("Hi, I'm your Virtual Pet!")
        print()
        print("What are we doing today?")

    def feed(self,food):
        self.hunger = self.hunger - 1
        self.energy = self.energy + 1

def MenuScreen(name):
    print("MAIN MENU")
    print()
    print("1. Feed {0}".format(name))
    print("2. Walk {0}".format(name))
    print("3. Check {0}'s energy".format(name))
    print("Please enter your choice: ")

def MenuScreenChoice():
  Choice = eval(input())
  print('')
  return Choice





def main():
    name = input("Please enter a name for your pet: ")
    #create an instance of the class
    pet_one = VirtualPet(name)
    #call the talk method
    pet_one.talk()
    print()
    print()
    MenuScreen(name)
    

if __name__ == "__main__":
    main()
