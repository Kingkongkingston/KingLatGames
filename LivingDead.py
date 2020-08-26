<<<<<<< HEAD
=======


>>>>>>> 550a0393a898e63b336daa3866fa201897762bfc
def prestige(money):
    if prestige == 1:
        print("Nice work, you're prestige level 1! You earned 10 cash!")
        money += 10


def prestige2(money):
    if prestige == 2:
        print("Nice work, you're prestige level 2! You earned 20 cash!")
        money += 20


def prestige3(money):
    if prestige == 3:
        print("Nice work, you're prestige level 3! You earned 30 cash!")
        money += 30


def prestige4(money):
    if prestige == 4:
        print("Nice work, you're prestige level 4! You earned 40 cash")
        money += 40


def prestige5(money):
    if prestige == 5:
        print("Your prestige level has maxed out! You earned 50 cash!")
        money += 50


def call911():
    response = input('''
You grab your phone to call 911, but the phone battery is dead. You look for your charger, but the
electricity stops working. The zombies must have switched off the power generator. Isn't that a little
too smart for a zombie to behave? What do you do now?
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
    print('''You try to climb down the stairs, but the zombies rush up the stairs at eye-blurring speed. You are ambushed by a horde of hungry, bloodthirsty
zombies, and you die a quick, painless death.''')
    again()


def start():
    print('''This game is a text adventure game made to test your general knowledge, critical thinking,
    and problem solving abilities. You can use cash to buy items like ammo and weapons.
    If you take risky choices and succeed, you will be rewarded greatly with prestige levels. You gain cash every
    If you tak risky choices and succeed, you will be rewarded greatly with prestige levels. You gain cash every
    time you level up. If there are any problems with this game, please email the makers of this
    game at akronnie55@gmail.com or setharaphael7@gmail.com''')

    name = input("What is your name? This information is used for game purposes only and it will not be recorded. ")

    print('''
Greetings! You live in an apartment building near Toronto, Canada. You work as a mechanic,
you're skilled at rock climbing, and your hobby is racing. Your life has been amazing until August 17, during
the night, at around 11 PM...
    ''')
    print('''
You feel tired, so you decide to go to bed. After an hour, you wake up in your bed, deprived of sleep.
Everything is quiet, so you think everything is normal, but you are awfully wrong. You open the fridge to grab a drink of juice, but you hear a disturbing
retching sound outside. You open the window and you see a man walking around on the street. You close the window
just in time to hear a scream outside. You open the window again, and the first man is grabbing another person
by the head and ripping his head off. You start to feel dizzy. You think you're imagining things, but you hear
a chorus of howling nearby. You step into the balcony of your home, bathed in
moonlight, just in time to see a horde of zombies running down the road towards your apartment building. You
see them enter the lobby, and you hear another scream. The lady at the front desk has mutated into a zombie as
well. What do you do?
    ''')

    response = input('''
Do you:
1) Call 911
2) Run downstairs to investigate
3) Climb down to your car
What is your choice? >> ''')
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
    You take a nibble on the chip, and you realize what going to happen next. You start to leak blood everywhere.
    You start to wonder why you are dying, but too late; You are welcomed into the arms of death.
    ''')
    again()


def pizzaShop():
    response = input('''
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
        Do you:
        1) Accept his offer
        2) Decline his offer, you're going to go solo
        What is your choice>>
    ''')

    if response == "1":
        response = print("Coming soon!")
    elif response == "2":
        response = print("Coming soon!")
    else:
        urstupid()


def policeStation():
    response = input('''
    You decide to go to the police station, because you think its safe there. On the way there, you see a zombie,
    no wait,its another survivor! You drive over to him, and he thinks you're a zombie, so he yells,
        "Back off, stinky citizen!", and shoots your tire.
        "Dude, i'm just another survivor, like you!", you shout.
    Relieved, the guy walks over to you, apoligizes for shooting your tire, and shakes hands with you.
        "I'm terribly sorry for shooting your tire. How can I repay you?"
        "No thanks, i'm a mechanic, so I always carry a tool kit.", you say.
        After talking for a few minutes, the guy asks you,
        "I have a gang of 3 survivors and a dog a little south of here. I can help you survive if you join me...
        do you wanna join us?"
<<<<<<< HEAD
=======

>>>>>>> 550a0393a898e63b336daa3866fa201897762bfc
        Do you:
        1) Accept his offer
        2) Decline his offer, you're going to go solo
        What is your choice>>
    ''')


def leaveGasStation():
    response = input('''
    You decide that since you filled up your car with gas, you can visit the pizza shop or the police station.
    Where do you choose to go?
    Do you:
    1) Drive to the pizza shop
    2) Drive to the police station
    ''')
    if response == "1":
        pizzaShop()
    elif response == "2":
        policeStation()


def gasStation():
    response = input('''
    You fill up your car with gas, and walk around. You see a small shop, so ou open the door, and you hear a
    dinging noise. You flinch, but you realize that it's the bell on the door.
    The shop is empty, but you see some snack bags on the ground, and you pick them up.
    It looks like someone has messed with the bag, because there are blood marks on the bag and it has been
    opened. You look inside, and it smells weird. You take a chip, and examine it.
    Do you:
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
    response = input('''
You gather your valuables, grab your family photos (you don't feel like leaving them behind), open your
apartment window and casually climb down to the first floor. The zombies can't see you leave, but they
smell flesh, so you quickly open your car door, hop in the driver seat, and drive away.
15 minutes later, you come across an abandoned gas station. A sign up ahead says that there is a pizza shop
1 mile away, and there is a police station 3.5 miles away. Where do want to go?
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
    response = input('''
You press the elevator button, but nothing works, because the zombies cut out the power. What do you do?
Do you:
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


<<<<<<< HEAD
start()
=======
start()



>>>>>>> 550a0393a898e63b336daa3866fa201897762bfc
