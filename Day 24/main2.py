# with open("Day 24/scoreboard.py") as file:
#     contents = file.read()
#     print(contents)


def sum(no1,no2):
    return no1+ no2

with open("Day 24/score.txt",mode="a") as file:
     file.write("\nsum")
     
   
with open("Day 24/score.txt") as file:
    contents = file.read()
    print(contents)