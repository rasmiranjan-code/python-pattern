height = int(input("Enter the height of the triangle: "))
base = int(input("Enter the base of the triangle: "))

for i in range(1, height + 1):
    stars = (i * base) // height   # Proportion ke hisab se stars

    for j in range(stars):
        print("*", end="")

    print()