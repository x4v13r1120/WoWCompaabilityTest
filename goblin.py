# goblin-warrior,hunter,rogue,shaman,mage,warlock,death knight
"""
The 3rd and final phase of my program
"""


def goblin_Classes():
    """
This is were the goblin class will be decided
    """
    wowClass = ['warrior', 'hunter', 'rouge', 'mage',
                'warlock','death knight']
    count = [0, 0, 0, 0, 0, 0,]
    print("Goblins are the ones in azeroth with quick hands and fast minds,\n"
          "as one you will be able to be a number of different classes.\n"
          "Warrior, Hunter, Rouge, Shaman,"
          " Mage, Warlock "
          "and Death knight are available to dwarfs.\n"
          "In This final round of questions we will decided which class you "
          "have most in common with.\n"
          "Lets Begin")
    print("\nDo you enjoy\nA. watching tv\nor\nB.Using your phone")
    answer1 = input()
    while answer1 != "A" and answer1 != "B":
        print("Error, please print A or B.", end="")
        answer1 = input()
    if answer1 == "A":
        count[0] += 1
    elif answer1 == "B":
        count[1] += 1
    print("\nWould you be more inclined to watch a movie\nA.In a "
          "theater\nor\nB.At a drive in")
    answer2 = input()
    while answer2 != "A" and answer2 != "B":
        print("Error, please print A or B.", end="")
        answer2 = input()
    if answer2 == "A":
        count[2] += 1
    elif answer2 == "B":
        count[3] += 1
    print("\nDo u enjoy\nA.Going for car rides\nor\nB.Going for walks")
    answer3 = input()
    while answer3 != "A" and answer3 != "B":
        print("Error, please print A or B.", end="")
        answer3 = input()
    if answer3 == "A":
        count[4] += 1
    elif answer3 == "B":
        count[5] += 1
    print("\nWhich interests you more\nA.Science\nor\nB.Art")
    answer4 = input()
    while answer4 != "A" and answer4 != "B":
        print("Error, please print A or B.", end="")
        answer4 = input()
    if answer4 == "A":
        count[6] += 1
    elif answer4 == "B":
        count[9] += 1
    print(
        "\nWould u rather\nA.Go to the gym\nor"
        "\nB.Go play basketball")
    answer5 = input()
    while answer5 != "A" and answer5 != "B":
        print("Error, please print A or B.", end="")
        answer5 = input()
    if answer5 == "A":
        count[1] += 1
    elif answer5 == "B":
        count[2] += 1
    print("\nWould you enjoy\nA.Baking\nor\nB.Grilling")
    answer6 = input()
    while answer6 != "A" and answer6 != "B":
        print("Error, please print A or B.", end="")
        answer6 = input()
    if answer6 == "A":
        count[3] += 1
    elif answer6 == "B":
        count[4] += 1
    print("\nWould you rather go\nA.On a fishing trip\nor\nB.A Camping trip")
    answer7 = input()
    while answer7 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer7 = input()
    if answer7 == "A":
        count[5] += 1
    elif answer7 == "B":
        count[0] += 1

    print("You are a", wowClass[count.index(max(count))])
    print("")
