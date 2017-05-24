class Animal(object):
    def __init__(self, name):
        self.name = name
    
    def set_legs(self, legs):
        self.legs = legs
    
    def set_eating_preferences(self, pref):
        self.diet_type = pref

class fish(Animal):
    def __init__(self, name, fish_type):
        self.fish_type = fish_type
        super(fish, self).__init__(name)
    
    def set_water_habitat(self, habitat):
        self.water_habitat = habitat

class tiger(Animal):
    def __init__(self, name, tiger_type):
        super(tiger, self).__init__(name)
        self.tiger_type = tiger_type
    
    def tiger_color(self, color):
        self.tiger_color = color

Seeta = tiger("Seeta", "Siberian Tiger")
Seeta.set_legs(4)
print Seeta.tiger_type
print Seeta.name
print Seeta.legs

Tim = fish("Tim", "Salmon")
print Tim.fish_type