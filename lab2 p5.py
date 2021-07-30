"""
Phiriya Trakoolwang, 633040223-5
Lab 2 Problem 5
"""

taekwondo_olympics_2020 = {
    "Gold": {"Thailand"},
}

taekwondo_olympics_2020.update({"Silver": {"spain"}, "Bronze": {"Israel", "Serbia"}})

print("The list of medal in Taekwondo 2020 woman 49 kilograms:")
for key, value in taekwondo_olympics_2020.items():
    for item in value:
        print(f"{item} received {key} medal")

print(f"The dictionary of medals is {taekwondo_olympics_2020}")
