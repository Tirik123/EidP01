from dataclasses import dataclass


@dataclass
class Robot:
    hp: int         #Lebenspunkte
    armor: int      #Rüstung
    attack: int     #Angriffspunkte
    robot_typ: int  #Typ

    def __post_init__(self):
        assert self.robot_typ == 1 or self.robot_typ == 2 or self.robot_typ == 3

    def hit_damage(self, other):
        Schaden = self.attack - other.armor     #Schaden generell
        if self.robot_typ == 1:
            if other.robot_typ == 2:
                self.attack += 1
            elif other.robot_typ == 3:
                self.attack += 2
        if self.robot_typ == 2:
            if other.robot_typ == 1:
                self.armor += 2
        return Schaden
    
    def __ge__(self, other):
        iter_self = 0
        iter_other = 0
        while self.hp >= 0:
            iter_self += 1
            self.hp -= other.hit_damage(self)
        while other.hp >= 0:
            iter_other += 1
            other.hp -= self.hit_damage(other)
        if iter_self >= iter_other:
            return True
        elif iter_other >= iter_self:
            return False



if __name__ == '__main__':
    r1 = Robot(10, 1, 5, 1)
    r2 = Robot(16, 2, 3, 2) 
    #print(f'r1 dmg: [{r1.hit_damage(r2)}], r2 dmg: [{r2.hit_damage(r1)}]')
    #print(r1 >= r2)
    print(r1 >= Robot(10, 1, 5, 1))