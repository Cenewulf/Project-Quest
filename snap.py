# I've never made a game like this before or thought of. 
# Hope you dont mind me trying to build one here
# Always better to code with others
import random
import time

# That will tidy shit up. Just take the color. You can see under def print_weapon()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

red = color.RED
end = color.END
bold = color.BOLD
class Weapon:
    def __init__(self, minDamage, maxDamage, weaponType):
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.type = weaponType

    def print_weapon(self, wep_type):
        print(f"\n{bold}Attack Style: {wep_type}{end}"
              f"\n{red}Weapon:{end} {self.type}\n" 
              f"{red}Damage:{end} {self.minDamage} - {self.maxDamage}\n") 

    def return_wep(self):
        return self.minDamage, self.maxDamage, self.type


class Armour:
    def __init__(self, armourHealth, armourType):
        self.armourHealth = armourHealth
        self.type = armourType

    def print_weapon(self):
        print(f"{color.PURPLE}Armour Type:{color.END}  {self.type}\n"
              f"\033[1;33;40mArmour:\033[0;0m  {self.armourHealth}\n")

    def return_armour(self):
        return self.armourHealth, self.type

# Take whatever code you need

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.wepDamage = wepDamage
        self.armour = armour
        self.armourHealth = armourHealth
     
    def print_hero(self):
        print(f"\033[1;34;40mHeroes Name:\033[0;0m {self.name}\n" 
              f"Heroes Health: {self.health}\n"
              f"Heroes Weapon: {self.weapon}\n"
              f"Weapon Damage: {self.wepDamage}\n"
              f"Heroes Armour: {self.armour}\n"
              f"Armour Health: {self.armourHealth}\n")

    # def attack(self):
    #     damage = 
        

# class Enemy(Hero):
#     def __init__(self, health, weapon, wepdamage, armour, armourHealth):
#         super().__init__(health, weapon, wepdamage, armour, armourHealth)
#         pass


weapon_type = ['Melee', 'Range']
''' Bows '''
short_bow = Weapon(3, 10, "Bow")
long_bow = Weapon(5, 12, "Bow")
ogre_bow = Weapon(10, 15, "Bow")
''' Swords '''
short_sword = Weapon(3, 10, "Sword")
long_sword = Weapon(5, 12, "Sword")
''' Lance '''
lance = Weapon(10, 15, "Lance")

''' Puts all the range & melee weapons into a list '''
random_range = [short_bow, long_bow, ogre_bow]
random_melee = [short_sword, long_sword, lance]

''' Uses random.choice to pick a random instanced weapon '''
melee_rand = random.choice(random_melee)
range_rand = random.choice(random_range)



# hero_melee = Hero('Adrino')
# hero_range = Hero('Archer')

weapon = random.choice([melee_rand, range_rand])
if weapon == random_melee:
    wep.print_weapon(weapon_type[0])
else:
    weapon.print_weapon(weapon_type[1])





