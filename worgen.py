"""
The 3rd and final phase of my program
"""


# worgen-warrior,hunter,rogue,shaman,mage,warlock,death knight,priest
def worgen_Classes():
    """
This is were the Worgen class will be decided
    """
    wowClass = ['Warrior', 'Hunter', 'Rogue', 'Mage',
                'Shaman', 'Warlock', 'Priest', 'Death knight']
    count = [0, 0, 0, 0, 0, 0, 0, 0]
    print("Worgen's are humans who can transform into werewolf's,"
          "they ideally work alone,\n "
          "as one you will be able to be a number of different classes.\n"
          "Warrior, paladin, Hunter, Shaman, Mage,"
          "Monk, Death knight, Priest.\n"
          "In This final round of questions we will decided which class you "
          "have most in common with.\n"
          "Lets Begin")
    print("\nWould you rather\nA.Find the lost city of atlantis\nor"
          "\nB.Find Alexander the greats tomb")
    answer1 = input()
    while answer1 != "A" and answer1 != "B":
        print("Error, please print A or B.", end="")
        answer1 = input()
    if answer1 == "A":
        count[0] += 1
    elif answer1 == "B":
        count[1] += 1
    print("\nWould u rather\nA.Swim with dolphins\nor"
          "\nB.Swim with sharks")
    answer2 = input()
    while answer2 != "A" and answer2 != "B":
        print("Error, please print A or B.", end="")
        answer2 = input()
    if answer2 == "A":
        count[2] += 1
    elif answer2 == "B":
        count[3] += 1
    print("\nwould you enjoy\nA.Studying the environment\nor"
          "\nB.studying how the world works around us")
    answer3 = input()
    while answer3 != "A" and answer3 != "B":
        print("Error, please print A or B.", end="")
        answer3 = input()
    if answer3 == "A":
        count[4] += 1
    elif answer3 == "B":
        count[5] += 1
    print("\nWhich interests you more\nA.Baking a cake \nor\nB.Baking cookies")
    answer4 = input()
    while answer4 != "A" and answer4 != "B":
        print("Error, please print A or B.", end="")
        answer4 = input()
    if answer4 == "A":
        count[6] += 1
    elif answer4 == "B":
        count[7] += 1
    print("\nWould u rather\nA.Rest in a hammock\nor"
          "\nB.Rest in a rocking chair")
    answer5 = input()
    while answer5 != "A" and answer5 != "B":
        print("Error, please print A or B.", end="")
        answer5 = input()
    if answer5 == "A":
        count[1] += 1
    elif answer5 == "B":
        count[2] += 1
    print("\nWould you rather have\nA.Vr headset\nor\nB.Gaming console")
    answer6 = input()
    while answer6 != "A" and answer6 != "B":
        print("Error, please print A or B.", end="")
        answer6 = input()
    if answer6 == "A":
        count[3] += 1
    elif answer6 == "B":
        count[4] += 1
    print("\nAre you the type of person to\nA.Help others first\nor"
          "\nB.Help yourself first")
    answer7 = input()
    while answer7 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer7 = input()
    if answer7 == "A":
        count[5] += 1
    elif answer7 == "B":
        count[6] += 1
    print("\nWould you rather live in\nA.A busy city\nor\nB.A quiet town")
    answer8 = input()
    while answer8 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer8 = input()
    if answer8 == "A":
        count[7] += 1
    elif answer8 == "B":
        count[6] += 1
    print("You are a", wowClass[count.index(max(count))])
