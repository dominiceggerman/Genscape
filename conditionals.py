# By Dominic Eggerman

# Demo to show conditional statements

# Evaluation function
def evaluate(var):
    print(var)
    if var is 5:
        print("var is 5")
    elif var == 6:
        print("var is 6")
    elif var >= 7:
        print("var is >= 8")
    else:
        print("var is less than 5")
    print("------")

def frank():
    return True

# Run
if __name__ == "__main__":
    # Assign x, y, z
    x = 5
    y = 6
    z = y + x
    # x, y, z = 4, 6, 22

    evaluate(x)  # Pass x as an arguement to the evaluate() function
    evaluate(y)
    evaluate(z)

    a = frank()
    if a:
        print("a is True")