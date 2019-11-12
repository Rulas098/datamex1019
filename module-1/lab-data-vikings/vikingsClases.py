
# Soldier


class Soldier:
    pass

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage=0):
        self.health = self.health - damage

# Viking

class Viking(Soldier):

    def __init__(self,name,health,strength):
        self.name=name
        super().__init__(health,strength)
    def receiveDamage(self,damage=0):
        self.health = self.health -damage
        if self.health > 0:
            return '{} has received {} points of damage'.format(self.name, damage)
        else:
            return '{} has died in act of combat'.format(self.name)
    def battleCry(self):
        return 'Odin Owns You All!'
    pass

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage=0):
        self.health = self.health - damage
        if self.health > 0:
            return 'A Saxon has received {} points of damage'.format(damage)
        else:
            return 'A Saxon has died in combat'
    pass
# War


class War:
    pass
