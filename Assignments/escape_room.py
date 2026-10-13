# Ren Brown, 1, Escape Room

print("     During the school day, you accidentally lock yourself in the bathroom stall. You are not saved. The day passes by slowly with you eating your lunch in that stall. You get bored and use your phone before putting it away, still trying to call for help with no one answering, as if they cannot hear you. You slowly become terrified that you'll be stuck in the stall all night.")

print("     Around midnight, when you have fallen asleep, the stall door unlocks. You jerk awake and at the sound of a lock unlocking before realizing it's just the stall lock that has unlocked. You burst out of the bathroom, only to find that you are in a different place entirely. Scared, you try to turn around and go back into the bathroom, to the stall that started all this, but it has dissapeared in a flash, leaving you momentarily blind. When your eyes finally refocus, you realize you are in a dark room. As you look around, you notice some scattered objects and blood smeared on the wall. It's too dark to make out what they are just yet. A red lantern flares to life, the blood red light casting an eerie weak glow around the room.")

print("      Cautiously, you pick the lantern up and turn around the room slowly, turning around able to make out the objects but with the room still dark despite the lanterns bloody glow. You carefully note every item that could help you escape. There are eight items. Each item is scattered around the room. The items include: a lever, an elevator, a key card, a knife, a journal, a flashlight a sticky note, and a lunch box.")

while True:
    while True:
        try:
            unstable = input("Which of the items will you use? ").strip().lower()
            if unstable == "lever":
                print("You pull the lever. An enormous shadow monster drops from the ceiling. You scream, terrified of it. The shadow makes a sound alomost like a childs giggle and swallows you up.")
                print("You died. Game over. Try again.")
                continue
            break
        except:
            print("A growl comes from somewhere distant but quickly approaching. You spin around. Time is running out and you need to choose a clue to escape.")
    if unstable == "lunch box":
        print("You grab the lunchbox, the lantern glowing red as you open the lid slowly. Inside is a small rock the size of a small potato. The rock is as black as the night sky with speckled stars across and a swirl of colors in random places, as if the galaxy were in your hand. It subtly glows a soft white. You stare at it. A wish stone. You carefully pick it up, wishing to go home.")
        print("You jolt awake in your bed, panting. It worked. You look around your room. You're home now. Safe.")
        print("You escaped! Good job!")
        break

    elif unstable == "elevator":
        print("You turn toward the elevator, pressing the button to open the doors. You step inside and the door closes. A drop of something wet drips onto your shoulder. You look at the drop, examining it before looking up. The elevator was a fake. It's a mimic. The mimic devours you, leaving only bones as a warning for the next person who dares enter.")
        print("You died. Game over. Try again.")

    elif unstable == "knife":
        print("You use the red light to pick up the knife. A scream echoes from it. You drop it as the knife glitches. A silouette the size of a human emerges, glitching with every growl it makes. You turn around, ready to run, but the silouette glitches in front of you, reaching out to harm you in a void. You back away and the silouette glitches to nothing, gone. You glance around the room, trying to place which item will help you get out quickly before something else appears. Your eyes land on the journal.")

    elif unstable == "flashlight":
        print("You put the lantern, which was already emitting a glow, down and pick the flashlight up. You try to turn it on but the batteries are dead. Frustrated, you throw it against the walll, having it shatter upon impact. You sit down against the wall, losing hope for escaping. You move on to the next object that might emmit a light to help you.")

    elif unstable == "key card":
        print("You pick the key card up, turning it around in your hands. You use the lantern to light up the name on the key card. 'Charles Lamon'. You wonder who Charles Lamon is for about a minute before realizing you still need to escape. You try to slash the key card against the panel of the wall in the room. The panel flashes yellow and says 'Card Access Revoked'. You groan, frustrated at the failure. You turn back to the other objects, eyeing the knife. It could be good for self defense.")
        
    elif unstable == "journal":
        print("You pick the journal up, reading it. It holds no useful information to get out only a picture of a wish stone with a warning that says 'Find it and get out before it comes.' You glance around the room, looking or anything remotely capable of light or seeping light in any way.")
    elif unstable == "sticky note":
        print("Your eyes land on the sticky note. You pick it up, examining the clue on it. I has a picture of food on it. In the distance, a roar echoes. It is approaching. You try to think of the one thing in the room that might have a relation to food.")
    else:
        print("Sadly you entered an invalid word, number, or symbol and cannot continue. Please exit now or retry.")