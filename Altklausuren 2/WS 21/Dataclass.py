from dataclasses import dataclass

@dataclass
class Ranking:
    club: str
    wins: int
    draws: int
    losses: int
    goals_achieved: int
    goals_conceded: int

    def table_entry(self) -> str:
        count_games = self.wins + self.draws + self.draws
        points = 0
        points += self.wins * 3 + self.draws
        difference_goals = self.goals_achieved - self.goals_conceded
        return f'{self.club} {count_games} {self.wins} {self.draws} {self.losses} {self.goals_achieved}:{self.goals_conceded} {difference_goals} {points}'
    
    def __lt__(self: 'Ranking', other: "Ranking") -> bool:
        self.count_games = self.wins + self.draws + self.draws
        self.points = 0
        self.points += self.wins * 3 + self.draws
        self.difference_goals = self.goals_achieved - self.goals_conceded
        other.count_games = other.wins + other.draws + other.draws
        other.points = 0
        other.points += other.wins * 3 + other.draws
        other.difference_goals = other.goals_achieved - other.goals_conceded
        if self.points < other.points:
            return True
        elif self.points == other.points:
            if self.difference_goals < other.difference_goals:
                return True
            elif self.difference_goals == other.difference_goals:
                if self.goals_achieved < other.goals_achieved:
                    return True
        return False




if __name__ == '__main__':
    print(Ranking("FC H.", 6, 2, 2, 23, 14).table_entry())
    r1 = Ranking("FC H.", 6, 2, 2, 23, 14)
    r2 = Ranking("FC U.", 5, 3, 2, 20, 15)
    print(r2 < r1)
    print(r1 < r1)
