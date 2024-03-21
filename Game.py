class Player:
    def __init__(self, name, health, attack_power, monster=None):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power
        self.__monster = monster

    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def attack_power(self):
        return self.__attack_power

    def attack(self, monster):
        monster.take_damage(self.__attack_power)
        print(f"{self.__name} attacks {monster.name} for {self.__attack_power} damage.")

    def take_damage(self, damage):
        self.__health -= damage

    def is_alive(self):
        return self.__health > 0

class Monster(Player):
    def attack(self, player):
        player.take_damage(self.attack_power)
        print(f"{self.name} attacks {player.name} for {self.attack_power} damage.")

def combat(player, monster):
    while player.is_alive() and monster.is_alive():
        player.attack(monster)
        monster.attack(player)
        print(f"{player.name} Health: {player.health}, {monster.name} Health: {monster.health}")

    return player

player1 = Player(name='Arianne', health=1000, attack_power=100)
monster1 = Monster(name='Balmond', health=500, attack_power=150)

combat(player1, monster1)