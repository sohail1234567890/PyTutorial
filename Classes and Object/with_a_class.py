
import datetime

class Cricketplayer:
    team_size = 11
    def __init__(self, fname, lname, birth_year, team):
        self.first_name = fname
        self.last_name  = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []


    def add_scores(self, score):
        self.scores.append(score)

    def get_average_scores(self):
        return sum(self.scores)/len(self.scores)

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def __str__(self):
        return f"{self.first_name} {self.last_name}, the cricket player  from {self.team}"

virat = Cricketplayer('virat', 'kohli', 1988, 'India')
virat.add_scores(37)
virat.add_scores(100)
virat.add_scores(23)

print(virat.first_name)
print(virat.last_name)
print(virat.birth_year)
print(virat.scores)
print(virat.get_average_scores())
print(f"Age of Virat {virat.get_age()}")

print(virat)