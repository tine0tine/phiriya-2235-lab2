"""
Phiriya Trakoolwang, 633040223-5
Lab 2 Problem 6
"""

olympics_2020 = "Badminton: Thailand vs Great Britain" \
                "Table Tennis: Thailand vs Japan"
x, y, z = olympics_2020.split(":")
w = y.replace("Table Tennis", "")
e = y.replace("Thailand vs Great Britain", "")

print("For some olympics 2020 games of Thai athletes:")

print(f"For {x}, the game is between{w}")

print(f"For {e}, the game is between {z}")
