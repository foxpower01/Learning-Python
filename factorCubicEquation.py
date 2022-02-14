import numbers


def primeFactors(number):
    factor = 2
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

def findFactor(terms):
    leadingCoFactors = possibleFactors(primeFactors(terms[0]))
    constantFactors = possibleFactors(primeFactors(terms[-1]))
    for fac in constantFactors:
        for tor in leadingCoFactors:
            print(fac / tor)
            print(terms[0] * ((fac / tor) ** 3) + terms[1] * ((fac / tor) ** 2) + terms[2] * ((fac / tor)) + terms[3])
            if terms[0] * ((fac / tor) ** 3) + terms[1] * ((fac / tor) ** 2) + terms[2] * ((fac / tor)) + terms[3] == 0:
                return(fac / tor)
    
equation = input("input a cubic in the form 'ax+bx+cx+d', with the terms in order of decending powers. Include all terms with a 0 coefficient, and include 1 coefficients (no naked x's). Don't input powers.\n")
terms = list(map(lambda x: int(x), equation.split("x")))

print(terms)
print(int(terms[1]))
print(findFactor(terms))
print(terms[0] * ((-0.75561) ** 3) + terms[1] * ((-0.75561) ** 2) + terms[2] * ((-0.75561)) + terms[3])