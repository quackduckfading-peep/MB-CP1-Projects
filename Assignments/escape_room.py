# Ren Brown, 1, Escape Room

print("     During the school day, you accidentally lock yourself in the bathroom stall. You are not saved. The day passes by slowly with you eating your lunch in that stall. You get bored and use your phone before putting it away, still trying to call for help with no one answering, as if they cannot hear you. You slowly become terrified that you'll be stuck in the stall all night.")

print("     Around midnight, when you have fallen asleep, the stall door unlocks. You jerk awake and at the sound of a lock unlocking before realizing it's just the stall lock that has unlocked. You burst out of the bathroom, only to find that you are in a different place entirely. Scared, you try to turn around and go back into the bathroom, to the stall that started all this, but it has dissapeared in a flash, leaving you momentarily blind. When your eyes finally refocus, you realize you are in a dark room. As you look around, you notice some scattered objects and blood smeared on the wall. A red lantern flares to life, the blood red light casting an eerie glow around the room. ")

print("      Cautiously, you pick the lantern up and turn around the room slowly, noting every item that could help you escape. There are eight items. Each item is scattered around the room. The items include: a lever, an elevator, a knife, a flashlight, a master key card, a lunch box, a journal, and a sticky note.")

while True:
    while True:
        try:
            unstable = input("Which of the items will you use? ").strip().lower()
            if unstable == "lever":
                print("You pull the lever. An enormous shadow monster drops from the ceiling. You scream, terrified of it. The shadow makes a sound alomost like a childrens giggle and swallows you up.")
                print("Game over. Try again.")
                continue
            break
        except:
            print("A growl comes from somewhere distant but quickly approaching. You spin around. Time is running out and you need to choose a clue to escape.")
    if unstable == "elevator":
        print("You turn toward the elevator, pressing the button to open the doors. You step inside and the door closes. A drop of something wet drips onto your shoulder. You look at the drop, examining it before looking up. The elevator was a fake. It's a mimic. You don't make a singl sound as the mimic devours you, leaving only bones as a warning for the next person who dares enter.")
    elif unstable == "knife":
        print(:)