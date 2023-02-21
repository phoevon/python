##Calculate dogs ages##
dog_size = ""
dog_age = ""

little_dog_dict = {"1": 15,
                   "2": 24,
                   "3": 28,
                   "4": 32,
                   "5": 36,
                   "6": 40,
                   "7": 44,
                   "8": 48,
                   "9": 52,
                   "10": 56,
                   "11": 60,
                   "12": 64,
                   "13": 68,
                   "14": 72,
                   "15": 76}
middle_dog_dict = {"1": 15,
                   "2": 24,
                   "3": 28,
                   "4": 32,
                   "5": 36,
                   "6": 42,
                   "7": 47,
                   "8": 51,
                   "9": 56,
                   "10": 60,
                   "11": 65,
                   "12": 69,
                   "13": 74,
                   "14": 78,
                   "15": 83}
big_dog_dict = {"1": 14,
                "2": 22,
                "3": 29,
                "4": 34,
                "5": 40,
                "6": 45,
                "7": 50,
                "8": 55,
                "9": 61,
                "10": 66,
                "11": 72,
                "12": 77,
                "13": 82,
                "14": 88,
                "15": 83}
giant_dog_dict = {"1": 14,
                  "2": 20,
                  "3": 28,
                  "4": 35,
                  "5": 42,
                  "6": 49,
                  "7": 56,
                  "8": 64,
                  "9": 61,
                  "10": 71,
                  "11": 78,
                  "12": 86,
                  "13": 93,
                  "14": 101,
                  "15": 108}


dog_size = input("WHAT'S YOUR DOG SIZE? \nIF LITTLE BREED <10KGS TYPE 1 \nIF MEDIUM BREED AMONG 10 AND 22KGS TYPE 2 \nIF BIG BREED AMONG 23 AND 40KGS TYPE 3 \nIF GIANT BREED 41< TYPE 4: ")
if dog_size == "1":
    dog_age = input("What's your little dog age? ")
elif dog_size == "2":
    dog_age = input("What's your middle weight dog age? ")
elif dog_size == "3":
    dog_age = input("What's your big dog age? ")
elif dog_size == "4":
    dog_age = input("What's your giant dog age? ")
else:
    print("Not a correct size")

if dog_size == "1":
    print("Your little dog has " + str(little_dog_dict[dog_age]) + " human years")
elif dog_size == "2":
    print("Your middle size dog has " + str(middle_dog_dict[dog_age]) + " human years")
elif dog_size == "3":
    print("Your big dog has " + str(big_dog_dict[dog_age]) + " human years")
else:
    print("Your giant dog has " + str(giant_dog_dict[dog_age]) + " human years")
