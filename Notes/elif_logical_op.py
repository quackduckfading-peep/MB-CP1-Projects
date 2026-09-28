# RB, 1, Elif and Logical Operators Notes

age = 17
license = False

if age >= 18:
    print("You are an adult and can vote.")
elif age >= 15 and license:
    print("You can drive! But you still have no rights. Go to school!")
elif age >= 15 and not license:
    print("You could drive... but you haven't done the paperwork. You still have not rights so go to school.")
else:
    print("You are a minor with no rights but you can drive.")


win = True
hp = 0

if win or hp < 1:
    print("Game Over")
    if hp > 0:
        pass
    else:
        print("You lost :(")
else:
    print("The game is still going")