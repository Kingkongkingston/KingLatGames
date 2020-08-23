response = ""
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
    print('''This game is a text adventure game made to test your general knowledge, critical thinking, and problem solving abilities. To answer
the questions that will pop up during the game, copy and paste the given choices next to the question.
If there are any problems with this game, please email the maker of this game at akronnie55@gmail.com''')

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
What is your choice? >>> ''')
    if response == "1":
        call911()
    elif response == "2":
        stairs()
    elif response == "3":
        car()
    else:
        urstupid()


def car():
    response = input('''
You gather your valuables, grab your family photos (you don't feel like leaving them behind), open your
apartment window and casually climb down to the first floor. The zombies can't see you leave, but they
smell flesh, so you quickly open your car door, hop in the driver seat, and drive away.''')

def elevator():
    response = input('''
You press the elevator button, but nothing works, because the zombies cut out the power. What do you do? Do you:
1) Go down via the stairs
2) Get to the car instead
What is your choice? >>> ''')
    if response == "1":
        stairs()
    elif response == "2":
        car()
    else:
        urstupid()



def check(theResponse):
    if theResponse == "stairs":
        stairs()
    elif theResponse == "car":
        car()
    elif theResponse == "elevator":
        elevator()
    elif theResponse == "911":
        call911()
    else:
        urstupid()

def urstupid():
    print("Why would you do anything but what I have provided you with? You're so stupid that the zombies could smell it, and they come and eat you.")
    print("And I'm kinda glad tbh")

def again():
    playAgain = input("Would you like to play again? >>> ")
    if playAgain.lower() == "y" or playAgain.lower() == "yes":
        start()
    else:
        print("Ok. Come back and try again soon!")
start()