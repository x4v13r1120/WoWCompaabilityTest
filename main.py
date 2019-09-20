# Xavier Naranjo 09/12/2019
# Description of program
print("Welcome to, World of Warcraft Character Compatibility test!\n")

print("This is where you will pick\nYour true embodiment of a WoW character\nBased off a few rounds of questioning.\n")

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
allegiance=(input("A or B?\n"))
A=0
B=0
if allegiance=="A":
    A=A+1

elif allegiance=="B":
    B=B+1
else:
    print("ERROR...must be A or B.")
print("Interesting chocice lets keep going.\n")
print("Question 2\n\n")
choice3="A. Music Festival"
choice4="B. A House Party"
print("Would you rather go to",choice3 +"or",choice4,"\n")
allegiance=(input("A or B?\n"))
if allegiance=="A":
    A=A+1
elif allegiance=="B":
    B=B+1
else:
    print("ERROR...must be A or B.")
print("I'm more of a stay at home type myself.\n")
print("Question 3\n\n")
choice5="A.Go out to eat"
choice6="B.Cook at home"
print("Your roommates come to you asking you if you would rather ",choice5+" or",choice6,"\n")
allegiance=(input("A or B?\n"))
if allegiance=="A":
    A=A+1
elif allegiance=="B":
    B=B+1
else:
    print("ERROR...must be A or B.")






