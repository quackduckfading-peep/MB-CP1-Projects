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
    if unstable == "lunch box":
        print("You grab the lunchbox, the lantern glowing red as you open the lid slowly. Inside is a small rock the size of a small potato. The rock is as black as the night sky with speckled stars across and a swirl of colors in random places, as if the galaxy were in your hand. It subtly glows a soft white. You stare at it. A wish stone. You carefully pick it up, wishing to go home.")
        print("You jolt awake in your bed, panting. It worked. You look around your room. You're home now. Safe.")
        print("Good job. You escaped. But shadows always return...")
        break
    elif unstable == "elevator":
        print("You turn toward the elevator, pressing the button to open the doors. You step inside and the door closes. A drop of something wet drips onto your shoulder. You look at the drop, examining it before looking up. The elevator was a fake. It's a mimic. You don't make a singl sound as the mimic devours you, leaving only bones as a warning for the next person who dares enter.")
        print("You died. Game over. Try again.")
    elif unstable == "knife":
        print("You use the red light to pick up the knife. A scream echoes from it. You drop it as the knife glitches. A silouette the size of a human emerges, glitching with every growl it makes. You turn around, ready to run, but the silouette glitches in front of you, reaching out and glitching you to an endless void with no exit, floating forever.")
        print("Game over. Try again.")