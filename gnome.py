# gnome- warrior,hunter,rouge,mage,warlock,monk,death knight, priest

"""
The 3rd and final phase of my program
"""


def gnome_Classes():
    """
This is were the Gnome class will be decided
    """
    wowClass = ['Warrior', 'Hunter', 'Rouge', 'Mage', 'warlock',
                'Monk', 'Priest', 'Death knight']
    count = [0, 0, 0, 0, 0, 0, 0, 0]
    print("Gnome are the crafty ones who enjoy tinkering with metals and "
          "springs to create new mounts and gadgets"
          " in the world of Azeroth,\n "
          "as one you will be able to be a number of different classes.\n"
          "Warrior, Demon hunter, Hunter, Rouge, Druid,"
          " Mage, Death knight, Monk, Priest.\n"
          "In This final round of questions we will decided which class you "
          "have most in common with.\n"
          "Lets Begin")
    print("\nWould you rather\nA.Watch a documentary\nor"
          "\nB.Watch a Action thriller")
    answer1 = input()
    while answer1 != "A" and answer1 != "B":
        print("Error, please print A or B.", end="")
        answer1 = input()
    if answer1 == "A":
        count[0] += 1
    elif answer1 == "B":
        count[1] += 1
    print("\nGo on to a\nA.African safari\nor\nB.Amazonian Jungle")
    answer2 = input()
    while answer2 != "A" and answer2 != "B":
        print("Error, please print A or B.", end="")
        answer2 = input()
    if answer2 == "A":
        count[2] += 1
    elif answer2 == "B":
        count[3] += 1
    print("\nDo u enjoy\nA.Learning\nor\nB.Teaching")
    answer3 = input()
    while answer3 != "A" and answer3 != "B":
        print("Error, please print A or B.", end="")
        answer3 = input()
    if answer3 == "A":
        count[4] += 1
    elif answer3 == "B":
        count[5] += 1
    print("\nwhich Would u like more\nA.Fishing\nor\nB.Hunting")
    answer4 = input()
    while answer4 != "A" and answer4 != "B":
        print("Error, please print A or B.", end="")
        answer4 = input()
    if answer4 == "A":
        count[6] += 1
    elif answer4 == "B":
        count[7] += 1
    print("\nWhat would you rather have for breakfast\nA.Pancakes\nor"
          "\nB.Waffles")
    answer5 = input()
    while answer5 != "A" and answer5 != "B":
        print("Error, please print A or B.", end="")
        answer5 = input()
    if answer5 == "A":
        count[1] += 1
    elif answer5 == "B":
        count[2] += 1
    print("\nWould you enjoy\nA.Tofu\nor\nB.Chicken")
    answer6 = input()
    while answer6 != "A" and answer6 != "B":
        print("Error, please print A or B.", end="")
        answer6 = input()
    if answer6 == "A":
        count[3] += 1
    elif answer6 == "B":
        count[4] += 1
    print("\nWould you rather go\nA.On a cruise\nor\nB.On road trip")
    answer7 = input()
    while answer7 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer7 = input()
    if answer7 == "A":
        count[5] += 1
    elif answer7 == "B":
        count[6] += 1
    print("\nDo you like when it rains\nA.Yes\nor\nB.No")
    answer8 = input()
    while answer8 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer8 = input()
    if answer8 == "A":
        count[7] += 1
    elif answer8 == "B":
        count[8] += 1
    print("\nWhich would you rather see\nA.The pyramids\nor"
          "\nB.The Cedar wood forest")
    answer9 = input()
    while answer9 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer9 = input()
    if answer9 == "A":
        count[8] += 1
    elif answer9 == "B":
        count[4] += 1
    print("You are a", wowClass[count.index(max(count))])
