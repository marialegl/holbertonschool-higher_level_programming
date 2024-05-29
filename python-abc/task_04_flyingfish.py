class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# Instantiate an object of the FlyingFish class
flying_fish = FlyingFish()

# Call the fly, swim, and habitat methods and observe the outputs
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

# Investigate the method resolution order
print(FlyingFish.mro())
