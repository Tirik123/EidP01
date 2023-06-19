from dataclasses import dataclass

#a)
@dataclass
class Ranking():
    club: str  # der Name des Vereins
    wins: int  # die Anzahl der gewonnen Spiele -> 3 Pkt
    draws: int  # die Anzahl der Unentschieden -> 1 Pkt
    losses: int  # die Anzahl der verlorenen Spiele -> 0 Pkt
    goals_achieved: int  # Tore die der Verein erzielt hat
    goals_conceded: int  # Tore die der Verein erlitten hat
    

    def punkte(self):
        return self.wins * 3 + self.draws
    

    def anzahl_spiele(self):
        return self.wins + self.draws + self.losses


    def tordifferenz(self):
        return self.goals_achieved - self.goals_conceded


    def table_entry(self) -> str:
        return f"{self.club} {self.anzahl_spiele()} {self.wins} {self.draws} {self.losses} {self.goals_achieved}:{self.goals_conceded} {self.punkte()}"


    def __lt__(self, other):
        if isinstance(other, Ranking):
            if self.punkte() == other.punkte() and self.tordifferenz() < other.tordifferenz():
                return True
            elif self.punkte() < other.punkte():
                return True
            elif self.punkte() == other.punkte() and self.tordifferenz() == other.tordifferenz():
                if self.goals_achieved < other.goals_achieved:
                    return True
        return False


    

if __name__ == '__main__':
    print(Ranking("FC H.", 6, 2, 2, 23, 14).table_entry())
    r1 = Ranking("FC H.", 6, 2, 2, 23, 14)
    r2 = Ranking("FC U.", 5, 3, 2, 20, 15)
    print(r2 < r1)
    print(r1 < r1)

