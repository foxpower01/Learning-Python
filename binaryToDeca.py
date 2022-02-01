places = []
output = 0
isNegative = False
input = input("Binary number, first bit determines sign:\n")
input = list(input)
for item in input[::-1]:
    places.append(item)
if places[-1] == 0:
    isNegative = True
places.pop()
print(list(places))
for i in range(len(list(places))):
    output += 2 ** i * int(list(places)[i])
if isNegative:
    output = -1 * output
print(output)