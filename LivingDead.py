money = 10

def continueGame():
    input("Press enter to continue: ")

def call911():
    response = input('''
You grab your phone to call 911, but the phone battery is dead. You look for your charger, but the
electricity stops working. The zombies must have switched off the power generator. Isn't that a little
too smart for a zombie to behave? What do you do now?
''')
    continueGame()
    input('''
Do you:
1) Run downstairs
2) Get to your car ASAP
3) Take the elevator
What is your choice? >>> ''')
    if response == "1":
        stairs()
    elif response == "2":
        car()
    elif response == "3":
        elevator()
    else:
        urstupid()


def stairs():
    print('''You try to climb down the stairs, but the zombies rush up the stairs at eye-blurring speed. You are 
    ambushed by a horde of hungry, bloodthirsty zombies, and you die a quick, painless death.
    ''')
    again()


def start():
    print('''This game is a text adventure game made to test your general knowledge, critical thinking,
    and problem solving abilities. You can use cash to buy items like ammo and weapons.
    If you take risky choices and succeed, you will be rewarded greatly with prestige levels. You gain cash every
    time you level up. If there are any problems with this game, please email the makers of this
    game at akronnie55@gmail.com or setharaphael7@gmail.com''')
    input("What is your name? This information is used for game purposes only and it will not be recorded. ")
    continueGame()
    print('''
Greetings! You live in an apartment building near Toronto, Canada. You work as a mechanic,
you're skilled at rock climbing, and your hobby is racing. Your life has been amazing until August 17, during
the night, at around 11 PM...
    ''')
    continueGame()
    print('''
You feel tired, so you decide to go to bed. After an hour, you wake up in your bed, deprived of sleep.
Everything is quiet, so you think everything is normal, but you are awfully wrong. You open the fridge to grab a drink 
of juice, but you hear a disturbing retching sound outside. You open the window and you see a man walking around on the 
street. You close the window just in time to hear a scream outside. You open the window again, and the first man is 
grabbing another person by the head and ripping his head off. You start to feel dizzy. You think you're imagining 
things, but you hear a chorus of howling nearby. You step into the balcony of your home, bathed in
moonlight, just in time to see a horde of zombies running down the road towards your apartment building. You
see them enter the main lobby in the first floor, and you hear another scream. The lady at the front desk has mutated 
into a zombie as well.
    ''')
    continueGame()
    response = input('''
        Do you:
        1) Call 911
        2) Run downstairs to investigate
        3) Climb down to your car
        What is your choice? >> 
        ''')
    if response == "1":
        call911()
    elif response == "2":
        stairs()
    elif response == "3":
        car()
    else:
        urstupid()


def eatChips():
    print('''
    You take a nibble on the chip and you start to leak blood everywhere.
    You start to wonder why you are dying, but too late; You are welcomed into the arms of death.
    ''')
    again()


def pizzaShop(money):
    response = print('''
    You decide to go to the pizza shop, because you were starving. On the way there, you see a zombie, no wait,
    its another survivor! You drive over to him, and he thinks you're a zombie, so he yells, "Back off, stinky
    citizen!", and shoots your tire.
        "Dude, i'm just another survivor, like you!", you shout.
    Relieved, the guy walks over to you, apologizes for shooting your tire, and shakes hands with you.
        "I'm terribly sorry for shooting your tire. How can I repay you?"
        "No thanks, i'm a mechanic, so I always carry a tool kit.", you say.
        After talking for a few minutes, the guy asks you,
        "I have a gang of 3 survivors and a dog a little south of here. I can help you survive if you join me...
        do you wanna join us?"
        ''')
    continueGame()
    input('''
        Do you:
        1) Accept his offer
        2) Decline his offer, you're going to go solo
        What is your choice>>
    ''')

    if response == "1":
        money += 20
        response = print("Coming soon!")
        print(response)
        again()
    elif response == "2":
        response = print("Coming soon!")
        print(response)
        again()
    else:
        urstupid()

def rebelDeath():
    response = print('''
        You choose to go solo, but a few days after you leave, the rebels find out where you are. You run for many 
        weeks, but in the end, they corner you, and you have no chance of survival. They have no mercy, and they slowly,
        and painfully, end your existence.
        ''')
    print(response)
    again()

def joinGroup():
    response = print('''
    You decide to join this mysterious man, and you have no regrets. Many other people join you, and you know that if 
    you went solo, it would have been hard to survive. He has all of the resources you need, and you live 
    an almost-perfect life, until the second wave begins...
    One morning, you notice a giant fire north of camp. You realize the town that you met the group leader at is burning
    down! You inform your leader about the fire, and when you tell him, his smile melts off of his face like a melting
    ice-cream in 100 degree weather. He tells you about the rebels that are against his clan. 
        "Those people want our resources, our people, and most importantly, our lives. There are many clans out there 
        like ours, and those rebels want to wipe us all out", he tells you.
    You realize how dire the situation is, so you and the clan leader make an escape plan to evacuate all 50 people of 
    your clan to another state or country. You plan to evacuate tomorrow, to ensure everyone's safety. You start to 
    think that being in a clan is very risky, and with those rebels out there, you may not survive to see the end of 
    this invasion of zombies.
    ''')
    continueGame()
    input('''Do you:
    1) Evacuate with the rest of the clan
    2) Leave the clan, and go solo again.
    What is your choice>> 
    ''')

    if response == "1":
        response = print("Coming soon!")
        print(response)
    elif response == "2":
        rebelDeath()


def policeStation(money):
    response = print('''
    You decide to go to the police station, because you think its safe there. On the way there, you see a zombie,
    no wait,its another survivor! You drive over to him, and he thinks you're a zombie, so he yells,
        "Back off, stinky citizen!", and shoots your tire.
        "Dude, i'm just another survivor, like you!", you shout.
    Relieved, the guy walks over to you, apologizes for shooting your tire, and shakes hands with you.
        "I'm terribly sorry for shooting your tire. How can I repay you?"
        "No thanks, i'm a mechanic, so I always carry a tool kit.", you say.
        "I have a gang of 3 survivors and a dog a little south of here. I can help you survive if you join me...
        do you wanna join us?"
        He tells you about his campsite, his location, and about a mysterious group of rebels that follow them around.
        The risks are low, and if you join them , you could grow a clan with him that will live to tell the tale of the 
        zombie invasion.
        ''')
    continueGame()
    input('''Do you:
        1) Accept his offer
        2) Decline his offer, you're going to go solo
        What is your choice>> 
    ''')

    if response == "1":
        joinGroup()
        money += 10
    elif response == "2":
        rebelDeath()
    else:
        urstupid()

def leaveGasStation():
    response = print('''
    You decide that since you filled up your car with gas, you can visit the pizza shop or the police station.
    Where do you choose to go?
    ''')
    continueGame()
    input('''Do you:
    1) Drive to the pizza shop
    2) Drive to the police station
    ''')
    if response == "1":
        pizzaShop(money)
    elif response == "2":
        policeStation(money)


def gasStation():
    response = print('''
    You fill up your car with gas, and walk around. You see a small shop, so ou open the door, and you hear a
    dinging noise. You flinch, but you realize that it's the bell on the door.
    The shop is empty, but you see some snack bags on the ground, and you pick them up.
    It looks like someone has messed with the bag, because there are blood marks on the bag and it has been
    opened. You look inside, and it smells weird. You take a chip, and examine it.
    ''')
    input('''Do you:
    1) Eat it
    2) Leave
    What is your choice>>
    ''')
    if response == "1":
        eatChips()
    elif response == "2":
        leaveGasStation()
    else:
        urstupid()


def pizzaShopDeath():
    input('''
    You should have filled up your car at the gas station, because your car's engine shuts off. The zombies notice
    how stupid you acted, and come after you like ants on sugar.
    ''')
    again()


def policeStationDeath():
    pizzaShopDeath()
    again()


def car():
    response = print('''
    You gather your valuables, grab your family photos (you don't feel like leaving them behind), open your
    apartment window and casually climb down to the first floor. The zombies can't see you leave, but they
    smell flesh, so you quickly open your car door, hop in the driver seat, and drive away.
    15 minutes later, you come across an abandoned gas station. A sign up ahead says that there is a pizza shop
    1 mile away, and there is a police station 3.5 miles away. Where do want to go?
    ''')
    continueGame()
    input('''
    Do you:
    1) Visit the gas station
    2) Go to the pizza shop
    3) Go to the police station
    What is your choice>>
    ''')
    if response == "1":
        gasStation()
    elif response == "2":
        pizzaShopDeath()
    elif response == "3":
        policeStationDeath()
    else:
        urstupid()


def elevator():
    response = print('''
You press the elevator button, but nothing works, because the zombies cut out the power. What do you do?
Do you:
''')
continueGame()
input('''
1) Go down via the stairs
2) Get to the car instead
What is your choice? >> ''')
if response == "1":
    stairs()
elif response == "2":
    car()
else:
    urstupid()


def urstupid():
    print(
        "Why would you do anything but what I have provided you with? You're so stupid that the zombies could smell it, and they come and eat you.")
    print("And I'm kinda glad tbh")


def again():
    playAgain = input("Would you like to play again? >>> ")
    if playAgain.lower() == "y" or playAgain.lower() == "yes":
        start()
    else:
        print("Ok. Come back and try again soon!")
        quit()

start()