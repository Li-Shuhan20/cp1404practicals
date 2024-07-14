CODE_OF_COLOUR = {"Wine": "#722f37", "White": "#ffffff", "Volt": "#ceff00", "Red Orange": "#ff5349",
                  "Cameo Pink": "#efbbcc", "Buff": "#f0dc82", "Black": "#000000", "Barn Red": "#7c0a02",
                  "Baby Blue": "#89cff0", "Apricot": "#fbceb1", "Absolute Zero": "#0048ba"}

print(CODE_OF_COLOUR)
colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", CODE_OF_COLOUR[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()
