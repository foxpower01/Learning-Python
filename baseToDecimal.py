from pickle import TRUE


def baseToDecimal(number, base):

    numPlaces = []
    output = 0
    for item in list(number)[::-1]:
        numPlaces.append(item)
    for i in range(len(numPlaces)):
        output += int(base) ** i * int(numPlaces[i])
    return(output)

def main():

    number = input("give a positive integer in any base: ")
    if number == "stop":
        exit()
    base = input("what base is " + number + " in? ")
    print(baseToDecimal(number, base))

if __name__ == "__main__":
    while TRUE:
        main()