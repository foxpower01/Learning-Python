import math

def primeFactors(number):
    factor = 2
    number = abs(number)
    numberSave = number
    primeFactors = []
    while factor * factor <= number:
        if number % factor:
            factor += 1
        else:
            number //= factor
            primeFactors.append(factor)
    if number > 1:
        primeFactors.append(number)
    primeFactors.append(1)
    primeFactors.append(numberSave)
    print(primeFactors)
    return(primeFactors)

#def factors(number):
#    factor = 1
#    factors =[]
#    while factor * factor <= number:
#        if number % factor == 0:
#            factors.append(factor)
#            factor += 1
#        else:
#            factor += 1

def possibleFactors(primes):
    factors = []
    for i in range(len(primes)):
        for j in range(len(primes)):
            if i != j:
                if factors.count(primes[i] * primes[j]) == 0 and primes[i] * primes[j] <= primes[-1]:
                    factors.append(primes[i] * primes[j])
                    factors.append(primes[i] * primes[j] * -1)
#    for i in primes:
#        for j in primes:
#            if i * j <= number:
#                if i != j or primes.count(i) > 1:
#                    if factors.count(i * j) == 0:
#                        factors.append(i * j)
#                        factors.append(-1 * i * j)
    factors.append(1)
    factors.append(-1)
    print(factors)
    return(factors)

def syntheticDivision(terms, factor):
    tempCos = []
    temp = 0
    for i in range(len(terms)):
        tempCos.append(0)
    for i in range(len(terms)):
        tempCos[i] = terms[i] + temp
        temp = tempCos[i] * (factor)
    return(tempCos)

def findFactor(terms):
    listOfFactors = []
    listOfPosFactors = []
    if terms[-1] == 0:
        listOfFactors.append(0)
        if solveQuadratic(terms) != "complex roots":
            for factor in solveQuadratic(terms):
                listOfFactors.append(factor)
        else:
            listOfFactors.append("complex roots")
        return(listOfFactors)
    else:
        leadingCoFactors = possibleFactors(primeFactors(terms[0]))
        constantFactors = possibleFactors(primeFactors(terms[-1]))
        for fac in constantFactors:
            for tor in leadingCoFactors:
                if listOfPosFactors.count(fac / tor) == 0:
                    listOfPosFactors.append(fac / tor)
                    print(fac/tor)
                tempCos = syntheticDivision(terms, fac / tor)
                print("remainder ", tempCos[-1])
                if (tempCos[-1] > -0.01 and tempCos[-1] < 0.01) and listOfFactors.count(fac / tor) == 0:
                    listOfFactors.append(fac / tor)
                    nextCos = tempCos
        if len(listOfFactors) > 2:
            return([listOfFactors, nextCos])
        else: 
            for factor in listOfPosFactors:
                if factor > 0:
                    tempCos = syntheticDivision(terms, math.sqrt(factor))
                    print("sqrt ", factor)
                    print(tempCos[-1])
                    if tempCos[-1] > -0.01 and tempCos[-1] < 0.01:
                        listOfFactors.append("+-sqrt(" + str(factor) + ")")
                        nextCos = tempCos
        if len(listOfFactors) > 2:
            return([listOfFactors, nextCos])

def solveQuadratic(terms):
    a = terms[0]
    b = terms[1]
    c = terms[2]
    roots = []
    print(a, b, c)
    if b ** 2 - 4 * a * c >= 0:
        for i in range(2):
            root = ((0 - b) + ((-1) ** i) * math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
            print(root)
            print((-1) ** i)
            if roots.count(root) == 0:
                roots.append(root)
        return(roots)
    else:
        return("complex roots")
    
equation = input("input a cubic in the form 'ax+bx+cx+d', with the terms in order of decending powers. Include all terms with a 0 coefficient, and include 1 coefficients (no naked x's). Don't input powers.\n")
terms = list(map(lambda x: int(x), equation.split("x")))

print(terms)
results = findFactor(terms)
print(results)
#print(solveQuadratic(terms))