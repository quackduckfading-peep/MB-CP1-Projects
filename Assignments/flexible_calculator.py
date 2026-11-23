# Ren Brown, 1, Flexible Calculator

import random

action = input("Sum, average, maximum, minimum, or product. Which of these would you like to do? ").strip().lower()

if action == "sum":
    x = random.randint(1, 20)
    print(f"Your first number is {x}.")
    y = random.randint(1, 20)
    print(f"Your second number is {y}.")
    answer = x + y
    print(f"The sum of those numbers is {answer}.")
elif action == "average":
    a = random.randint(1, 20)
    print(f"The first number is {a}.")
    b = random.randint(1, 20)
    print(f"The second number is {b}.")
    c = random.randint(1, 20)
    print(f"The third number is {c}.")
    d = random.randint(1, 20)
    print(f"The fourth number is {d}.")
    step_1 = a + b + c + d
    print(f"We added those together and got {step_1}.")
    step_2 = step_1/4
    print(f"We now get the average of {step_2}.")
elif action == "maximum":
    e = random.randint(1, 20)
    print(f"The first number is {e}.")
    f = random.randint(1, 20)
    print(f"The second number is {f}.")
    g = random.randint(1, 20)
    print(f"The third number is {g}.")
    h = random. randint(1, 20)
    print(f"The fourth number is {h}.")
    i = random.randint(1, 20)
    print(f"The fifth nmber is {i}.")
    maximum = max(e, f, g, h, i)
    print(f"The maximum is {maximum}")
elif action == "minimum":
    j = random.randint(1, 20)
    print(f"The first number is {j}.")
    k = random.randint(1, 20)
    print(f"The second number is {k}.")
    l = random.randint(1, 20)
    print(f"The third number is {l}.")
    m = random. randint(1, 20)
    print(f"The fourth number is {m}.")
    n = random.randint(1, 20)
    print(f"The fifth nmber is {n}.")
    o = random.randint(1, 20)
    print(f"The sixth number is {o}.")
    minimum = min(j, k, l, m, n, o)
    print(f"The mimumum is {minimum}.")
elif action == "product":
    p = random.randint(1, 20)
    print(f"The first number is {p}.")
    q = random.randint(1, 20)
    print(f"The second number is {q}")
    first = input(f"Would you like the first number divided to be the first number? Yes or No? ").strip().lower()
    if first == "yes":
        product = p/q
        print(f"The product is {product}.")
    elif first == "no":
        product = q/p
        print(f"The product is {product}.")
else:
    print("Wrong answer. Try again.")