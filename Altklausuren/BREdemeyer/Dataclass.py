from dataclasses import dataclass

@dataclass(frozen = True)
class GameObject:
    spNr: int
    league: str
    sr: set[str]


    def __lt__(self, other: "GameObject") -> bool:
        if self.league == other.league:
            return self.spNr < other.spNr
        return self.league < other.league
    

    def log(self) -> str:
        return f'Spiel: Sp-Nr. {self.spNr} @ {self.league} ({self.sr} & {self.sr})'
    

@dataclass(frozen = True)
class NormalGameObject(GameObject):

    def __post_init__(self):
        assert self.league[:4] != "pok-"

    
    def log(self) -> str:
        return "Runden-" + super().log()



@dataclass(frozen = True)
class PokalGameObject(GameObject):
    def __post_init__(self):
        assert self.league[:4] == "pok-"
        assert len(self.sr) >= 2


    def log(self) -> str:
        return "Pokal-" + super().log()

# GameObject = NormalGameObject | PokalGameObject

            
def sort_games(list_GO: list[GameObject]) -> tuple[list[int], list[int]]:
    empty_tuple = ([], [])
    for i in list_GO:
        match i:
            case NormalGameObject():
                empty_tuple[0].append(i.spNr)
            case PokalGameObject():
                empty_tuple[1].append(i.spNr)
    return empty_tuple


if __name__ == '__main__':
    g2 = GameObject(130002, "l2", {"SR B", "SR C"})
    g1 = GameObject(130001, "l1", {"SR A"})
    print(g1.log())
    g4 = PokalGameObject(130004, "pok-l1", {"SR A", "SR B"})
    print(g4.log())
    g3 = NormalGameObject(130003, "l1", {"SR A", "SR B"})
    print(g3.log())
