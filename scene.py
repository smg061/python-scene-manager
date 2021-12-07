
from __future__ import annotations
from utils import slow_space_print
from main_character import BaseEnemy, Character, MainCharacter


def generic_complete():
    input(">")
    return True

class EventNode():
    def __init__(self, text_body: str, complete_conditions: function = generic_complete) -> None:
        self.text_body = text_body
        self.completed = False
        self.complete_conditions = complete_conditions
        self.next_node = None
        self.game_over = False
        
    def complete_event(self):
        is_completed = self.complete_conditions()
        if is_completed:
            self.completed = True
        
    def play_text(self):
        slow_space_print(self.text_body)
        return
    

class BattleNode(EventNode):
    def __init__(self, text_body: str, main_character: MainCharacter, enemy: BaseEnemy, complete_conditions: function = generic_complete) -> None:
        super().__init__(text_body, complete_conditions=complete_conditions)
        self.main_character= main_character
        self.enemy = enemy
        self.game_over = False
        
    def complete_event(self):
        slow_space_print(f'You\'re being attacked by a vicious {self.enemy.name}!', False, 0.05)
        result = self.battle()
        if result is True:
            super().complete_event()
        else: 
            self.show_gameover()
            self.game_over = True
    
    def battle(self):
        while self.main_character.hp > 0 and self.enemy.hp > 0:
            self.main_character.battle(self.enemy)
            if self.main_character.hp <= 0 or self.enemy.hp <= 0:
                break
            self.enemy.battle(self.main_character)
        if self.main_character.hp <= 0:
            print("You were defeated!")
            return False
        else:
            print("You claim victory. For now...")
            self.main_character.level_up()
            return True
        
    def show_gameover(self):
        slow_space_print("You have succumbed to the wounds you suffered in battle", False, 0.05)
        slow_space_print("GΛMΣ-ӨVΣЯ")
        self.game_over = True
        self.next_node = None
            
        
    
class Scene():
    def __init__(self) -> None:
        self.head: EventNode = None
        self.next_scene: Scene = None
        self.is_completed_scene = False
        self.game_over = False
    
    def add_node(self, node: EventNode):
        current_node: EventNode = self.head
        if self.head is None:
            self.head = node
        else:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = node
    
    def go_to_next_scene(self):
        self.head.play_text()
        self.head.complete_event()            
        if self.head.game_over:
            self.head.next_node = None
            self.game_over = True
            
        elif self.head.completed and not self.head.game_over:
            self.head = self.head.next_node
            if self.head is None:
                self.is_completed_scene = True    
                     

class Branch():
    def __init__(self, next_branch: Branch = None):
        self.head: Scene = None
        self.game_over = False
        
    def add_scene(self, scene: Scene):
        current_node: Scene = self.head
        if self.head is None:
            self.head = scene
        else:
            while current_node.next_scene is not None:
                current_node = current_node.next_scene
            current_node.next_scene = scene
            
    def play_scene(self):
        if self.head is None: 
            return
        while not self.head.is_completed_scene:
            if self.head.game_over:
                break
            self.head.go_to_next_scene()
            
        if self.head is not None and self.head.is_completed_scene:
            self.head = self.head.next_scene
            
        elif self.head.game_over:
            self.head = None
            
    def play_all(self):
        while self.head is not None:
            self.play_scene()
    