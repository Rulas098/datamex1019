# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - int(damage)
        return

    pass

# Viking

class Viking(Soldier):
    def __init__(self, health, strength, name):
        Soldier.__init__(self, health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - int(self.damage)
        if self.health > self.damage:
            print(self.name + ' puntos menos por el daño causado '.format(self.damage))
        else:
            print(self.name + ' has muerto')
        return

    def battleCry(self):
        return 'Odin Owns You All'
    pass

# Saxon

class Saxon(Soldier):
    def __index__(self, health , strength):
        Soldier.__init__(self, health. strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > self.damage:
            return ('Saxon recibio puntos menos de vida'.format(self.damage))
        else:
            return ('Saxon murio en la batalla')
    pass

# War

class War:
    pass
