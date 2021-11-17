import time 

def slow_space_print(text, interval=0.1):
    """Slowly display text with spaces in between each letter and
    lowercase letter i's."""
    for character in text:
        if character == 'I':
            # I's are displayed in lowercase for style:
            print('i ', end='', flush=True)
        else:
            # All other characters are displayed normally:
            print(character + ' ', end='', flush=True)
        time.sleep(interval)
    print()  # Print two newlines at the end.
    print()
    

