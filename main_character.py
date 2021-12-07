from __future__ import annotations
from utils import slow_space_print

class Character():
    def __init__(self, name: str, hp: int, attack: int) -> None:
        self.name = name
        self.attack = attack
        self.hp = hp
        self.max_hp = hp
        self.magic_attack = 25

    def battle(self, other_character: Character):
        pass
    
    def show_hp_bar(self):
        proportion = int(self.hp/self.max_hp * 10)
        print(f"Your HP: {self.hp} / {self.max_hp}")
        print("----------")
        print("+" * proportion)
        print("----------")

class MainCharacter(Character):
    def __init__(self, name: str, hp: int, attack: int, mana: int, weapon: str) -> None:
        super().__init__(name, hp, attack)
        self.mana = mana
        self.weapon = weapon
        
        
    def battle(self, other_character: BaseEnemy):
         print("What to do?")
         self.show_hp_bar()
         print( f'MP: {self.mana}')
         print( f'{other_character.name}\'s HP: {other_character.hp} MP: {other_character.mana}')
         attack_points = 0
         while True:
            choice = input("1.Attack\n2.Fireball\n3.Heal\n4.Buff\n>")
            if choice.rstrip() == "1":
                attack_points = self.attack_enemy()
                break
            elif choice.rstrip() == "2":
                attack_points = self.throw_fireball()
                if other_character.name== "Dragon":
                    print("But the dragon is resistant against fire")
                    attack_points = 0
                break
            elif choice.rstrip() == "3":
                attack_points = self.heal()
                break
            elif choice.rstrip() == "4":
                self.buff_self()
                break
            else:
                continue
         other_character.hp -= attack_points
         
    def throw_fireball(self):
        if self.mana > 0:
            slow_space_print("You threw a powerful fireball", False, 0.05)
            slow_space_print(f"You dealt {self.magic_attack} damage!", False, 0.05)
            self.mana-=5
            return self.magic_attack
        else:
            slow_space_print("Out of mana!", False, 0.05)
            return 0
    
    def heal(self):
        slow_space_print("You patched your wounds and gained 25 HP!", False, 0.05)
        self.hp += 25
        self.mana-=10
        return 0
    
    def attack_enemy(self):
        slow_space_print(f"You strike at your enemy with your {self.weapon}", False, 0.05)
        slow_space_print(f"You dealt {self.attack} damage!", False, 0.05)
        return self.attack
    
    def buff_self(self):
        if self.attack < 31:
            slow_space_print("You concentrate and increase the power of your next strike...", False, 0.05)
            self.attack += 6
        else:
            slow_space_print("You cannot increase your attack more!", False, 0.05)
    
    def level_up(self):
        print("You leveled up!")
        print("You gained 20 mana!")
        print("Your fireball now does more damage!")
        self.hp = self.max_hp + 20
        self.max_hp = self.hp
        self.mana += 20
        self.magic_attack += 10
        
class BaseEnemy(Character):
    def __init__(self, name: str, hp: int, attack: int, mana: int) -> None:
        super().__init__(name, hp, attack)
        self.mana = mana
        
    def battle(self, other_character: Character):
        slow_space_print(f"The {self.name} attacks and deals {self.attack} damage!", False, 0.05)
        other_character.hp -= self.attack
        
    