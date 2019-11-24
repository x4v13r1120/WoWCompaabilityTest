"""
The 3rd and final phase of my program
"""


# orc-warrior,hunter,rogue,shaman,mage,warlock,monk,death knight

def orc_Classes():
    """
This is were the Orc class will be decided
    """
    wowClass = ['warrior', 'shaman', 'hunter', 'rouge', 'mage', 'warlock',
                'monk', 'death knight']
    count = [0, 0, 0, 0, 0, 0, 0, 0]
    print("Orc's are the opposites to humans's just as common."
          "They are big brutes who enjoy fighting over anything,\n"
          "as one you will be able to be a number of different classes.\n"
          "Warrior, Shaman, Hunter, Rouge, Mage, Warlock, Monk,"
          "and Death knight are the ones humans are able to be.\n"
          "In This final round of questions we will decided which class u "
          "have most in common with.\n"
          "Lets Begin")
    print("\nWould you rather have\nA. A sword and shield\nor"
          "\nB.Use magic and a sword ")
    answer1 = input()
    while answer1 != "A" and answer1 != "B":
        print("Error, please print A or B.", end="")
        answer1 = input()
    if answer1 == "A":
        count[0] += 1
    elif answer1 == "B":
        count[1] += 1
    print("\nWould u rather\nA.Use a bow\nor\nB.Use daggers")
    answer2 = input()
    while answer2 != "A" and answer2 != "B":
        print("Error, please print A or B.", end="")
        answer2 = input()
    if answer2 == "A":
        count[2] += 1
    elif answer2 == "B":
        count[3] += 1
    print("\nDo u enjoy\nA.Cast spells\nor\nB.Cast curses")
    answer3 = input()
    while answer3 != "A" and answer3 != "B":
        print("Error, please print A or B.", end="")
        answer3 = input()
    if answer3 == "A":
        count[4] += 1
    elif answer3 == "B":
        count[5] += 1
    print("\nDo you like\nA.Giving allies buffs\nor\nB.Healing allies")
    answer4 = input()
    while answer4 != "A" and answer4 != "B":
        print("Error, please print A or B.", end="")
        answer4 = input()
    if answer4 == "A":
        count[6] += 1
    elif answer4 == "B":
        count[0] += 1
    print(
        "\nWould u rather\nA.Play as a Tank\nor"
        "\nB.Play as a high damage giver")
    answer5 = input()
    while answer5 != "A" and answer5 != "B":
        print("Error, please print A or B.", end="")
        answer5 = input()
    if answer5 == "A":
        count[1] += 1
    elif answer5 == "B":
        count[2] += 1
    print("\nWould you rather\nA.go on  hike with friends\nor\nB.Go on a hike "
          "by yourself")
    answer6 = input()
    while answer6 != "A" and answer6 != "B":
        print("Error, please print A or B.", end="")
        answer6 = input()
    if answer6 == "A":
        count[3] += 1
    elif answer6 == "B":
        count[4] += 1
    print(
        "\nAre you the type of person to \nA.Eat at a pub\nor\nB.Eat at a "
        "gourmet ")
    answer7 = input()
    while answer7 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer7 = input()
    if answer7 == "A":
        count[5] += 1
    elif answer7 == "B":
        count[6] += 1
    print(
        "\nAt the grocery store\nA.Paper\nor\nB.Plastic")
    answer8 = input()
    while answer8 != "A" and answer8 != "B":
        print("Error, please print A or B.", end="")
        answer8 = input()
    if answer8 == "A":
        count[7] += 1
    elif answer8 == "B":
        count[0] += 1

    print("You are a", wowClass[count.index(max(count))])
