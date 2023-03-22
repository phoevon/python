import re
import json
import sys

with open("localization.json", "r+", encoding='utf-8') as json_file:
     content = json_file.read()
decoded_content = json.loads(content)


found = True
def player_search(for_search, decoded_content):
    for_search = input("Enter a data to search ")
    if not for_search:
     print("Must introducing something searcheable")
    sys.exit()
    for data in decoded_content["la_liga"]:
        if for_search in data["NAME"]:
            found = True
            name = data["NAME"]
            country = data["COUNTRY"]
            position = data["POSITION"]
            club = data["CLUB"]
            age = data["AGE"]
            week = data["WEEK"]
            year = data["YEAR"]
            identification = data["ID"]
            print(f"The player {name} is {age} years old and plays at {position}  in the club {club} and earn {week} at week ")
            exit()
        elif for_search in data["CLUB"]:
            found = True
            club = data["CLUB"]
            print(f"The {club} have the next players :") 
            for d in decoded_content["la_liga"]:
                if d["CLUB"] == club:
                    name = d["NAME"]
                    country = d["COUNTRY"]
                    print(f"- {name} and plays at position {position}")
        if found:
            sys.exit()
    
    print("No match.")

        






