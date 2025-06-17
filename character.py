class character: 
    def __init__(self):
        self.name = "Character"
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.speed = 7
        self.mana = 0
        self.level = 1

    def get_damage(self, damage):
        self.health = damage 
        if self.health < 0:
            self.health = 0
        return self.health

    def level_up(self, levels=1):
        self.level = self.level + levels