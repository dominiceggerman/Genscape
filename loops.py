# By Dominic Eggerman
# https://www.w3schools.com/python/default.asp
import time

def loopingExample():
    items = ["pencil", "pen", "paper"]
    to_buy = ["printer", "ink"]

    # Showing loop and append
    for item in to_buy:
        print(items)
        items.append(item)
    
    # Showing break / continue (next loop iteration) / pass (does nothing)
    # for i in items:
    #     if i is "pen":
    #         continue
    #     else:
    #         print(i)

    return items
    

def rangesExample():
    # Showing range()
    for x in range(6):
        print(x)
    for x in range(3, 30, 3):
        print(x)


def timeThis(x):

    # Slow way
    y = []
    for i in range(x):
        y.append(i)

    # Fast way (generators)
    # y = [i for i in range(x)]

if __name__ == "__main__":

    # Basic looping / appending / returning / break / continue
    # print("Returned: ", loopingExample())

    # Using a range
    # rangesExample()

    # # Time excecution of function
    startT = time.time()
    timeThis(20000)  # 'small' numbers
    # timeThis(20000000)  # large numbers
    print(time.time() - startT)