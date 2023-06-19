from   dataclasses import dataclass
from   typing      import Any, Optional, Union
import math
import pytest

## Aufgabe 4 (Dataclasses) #####################################################

@dataclass
class Ranking:
    club: str
    wins: int
    draws: int
    losses: int
    goals_achieved: int
    goals_conceded: int

    # Method is not required
    def points(self) -> int:
        return 3*self.wins + self.draws
    
    # Method is not required
    def goal_difference(self) -> int:
        return self.goals_achieved - self.goals_conceded

    def table_entry(self) -> str:
        games = self.wins + self.losses + self.draws
        return (f"{self.club} {games} {self.wins} {self.draws} {self.losses} " 
            + f"{self.goals_achieved}:{self.goals_conceded} {self.goal_difference()} {self.points()}")

    def __lt__(self, other):
        if isinstance(other, Ranking):
            if self.points() < other.points():
                return True
            elif self.points() == other.points() and self.goal_difference() < other.goal_difference():
                return True
            elif (self.points() == other.points() and self.goal_difference() == other.goal_difference()
                and self.goals_achieved < other.goals_achieved):
                return True
        return False