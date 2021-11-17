
from typing import Text
from scene import TextNode, Scene, SceneManager

my_text = ["Hello", "Goodbye", "Die Today", "Hell yeah baby"]
def build_scene():
    
    test_scene = Scene()
    
    for text in my_text:
        node = TextNode(text)
        test_scene.add_node(node)
        
    while test_scene.head.next_node is not None:
        test_scene.head.complete_scene()
        test_scene.head.play_text()
        test_scene.go_to_next_scene()
    pass
    
    
build_scene()

    