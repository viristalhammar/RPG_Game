import random

class Magic:
    """
    This Magic has name, mp cost, damge, type
    """
    def __init__(self,name,mp_cost,damage,magic_type):
        self.name = name
        self.mp = mp_cost
        self.damage = take_damage
        self.magic_type = magic_type
        self.high_damage = damage + 15
        self.low_damage = damage - 15

    def generate_magic_damage(self):
        dmg = random.randrage(self.low_damage,self.high_damage)
        return dmg
