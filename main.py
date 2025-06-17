from magican import magican
from fighter import fighter

fighter1 = fighter()
magican1 = magican()

fighter1.attack_enemy(magican1)

print(f"{fighter1.name} attacked {magican1.name} for {fighter1.attack_enemy(magican1)} damage.")
print(f"{magican1.name} has {magican1.health} health left.")
