"""
The 3rd and final phase of my program
"""


# pandaren-warrior,hunter,rogue,shaman,mage,monk,priest

def pandaren_Classes():
    """
This is were the Pandaren class will be decided
    """
    wowClass = ['Warrior', 'Hunter', 'Rouge', 'Shaman',
                'Monk', 'Priest', 'Mage']
    count = [0, 0, 0, 0, 0, 0, 0]
    print("Pandaren's very peaceful in their ways, many in touch with"
          "the nature around them\n "
          "as one you will be able to be a number of different classes.\n"
          "Warrior, Hunter, Rouge, Shaman,"
          " Mage, Monk, Priest.\n"
          "In This final round of questions we will decided which class you "
          "have most in common with.\n"
          "Lets Begin")
    print("\nWould you rather do \nA.Work at home\nor"
          "\nB.Work at coffee shop")
    answer1 = input()
    while answer1 != "A" and answer1 != "B":
        print("Error, please print A or B.", end="")
        answer1 = input()
    if answer1 == "A":
        count[0] += 1
    elif answer1 == "B":
        count[1] += 1
    print("\nWould you rather go to\nA.Science museum\nor\nB.Space museum")
    answer2 = input()
    while answer2 != "A" and answer2 != "B":
        print("Error, please print A or B.", end="")
        answer2 = input()
    if answer2 == "A":
        count[2] += 1
    elif answer2 == "B":
        count[3] += 1
    print("\nDo u enjoy\nA.Solving problems\nor\nB.Asking questions")
    answer3 = input()
    while answer3 != "A" and answer3 != "B":
        print("Error, please print A or B.", end="")
        answer3 = input()
    if answer3 == "A":
        count[4] += 1
    elif answer3 == "B":
        count[5] += 1
    print("\nwhich Would you be more inclined to read about"
          "\nA.Sports\nor\nB.Fashion")
    answer4 = input()
    while answer4 != "A" and answer4 != "B":
        print("Error, please print A or B.", end="")
        answer4 = input()
    if answer4 == "A":
        count[6] += 1
    elif answer4 == "B":
        count[0] += 1
    print("\nWould you rather\nA.Draw a picture\nor"
          "\nB.Write a story")
    answer5 = input()
    while answer5 != "A" and answer5 != "B":
        print("Error, please print A or B.", end="")
        answer5 = input()
    if answer5 == "A":
        count[1] += 1
    elif answer5 == "B":
        count[2] += 1
    print("\nWould you enjoy\nA.Going for a bike ride\nor\nB.Going for a run")
    answer6 = input()
    while answer6 != "A" and answer6 != "B":
        print("Error, please print A or B.", end="")
        answer6 = input()
    if answer6 == "A":
        count[3] += 1
    elif answer6 == "B":
        count[4] += 1
    print("\nWould you rather\nA.Take out the trash\nor\nB.Wash the dishes")
    answer7 = input()
    while answer7 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer7 = input()
    if answer7 == "A":
        count[5] += 1
    elif answer7 == "B":
        count[6] += 1
    print("You are a", wowClass[count.index(max(count))])
