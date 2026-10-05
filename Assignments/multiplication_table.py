# Ren Brown, 1, Multiplication Table

dings = 1
a = 1
b = 13

for i in range(a, b, a):
    for x in range(a, b, a):
        pop = int(i * x)
        print(pop, end = " ")