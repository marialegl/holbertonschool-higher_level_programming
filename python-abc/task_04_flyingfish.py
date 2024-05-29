class Fish:
    def __init__(self, swim_ability):
        self.swim_ability = swim_ability

    def swim(self):
        print(f"The fish is swimming")

    def habitat(self):
        print(f"The fish lives in water")


class Bird:
    def __init__(self, fly_ability):
        self.fly_ability = fly_ability

    def fly(self):
        print(f"The bird is flying")

    def habitat(self):
        print(f"The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def __init__(self, swim_ability, fly_ability):
        Fish.__init__(self, swim_ability)
        Bird.__init__(self, fly_ability)

    def fly(self):
        print(f"The flying fish is soaring!")

    def swim(self):
        print(f"The flying fish is swimming!")

    def habitat(self):
        print(f"The flying fish lives both in water and the sky!")


flying_fish = FlyingFish("underwater", "in the air")
flying_fish.fly()
flying_fish.swim()
flying_fish.habitat()

print(FlyingFish.mro())
