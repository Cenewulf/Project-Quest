import math
import random
import dice
import quest

class Job:
  def __init__(self,job):
    self.job = self


class Weapon:
  def __init__(self,  hands, damage, damageType, name):                  
    self.name = name
    self.hands = hands
    self.damage = damage
    #damagetype 1=physical 2=magical
    self.damageType = damageType

WoodenSword = Weapon(1,2,1, "Wooden Sword")
CopperSword = Weapon(1,7,1, "Copper Sword")
IronSword = Weapon(1,13,1, "Iron Sword")
SteelSword = Weapon(1,30,1, "Steel Sword")
MythrilBlade = Weapon(1,35,2, "Mythril Blade")
FlameSword = Weapon(1,35,2, "Flame Sword")
IceSword = Weapon(1,35,2, "Ice Sword")
ThunderBlade = Weapon(1,35,2, "Thunder Sword")
Grasscutter = Weapon(1,35,2, "Grasscutter")
Shadowbringer = Weapon(1,35,2, "Shadowbringer" )
HandAxe = Weapon(1,15,1, "Hand Axe")
BattleAxe = Weapon(1,25,1, "Battle Axe")
GreatAxe = Weapon(2,50,1, "Great Axe")
Bow = Weapon(2,13,1, "Bow")
GreatBow = Weapon(2,25,1, "Great Bow")
FlameBow = Weapon(2,25,2, "Flame Bow")
IceBow = Weapon(2,25,2, "Ice Bow")
ThunderBow = Weapon(2,25,2, "Thunder Bow")
ArtemisBow = Weapon(2,25,2, "Artemis Bow")
PoisonBow = Weapon(2,25,2, "Poison Bow")
Staff = Weapon(2,5,1, "Staff")
FlameStaff = Weapon(2,12,2, "Flame Staff")
IceStaff = Weapon(2,12,2, "Ice Staff")
ThunderStaff = Weapon(2,12,2, "Thunder Staff")
Katana = Weapon(2,15,1, "Katana")
IchiKujimori =  Weapon(2,27,1, "Ichi-Kujimori")
Tetsu = Weapon(2,32,2, "Tetsu")


print(Tetsu.name)

starter_list = [WoodenSword,Bow,Staff]









class Armor:
  def __init__(self, defstat,name):
    self.defstat = defstat
    self.name = name

Travellerscoat = Armor (2, "Traveller's Coat")
HideArmor = Armor (4,"Hide Armor")
CopperArmor = Armor (7, "Copper Armor")
IronArmor = Armor (15, "Iron Armor")
SteelArmor = Armor (27, "Steel Armor")
MythrilArmor = Armor (35, "Mythril Armor")
HeroArmor= Armor (50, "Hero's Armor")












  #def myfunc(self):
  

    # You use a "f" string known as format string, when you want to use a "variable" in string
    #print("This sword is " + str(self.weight) + "lbs heavy, it also requires " + str(self.hands) + " hands", "and does 1d6 damage")
  
  #def sharpen(self):
    #self.durability += 5
    #print(str(self.durability))
#### NOTES #####

# "f" string #
# print(f"This sword is {str(self.weight)} lbs heavy, it also requires {str(self.hands)} hands and does 1d6 damage")



# class Armor:
#   def __init__(self):
#     pass
  
#     # So in def func, we have self.randd, this means you can re-use this in any other function in armor. HOWEVER, in func1 you cannot call "randd" anywhere but the 
#     # func1 function
#   def func(self):
#     self.randd = random.int(1,100)
#     return self.randd
    
#   def func1(self):
#     randd = random.int(1, 100)

# p = Armor()
# print(p.func())