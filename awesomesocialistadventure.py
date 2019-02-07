answer = input("Play? (yes/no) ")

if answer.lower().strip() == "yes":
    answer = input("""You are a small boy, a factory worker in a small fantasy village.
you have been reading socialist literature, and have taken it upon yourself to slay the bourgeosie dragon
that runs your factory. You have gone near his office cave, knowing that his three headed
giant dog guard will slay you on sight, as the dragon has said to do to all workers who go near
his office. You are armed with a sword. (slay the guard/stand still)""")
    
    if answer.lower().strip() == "slay the guard":
        answer = input("""You slay the guard quickly, with ease. You see the
dragon at his desk, counting his unearned money. Do you slay him, or stand
still? (slay him/stand still)""")
    
        if answer.lower().strip() == "slay him":
            print("congratulations! The dragon is slain and the factory belongs to the workers!")
        else:
            print("The dragon slays you, and the revolution is lost.")
    
    else:
        print("The guard tears you apart, and the revolution is lost.")

else:
    print("Aw, come back when you wanna play!")