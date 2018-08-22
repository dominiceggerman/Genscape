# By Dominic Eggerman
# https://www.w3schools.com/python/default.asp

if __name__ == "__main__":

    items = ["pencil", "pen", "paper"]
    to_buy = ["printer", "ink"]

    # Showing loop and append
    for item in to_buy:
        print(item)
        items.append(item)
    print(items)
    
    # Showing break (also continue)
    # for i in items:
    #     if i is "paper":
    #         break
    #     print(i)

    # Showing range()
    # for x in range(6):
    #     print(x)
    # for x in range(3, 30, 3):
    #     print(x)

    # Rapidly populate a list (timeit)
    y = []
    for i in range(100):
        y.append(i)
    # y = [i for i in range(100)]
    print(y)