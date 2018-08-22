# By Dominic Eggerman

# Demo to show conditional statements

# Evaluation function
def evaluate(var):
    if var <= 4:
        print("var is <= 4")
    elif var >= 8:
        print("var is >= 8")
    else:
        print("var is 5, 6, or 7")

def trueFalse():
    return True

# Run
if __name__ == "__main__":
    # Assign x, y, z
    x = 4
    y = 6
    z = y + x
    # x, y, z = 4, 6, 2

    evaluate(x)  # Pass x as an arguement to the evaluate() function
    evaluate(y)
    evaluate(z)

    a = trueFalse()
    if a:
        print("a is True")