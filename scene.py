
from __future__ import annotations
from typing import Text
from utils import slow_space_print

class TextNode():
    def __init__(self, text_body: str) -> None:
        self.text_body = text_body
        self.completed = False
        self.next_node = None
        
    def complete_scene(self):
        self.completed = True
        
    def play_text(self):
        slow_space_print(self.text_body)
        return
    
        
    
class Scene():
    def __init__(self) -> None:
        self.head = None
        
    
    def add_node(self, node: TextNode):
        current_node: TextNode = self.head
        if self.head is None:
            self.head = node
        else:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = node
        
    def go_to_next_scene(self):
        if self.head.completed:
            self.head = self.head.next_node
            
        self.head.play_text()

class Branch():
    def __init__(self, next_branch: Branch = None):
        pass
         
class SceneManager():
    def __init__(self, scenes: list[Scene]) -> None:
        self.scenes = scenes
    
    def play_scene():
        """"plays currently selected"""
        pass