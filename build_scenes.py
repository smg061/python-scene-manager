
from scene import EventNode, BattleNode, Scene, Branch
from main_character import MainCharacter, BaseEnemy
from utils import slow_space_print


character = MainCharacter("Santos", 100, 21, 20, "sword")

enemy = BaseEnemy("Orc", 70, 20, 1)
enemy2 = BaseEnemy("Thief", 100, 20, 0)
enemy3 = BaseEnemy("Dragon", 120, 24, 100)

scene_one_text = ["====Cave Quest====\nBy Santos Gonzalez", "You wake up inside a dark cave with no memories of your past.\nYou have a pounding headache",
                  "You find a bag with items you recognize. Next to it, a sword",
                  "You decide to assess your surroundings.Suddenly you feel a figure rushing towards you.You ready yourself for battle"]

scene_two_text = ["You continue exploring the cave",
                  "You see a humanoid figure in the distance, but cannot discern it due to the cave's darkness "]

scene_three_text = ["You patch your wounds after a well fought battle",
                    "You feel like you're getting closer to the end",
                    "You can feel air flowing from the direction you're walking", 
                    "...", "You found the exit. Freedom is right in front of you. There is one small problem, however..."]

final_scene_text = ["You somehow deafeated the dragon guarding the exit ", "You're finally free from that creepy cave and all its dangers",
                    "You still don't know who you are, but at least you can ponder that in peace now", "Cave Quest END"]

def second_complete()-> bool:
    print("")
    input(">")
    return True

def searching_complete()-> bool:
    slow_space_print("...")
    slow_space_print("...")
    input("")
    return True

def complete_thief_battle():
    slow_space_print("The deafeated thief asks for mercy...")
    slow_space_print('"... please I was just scared! Please spare me!"')
    slow_space_print("Spare the thief?", False, 0.05)
    while True:
        choice = input("1.Spare\n2.Do not spare\n")
        if choice == "1":
            slow_space_print("You spare the thief and continue with your search for an exit")
            break
        elif choice == "2":
            slow_space_print("You show the thief no mercy. You continue with your search for an exit")
            break
    return True
        
def build_scene() -> Branch:
    test_scene = Scene()
    scene_two = Scene()
    scene_three = Scene()
    final_scene = Scene()
    battle_node = BattleNode("You are no match for me, boy (or girl)", character, enemy)

    for i, v in enumerate(scene_one_text):
        if i % 2 == 0: test_scene.add_node(EventNode(v))
        else: test_scene.add_node(EventNode(v, searching_complete))
    test_scene.add_node(battle_node)
    
    for text in scene_two_text:
        node = EventNode(text, second_complete)
        scene_two.add_node(node)
    
    battle_node = BattleNode('"Are you lost or something?..."', character, enemy2, complete_thief_battle)
    scene_two.add_node(battle_node)
        
    for text in scene_three_text:
        node = EventNode(text)
        scene_three.add_node(node)
        
    battle_node = BattleNode("ROAAAAAAAAAAAAHHHHHHRRRR", character, enemy3)
    scene_three.add_node(battle_node)
    
    for text in final_scene_text:
        node = EventNode(text)
        final_scene.add_node(node)
        
    branch = Branch()
    branch.add_scene(test_scene)
    branch.add_scene(scene_two)
    branch.add_scene(scene_three)
    branch.add_scene(final_scene)

    return branch

build_scene()