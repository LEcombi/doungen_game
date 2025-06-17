from character import character

class magican(character):
    def __init__(self):
        self.name = "Magician"
        self.health = 100
        self.attack = 8             # Base attributes for a magician
        self.defense = 3
        self.speed = 5
        self.mana = 20
        self.magic_power = 15
        self.magic_type = "healing"
        self.level = 1
        self.type = "magican"
    def attack_enemy(self, enemy):
        damage = self.attack * self.magic_power * 0.5
        if damage < 0:
            damage = 0
        enemy.get_damage(damage)
        return damage
    