
import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.damage = damage
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__ (self, name, health, strength):
        super().__init__ (health, strength)
        self.name = name

    def receiveDamage(self,damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return (f'{self.name} has received {self.damage} points of damage')
        else:
            return (f'{self.name} has died in act of combat')

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def __init__ (self, health, strength):
        super().__init__ (health, strength)
    
    def receiveDamage(self,damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return (f'A Saxon has received {self.damage} points of damage')
        else:
            return (f'A Saxon has died in combat')

# War


class War:

    def __init__ (self):
        self.vikingArmy= []
        self.saxonArmy= []

    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        randomSaxon = random.choice(self.saxonArmy)
        randomViking = random.choice(self.vikingArmy)
        randomSaxon.receiveDamage(randomViking.strength)
        if randomSaxon.health <= 0:
            self.saxonArmy.remove(randomSaxon)
        
        return randomSaxon.receiveDamage(randomViking.strength)
    
    def saxonAttack(self):
        randomViking = random.choice(self.vikingArmy)
        randomSaxon = random.choice(self.saxonArmy)
        randomViking.receiveDamage(randomSaxon.strength)
        if randomViking.health <= 0:
            self.vikingArmy.remove(randomViking)
        
        return randomViking.receiveDamage(randomSaxon.strength)
        
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 :
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
