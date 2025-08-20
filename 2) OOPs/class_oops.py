class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    def introduce(self):
        print(f"My name is {self.name} and I am a {self.animal_type}.")


my_pet = Pet("Tommy", "Dog")
my_pet.introduce()
