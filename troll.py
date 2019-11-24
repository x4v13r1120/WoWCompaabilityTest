"""
The 3rd and final phase of my program
"""


# troll-warrior paladin,hunter,rogue,shaman,mage,warlock,monk,druid,
# death knight,priest
def troll_Classes():
    """
This is were the Troll class will be decided
    """
    wowClass = ['Warrior', 'Hunter', 'Paladin', 'Mage',
                'Shaman', 'Monk', 'Priest', 'Death knight', 'Druid', 'Warlock']
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Troll are the voodoo doctors of Azeroth."
          "They enjoy being by the water and"
          "fishing is their main past time,\n "
          "as one you will be able to be a number of different classes.\n"
          "Warrior, paladin, Hunter, Shaman, Mage,"
          "Monk, Death knight, Priest.\n"
          "In This final round of questions we will decided which class you "
          "have most in common with.\n"
          "Lets Begin")
    print("\nWould you rather\nA.Go sky diving\nor\nB.Go budgie jumping")
    answer1 = input()
    while answer1 != "A" and answer1 != "B":
        print("Error, please print A or B.", end="")
        answer1 = input()
    if answer1 == "A":
        count[0] += 1
    elif answer1 == "B":
        count[1] += 1
    print("\nIf you had a superpower would you choose\nA.Flying\nor"
          "\nB.Super strength")
    answer2 = input()
    while answer2 != "A" and answer2 != "B":
        print("Error, please print A or B.", end="")
        answer2 = input()
    if answer2 == "A":
        count[2] += 1
    elif answer2 == "B":
        count[3] += 1
    print("\nDo u enjoy\nA.Exercising your body\nor\nB.Exercising your mind")
    answer3 = input()
    while answer3 != "A" and answer3 != "B":
        print("Error, please print A or B.", end="")
        answer3 = input()
    if answer3 == "A":
        count[4] += 1
    elif answer3 == "B":
        count[5] += 1
    print("\nWhich interests you more\nA.Economics\nor\nB.Politics")
    answer4 = input()
    while answer4 != "A" and answer4 != "B":
        print("Error, please print A or B.", end="")
        answer4 = input()
    if answer4 == "A":
        count[6] += 1
    elif answer4 == "B":
        count[7] += 1
    print("\nWould u rather\nA.Go to see a beautiful island\nor"
          "\nB.Go to see a magnificent mountain")
    answer5 = input()
    while answer5 != "A" and answer5 != "B":
        print("Error, please print A or B.", end="")
        answer5 = input()
    if answer5 == "A":
        count[1] += 1
    elif answer5 == "B":
        count[2] += 1
    print("\nWould you enjoy\nA.Going to a play\nor\nB.Going to a musical")
    answer6 = input()
    while answer6 != "A" and answer6 != "B":
        print("Error, please print A or B.", end="")
        answer6 = input()
    if answer6 == "A":
        count[3] += 1
    elif answer6 == "B":
        count[4] += 1
    print("\nWould you be more inclined to\nA.Research ancient history\nor"
          "\nB.Research future technology")
    answer7 = input()
    while answer7 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer7 = input()
    if answer7 == "A":
        count[5] += 1
    elif answer7 == "B":
        count[6] += 1
    print("\nWould you rather live in\nA.A cabin\nor\nB.A resort")
    answer8 = input()
    while answer8 != "A" and answer8 != "B":
        print("Error, please print A or B.", end="")
        answer8 = input()
    if answer8 == "A":
        count[7] += 1
    elif answer8 == "B":
        count[6] += 1
    print("\nWould you rather go to\nA.A water park\nor\nB.Aquarium")
    answer9 = input()
    while answer9 != "A" and answer9 != "B":
        print("Error, please print A or B.", end="")
        answer9 = input()
    if answer9 == "A":
        count[8] += 1
    elif answer9 == "B":
        count[9] += 1
    print("\nWould you rather live in\nA.A cabin\nor\nB.A resort")
    answer10 = input()
    while answer10 != "A" and answer10 != "B":
        print("Error, please print A or B.", end="")
        answer10 = input()
    if answer10 == "A":
        count[8] += 1
    elif answer10 == "B":
        count[9] += 1

    print("You are a", wowClass[count.index(max(count))])
