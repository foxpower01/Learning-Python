places = []
deciPlaces = []
output = 0
decimal = 0
isDecimal = False
isNegative = False
input = input("Binary number, first bit determines sign, use a '.' to indicate decimals:\n")
input = list(input)
for item in input[::-1]:
    if item == ".":
        isDecimal = True
    else:
        places.append(item)
for d in range(len(input)):
    if input.index(".") < d:
        deciPlaces.append(input[d])
        places.remove(input[d])
if places[-1] == "0":
    isNegative = True
places.pop()
print(list(places))
for i in range(len(list(places))):
    output += 2 ** i * int(list(places)[i])
for j in range(len(deciPlaces)):
    decimal += 2 ** -(j + 1) * int(deciPlaces[j])
if isNegative:
    output = -1 * output
    decimal = -1 * decimal
print(output + decimal)
print(deciPlaces)

def decimalToBase(number, base):
    numPlaces = []
    output = 0
    for item in list(number)[::-1]:
        numPlaces.append(item)
    for i in range(len(numPlaces)):
        output += base ** i * numPlaces[i]