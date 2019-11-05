
from string import ascii_uppercase

import alliance
import horde


def main():
    # Xavier Naranjo 09/12/2019
    # Description of program
    print("Welcome to, World of Warcraft Character Compatibility test!\n")

    print(
        "This is where you will pick\nYour true embodiment of a WoW character\nBased off a few rounds of questioning.\n")

    name = input("First and foremost, what is your name?")

    print("welcome", name + " to your first encounter to the world of Azeroth!!\n")
    # first round of questions will be for allegiance
    # second round of questions will be for race\
    # third round of questions will be for class

    print("Question 1\n\n")

    print("You are put in a position where you are stuck between\ngoing after purse robbers to help a woman\n"
          "or taking up a rather large amount of cash\nthat was dropped beside you.\n ")

    choice1 = "A.help the women"
    choice2 = "B.take the cash"
    print("Do you", choice1 + " or", choice2)
    allegiance = (input("A or B?\n"))
    A = 0
    B = 0
    while allegiance not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        allegiance = input()
    if allegiance == "A":
        A = A + 1

    elif allegiance == "B":
        B = B + 1
    else:
        print("ERROR...must be A or B.")
    print("Interesting chocice lets keep going.\n")
    print("Question 2\n\n")
    choice3 = "A. Music Festival"
    choice4 = "B. A House Party"
    print("Would you rather go to", choice3 + " or", choice4, "\n")
    allegiance = (input("A or B?\n"))
    while allegiance not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        allegiance = input()
    if allegiance == "A":
        A = A + 1
    elif allegiance == "B":
        B = B + 1
    else:
        print("ERROR...must be A or B.")
    print("I'm more of a stay at home type myself.\n")
    print("Question 3\n\n")
    choice5 = "A.Go out to eat"
    choice6 = "B.Cook at home"
    print("Your roommates come to you asking you if you would rather ", choice5 + " or", choice6, "\n")
    allegiance = (input("A or B?\n"))
    while allegiance not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        allegiance = input()
    if allegiance == "A":
        A = A + 1
    elif allegiance == "B":
        B = B + 1
    else:
        print("ERROR...must be A or B.\n")
    print("Yummy food... I should go eat....\n")
    print("Question 4\n\n")
    choice7 = "A. Apple"
    choice8 = "B. Android"
    print("This one is the big question", choice7 + " or", choice8, "\n")
    allegiance = (input("A or B?\n"))
    while allegiance not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        allegiance = input()
    if allegiance == "A":
        A = A + 1
        print("Apple squad\n")
    elif allegiance == "B":
        B = B + 1
        print("....Lowkey the better choice\n")
    else:
        print("ERROR...must be A or B.")
    print("Last one for the first round.\n")
    print("Question 5\n\n")
    choice9 = "A. yes"
    choice10 = "B. no"
    print("Do you like pineapples on pizza?", choice9 + " or", choice10, "\n")
    allegiance = (input("A or B?\n"))
    while allegiance not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        allegiance = input()
    if allegiance == "A":
        A = A + 1
    elif allegiance == "B":
        B = B + 1
    else:
        print("ERROR...must be A or B.")
    if A >= 3:
        alliance.allianceOptions()
    elif B >= 3:
        horde.hordeOptions()


main()
