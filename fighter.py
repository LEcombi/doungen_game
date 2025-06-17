from character import character

class fighter(character,):
    def __init__(self, name="Fighter", health=100, attack=10,
                 defense=5, speed=7, mana=0, level=1):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.mana = mana
        self.level = level
        self.type = "fighter"
        
    def attack_enemy(self, enemy):
        damage = self.attack
        if damage < 0:
            damage = 0
        enemy.get_damage(damage)
        return damage
