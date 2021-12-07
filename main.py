from build_scenes import build_scene


def main():
    branch = build_scene()
    branch.play_all()
    
    
if __name__ == "__main__":
    main()
    