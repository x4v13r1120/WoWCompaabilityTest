def allianceOptions():
    print("You belong to the Alliance\n"
          "A humble group of courageous hero's posed to protect Azeroth\n"
          "From those who want to destroy it")
    print("The next round of questions\nWill deal with what type of race you are\n")
    print("there are 13 different races in total\n"
          "7 in Alliance and 7 in horde\n"
          "one race can be played in either Horde or Alliance\n"
          "for Alliance there is Human, Dwarf, Night Elf, Gnome, Draenei and Worgen \n"
          "and the Pandaren which is the one race that can be played on both sides.\n"
          "In the Horde there is Orc, Undead, Tauren, Troll, Blood Elf and Goblin\n"
          "as well as the Pandaren again.")
    print("Each race has a certain amount of classes they can choose from that vary from race to race\n"
          "but we will get into that later.\n"
          "Since there are so many races there will be ten questions asked in this round.\n")
    print("So lets get started!!!\n\n")

    race = ['NightElf', 'Dwarf', 'Human', 'Gnome', 'Draenei', 'Worgen', 'Pandaren']
    count = [0, 0, 0, 0, 0, 0, 0]

    from string import ascii_uppercase
    print("Are you more of , A. A person who enjoys being outside or B. A person who enjoys spending the day outside ?")
    answer1 = input()
    while answer1 not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        answer1 = input()
    if answer1 == "A":
        count[0] += 1
    elif answer1 == "B":
        count[1] += 1
    print("Do you A. Enjoy being in the dark or B. Enjoy being in the wilderness ?")
    answer2 = input()
    while answer2 not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        answer2 = input()
    if answer2 == "A":
        count[2] += 1
    elif answer2 == "B":
        count[3] += 1
    print("Are you someone who A.Sees the light as a source of pureness and power or B. Someone who prefers the "
          "shadows ?")
    answer3 = input()
    while answer3 not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        answer3 = input()
    if answer3 == "A":
        count[4] += 1
    elif answer3 == "B":
        count[5] += 1
    print("Are you A. Tranquil and clam minded or B. Head-fast and strong minded ?")
    answer4 = input()
    while answer4 not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        answer4 = input()
    if answer4 == "A":
        count[6] += 1
    elif answer4 == "B":
        count[0] += 1
    print("Do you enjoy A. building things or B. fixing things ?")
    answer5 = input()
    while answer5 not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        answer5 = input()
    if answer5 == "A":
        count[1] += 1
    elif answer5 == "B":
        count[2] += 1
    print("Would you be more inclined to A. Harness the power of the land or B. Harness the power of gems ?")
    answer6 = input()
    while answer6 not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        answer6 = input()
    if answer6 == "A":
        count[3] += 1
    elif answer6 == "B":
        count[4] += 1
    print("Are you the type of person to  A. Embrace a family or B. embrace solidarity ?")
    answer7 = input()
    while answer7 not in ascii_uppercase:
        print("Error, please print A or B.", end="")
        answer7 = input()
    if answer7 == "A":
        count[5] += 1
    elif answer7 == "B":
        count[6] += 1
    print("You have most in common with the,", race[count.index(max(count))])


