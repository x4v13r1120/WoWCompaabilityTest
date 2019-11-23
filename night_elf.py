"""
The 3rd and final phase of my program
"""


def night_elf_Classes():
    """
This is were the Night Elf class will be decided
    """
    wowClass = ['Warrior', 'Hunter', 'Rouge', 'Mage', 'Demon Hunter',
                'Druid', 'Monk', 'Priest', 'Death knight']
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Night elf are solitary people who like to stick to there own roots "
          "and people rather than mingle with the other races in Azeroth,\n"
          "as one you will be able to be a number of different classes.\n"
          "Warrior, Demon hunter, Hunter, Rouge, Druid,"
          " Mage, Death knight, Monk, Priest.\n"
          "In This final round of questions we will decided which class you "
          "have most in common with.\n"
          "Lets Begin")
    print("\nWould you rather\nA.Go shopping\nor\nB.Window shop")
    answer1 = input()
    while answer1 != "A" and answer1 != "B":
        print("Error, please print A or B.", end="")
        answer1 = input()
    if answer1 == "A":
        count[0] += 1
    elif answer1 == "B":
        count[1] += 1
    print("\nAt the movies would you eat\nA.Popcorn\nor\nB.Candy")
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
    print("\nWhich interests you more\nA.Math\nor\nB.Music")
    answer4 = input()
    while answer4 != "A" and answer4 != "B":
        print("Error, please print A or B.", end="")
        answer4 = input()
    if answer4 == "A":
        count[6] += 1
    elif answer4 == "B":
        count[7] += 1
    print("\nWould u rather\nA.Go on a ferris wheel\nor"
          "\nB.On a roller coaster")
    answer5 = input()
    while answer5 != "A" and answer5 != "B":
        print("Error, please print A or B.", end="")
        answer5 = input()
    if answer5 == "A":
        count[1] += 1
    elif answer5 == "B":
        count[2] += 1
    print("\nWould you enjoy\nA.Sleeping in\nor\nB.Getting up early")
    answer6 = input()
    while answer6 != "A" and answer6 != "B":
        print("Error, please print A or B.", end="")
        answer6 = input()
    if answer6 == "A":
        count[3] += 1
    elif answer6 == "B":
        count[4] += 1
    print("\nWould you rather go\nA.To a carnival\nor\nB.To a cook out")
    answer7 = input()
    while answer7 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer7 = input()
    if answer7 == "A":
        count[5] += 1
    elif answer7 == "B":
        count[6] += 1
    print("\nWould you rather\nA.Talk\nor\nB.Text")
    answer8 = input()
    while answer8 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer8 = input()
    if answer8 == "A":
        count[7] += 1
    elif answer8 == "B":
        count[8] += 1
    print("\nAre the type to\nA.Express yourself\nor"
          "\nB.Keep things bottled up")
    answer9 = input()
    while answer9 != "A" and answer7 != "B":
        print("Error, please print A or B.", end="")
        answer9 = input()
    if answer9 == "A":
        count[8] += 1
    elif answer9 == "B":
        count[4] += 1
    print("You are a", wowClass[count.index(max(count))])
