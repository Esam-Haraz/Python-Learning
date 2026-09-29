class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def take_damage(self, damage_amount):
        self.health -= damage_amount
        if self.health > 0:
            return f"{self.name} Took {damage_amount}, Remaining Health is {self.health}"
        else:
            return f"{self.name} Took {damage_amount}, {self.name} is Defeated"

character = Player("Mario", 100)
print(character.take_damage(50))
print(character.take_damage(60))
