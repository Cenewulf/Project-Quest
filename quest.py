#Import Libraries
import dice, Items, random, time

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

#### OBJECTS #####
#### JEREMY IS WORKING ON THIS CHUNK RIGHT NOW ####
class Player:
    def __init__(self, name, health, weapon, strength, defense, agility):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.strength = strength
        self.defense = defense
        self.agility = agility
            
    def print_player(self):
        print(f"Heroes Name: {self.name}\n" 
              f"Heroes Health: {self.health}\n"
              f"Heroes Weapon: {self.weapon}\n"
              f"Weapon Damage: {self.strength}\n"
              f"Heroes Armour: {self.defense}\n"
              f"Armour Health: {self.agility}\n")


def Hero_setup():
  print("What is your name?")
  name = input()
  health = 10
  #print("What weapon do you choose")
  #print(wp_list)
  strength = 10
  defense = 6
  agility = 6
  Hero = Player(name, health, WoodenSword, strength, defense, agility)
  return Hero
  
class Hero: 
    health = 10
    strength = 10 
    agility = 6
    defense = 6
    name = "Cleetus"

class Bandit: 
    health = 8
    strength = 6 
    agility = 8
    defense = 5
    name = "Cleetus"



#### STORY BEGINS #####

## ADDING COLOR TO TEXT EX.##
#f"{color.PURPLE}Weapon Type:{color.END} {self.type}\n"

## NPC LEGEND ##


print(r"""                               ,_
                      , . ,          ///
                   '/(((/)))),       .'__,'
                 `-/6())c '(::-    .' /
                 /((()(   _/(8)__.'  / 
                 9/)9))) (((9((    .'
               '/()(((8)  `)())---'
               `9))()9()):(6(():,        ,                   <)()
               / `((6(( _/_/` '       ,o<>oo,,      ()`8o   () 8y
              /   ')))`   |       `8o ()o ()<>o,   8:.o8 <) :8oo'
             /   .' :     |      `()8()()8()()8,  8()((/   :/y-(>
   ()()     /  .'    )    |       8:_8hjw:8 :y 8,  `-))-8o||/ ,
    :/     / .'     /     |`-.   <)-'<>:: ::/8 o,   //   _//_()8,
<)._/-'  _/ /      /      )   `-.   8()-::// 8()o  /(_.-' ,--8<>8o
 :_/  __/  ,:__    |      :      `.    ,','-'    _/     .88()o'
  `--' ///|    `-.__:      :.___   :--' /____.--'  .'`-.`._/_.-<>
        '            `.     :   :   :        (O)  / ,()_`.: o
   //:::       ((O))   `.    :   `.  :       __.-'  ()8 /,8:-8
  (((O)))                )   /     `. :_.---':,        /:  ()`
   ::///    _/    ___.-.'   /--.__.--`.:     /:_      ()()
    .--.___./ ---'    /    /          ( :     ':
  ,'      _/:_,(>    /   .'            ) :
 /        / ':      /  .'              `-.:
         (   (>   _/ .'                   `'
                 (  /
                  )/
                 (/         QUEST                                         """)
                 
print("Press enter to continue.")
input()
print("""And Lo there came a wanderer. Unknown to these lands
He wandered the haunted forests, He traversed the blazing wastes and sands
Mettle and wit were always a test, Tragedy followed without rest
He rose from the ashes of failure and continued to strive for a better world.
Victory. Defeat. Neither mattered so long as He was able to breath life into the realm.
In his final triumph before the world fell. He with a mighty voice shouted a mighty spell.
chosen warriors would hear his call. Your tale is proof of this spell
Now we shall see if you will do well.""")
time.sleep(5)
print(r"""
                                .-'`-.
                               /  ||  \\
                              /   ||   \\
                             |____||___||
                             ||||| ||||||
                             |(   _L   ||
                             \|`-'__`-'|'
                              |  `--'  |
                             _|        |-.
                         .-'| |  \     /  `-.
                        /   | |\     .'      `-.
                       /    | | `''''           \\
                      J     | |             _____|
                      |  |  J J         .-'   ___ `-.
                      |  \   L L      .'  .-'  |  `-.`.
                      | \|   | |     /  .'|    |    |\ \\
                      |  |   J J   .' .'  |    |    | \ \\
                      |  |    L L J  /    |    |    |  \ L
                     /   |     \ \F J|    |    |    |   LJ
                     |   |      \J F | () | () | () | ()| L
                    J  \ |       FJ  |    |  / _`-. |   J |
                    |    |      J |  |    | //    \ |   J |
                   J     |\     | |  |    ||:(     ||   J |
                   |     | `----| |  |    ||::`._.:||   | F
                   |     /\_    | |  |    ||:::::::F|   | F
                   |    |  /`---| |  |    | \:::::/ |   FJ
                   F    |  / |  J |  |    |  `-:-'  |  J F
                  J_.--/  /  |  J J  | () | () | () |()FJ
                   |  |    /     L L |    |    |    | / F
                   |  |     |    \ \ |    |    |    |/ /
                 |`-. |    |     |\ \|    |    |    / /
                 J'\ \|    |     | `.`.   |    |  .'.'
                / .'> |    |     |  `-.`-.|____.-'.'
              .' /::'_|    |/    |    `-.______.-'
             / .::/   \    |     |           |  |
           .' /::'     |--._     |           |--|
          / .::/       |    `-.__|     ____.-|//|
        .' /::'        |        F `--'      ||< |
       / .::/          |       J   |        FL\\|
     .' /::'           )       |   |        F| >|
    / .::/            (        \   |        F|//|
  .' /::'              \       /   |        F|--|
 / .::/                 |` `' '(   (      ' J|  |
| /::'                  |  | ` \   \  `    / J  |
|_:/                    |  | | |    |`-  ''F J  J
                        |    ' F    |   "" |  `-'
                        |     J     |      |
                        |     /     |      |
                        |   .'      |      F
                       /---'(       J     J
                     .'     \        L    |
                  .-'        )       L    F
                .'       .---'       \__.-'
               (       .'             L   |
                `-----'               |   \\
                                      J    \\
                                       L    L
                                       |    F
                                       `-.-'   """)
print("Press any key to continue")
input()

#Intro to the game
print(r"""~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '    """)


print ("""\t It is the year 203 AD. The giants have been all but eradicated since their march on the world of man from Jotunheim.
No one knew how exactly it all came about, but there was a flash in the sky following a larger star impacting the battlefield. Was it divine intervention? Was it an asteroid?
Some even say that there was a mighty God who rode a steed as black as the night into the forray before the earth was torn.
Press Enter to Continue""")

input ()
print (""" \t Life has returned to a semblance of peace. Monsters and all manner of magical creatures both good and malicious still roam the land.
 In this land is where your journey begins. Where it ends is up to you to decide.
 \033[1;32;40mDungeon Master:\033[0;0m You find yourself at the BlueWolf Inn. You are tired and stressed from your ardurous jounrey and take a seat at the bar.
 """)
print("Press Enter to Continue")
input ()
#Conversation with the inkeeper
print("""\t Innkeeper: Greetings traveler. You look very tired. Rooms are 5 silver and today we have our local beef and Cockatrice stew for 2 silver.
\033[1;32;40mDungeon Master:\033[0;0m You hand the innkeeper a small pouch of coins and he after a few moments calls out for someone
Hilda we have someone. Fetch them a flagon of mead!
\033[1;32;40mDungeon Master:\033[0;0m A humanoid roughly in thher mid twenties comes from the kitchen. Long silver hair drapes down to their midsection.
You cannot help but notice that while one eye is as green as emeralds, the other is as blue as the hue of the ocean.""")
print("""\033[1;34;40mHilda:\033[0;0m Oh my what a handsome traveller. New around these parts?
\033[1;32;40mDungeon Master:\033[0;0m Before you could answer, a bard in the corner begins to play a rather somber tune in the corner and sings.
the tones from the lute and the coldness of his voice leaves the room in a sense of a bittersweet but calm tone.
\033[1;34;40mHilda:\033[0;0m He always plays such wonderful but sad tones. As I was saying...are you new to these parts? I have not seen you before.""")
print("Answer Yes or no to Continue")
Hilda_answ1 = input()
if Hilda_answ1 == "Yes":
    print ("\033[1;34;40mHilda:\033[0;0m Well welcome to Holbeck! If you are looking for work, the adventurer's guild is always looking for new adventurers.")
    print ("Press Enter to continue.")
    input ()
elif Hilda_answ1 == "No":
    print ("Dungeon Matser: You shake your head and say no.")
    print ("\033[1;34;40mHilda:\033[0;0m I see. Well I am glad to finally meet you.")
    print ("Press Enter to continue.")
    input ()

print ("\033[1;34;40mHilda:\033[0;0m I have lived in this town for quite some time now. It has its moments of being a bit unsafe considering the traders that")
print ("Sometimes during the winter months, our winter solstice banquet brings out the Fey Folk in the nearby woods to the east.")
print ("Lately most of the townsfolk are heading across the seas to find new lands or going out east to fight in the war effort.")
print ("\033[1;32;40mDungeon Master:\033[0;0m She let out a sigh before continuing")
input ()
print ("\033[1;34;40mHilda:\033[0;0m I wished he had never left....But that's a tale for another time. Be careful if you are on the roads to the east.")
print ("Poachers lately have been hunting down some of the Fey and magical creatures in the wood.")
print ("""\033[1;32;40mDungeon Master:\033[0;0m Before she could continue, the bard began to get a bit louder with his song as he got warmed up. After standing atop
one of the tables, he began to dance and sing, occasionally knocking over another patron's flagon or plate off the table. Some did not take to kindly
to his clumsiness. The man stood at a fairly short five foot three. Long black hair trailed down past his shoulders. It danced along with him as he jumped
around full of energy as was his song. 
\033[1;34;40mHilda:\033[0;0m He's a bit much isn't he?""")
print("Select an option to continue")
print("""[1]Yeah seems like it.

[2]Nah he's fine.

[3]...""")

print ("press the appropriate key to continue.")
bard_answ = input()

if bard_answ == "1":
    print("""\033[1;32;40mDungeon Master:\033[0;0m Hilda let out a slight chuckle before taking another patron's empty flagon. After passing the now full drink to the patron,
    her attention returned to you and the bard. """)

elif bard_answ == "2":
    print("""\033[1;32;40mDungeon Master:\033[0;0m Hilda gave a slight smile before taking another patron's empty flagon.
    "Well he's gonna cause trouble with some of these folks if he is not carely.""")
elif bard_answ == "3":
    print("\033[1;32;40mDungeon Master:\033[0;0m You stood there in silence taking in the surroundings instead of answering.")

time.sleep(10)
print("""\033[1;32;40mDungeon Master:\033[0;0m One of the patrons who just had his drink knocked over rose from his seat. 
    Mercenary: Hey that's my drink you clumsy bastard!
    \033[1;32;40mDungeon Master:\033[0;0m The bard was still in the middle of his song and was not paying attention. The Mercenary reached for him
    and after grabbing his tunic by the shoulder, Immediately punched him.""")

print("""Bard: Hey what was that for-
\033[1;32;40mDungeon Master:\033[0;0m Before he could finish his sentence, he found himself parrying another immediate fist from the same Mercenary. Before long,
the entire tavern is swept up into a fight.

[1] Get involved.

[2] Continue Talking to Hilda and Ignore the fighting.

[3] Try to leave the bar.""")

print("Press the appopriate key to continue")

input()
brawl_answ = input()
if brawl_answ == "1":
  print("""\033[1;32;40m\033[1;32;40mDungeon Master:\033[0;0m\033[0;0m You decide to get up and have a look to see how your combat skills measure up to simple tavern patrons.'""")
elif brawl_answ == "2":
  print ("""\033[1;32;40m\033[1;32;40mDungeon Master:\033[0;0m\033[0;0m You ignore the fighting going on and try to continue to strike up a conversation with Hilda.""")
elif brawl_answ == "3":
  print("""\033[1;32;40m\033[1;32;40mDungeon Master:\033[0;0m\033[0;0m: You try to step out of the tavern """)
  
  #print(Dice.d20)


# you wanted to call certain lines correct?




print("""Morning comes. The sound of the usual hustle and bustle within the town helps you rise with renewed vigor. 
You are hungry, willing And ready for the first adventure laid before you. While the events of last night won't hold much sway on the future.
you can't help but feel like that bard may play a part in this journey some day.""")

print("""'\033[1;32;40m\033[1;32;40mDungeon Master:\033[0;0m\033[0;0mYou walk downstairs after getting dressed and ready for the day. You remember that there was an adventurers guild
within the down. They are sure to have some work for a budding warrior such as yourself. As you step down into the main room,
you see the Inn Keeper behind the bar and Hilda near the firepit cleaning the general area. There are also a couple patrons at the tables having breakfast.
What will you do?""")
print(f"[1] Talk to the Inn Keeper\n"
      f"[2] Talk to Hilda\n"
      f"[3] Talk to the other inn patrons.\n"
      f"[4] Leave the Inn")
firstday_answ = input()


#Do you want on each new line ? You must use an f string to call "\n"
# \n = new line - delete this whenever

