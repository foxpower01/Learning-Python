def primeFactors(number):
    factor = 2
    primeFactors = []
    while factor * factor <= number:
        if number % factor:
            factor += 1
        else:
            number //= factor
            primeFactors.append(factor)
    if number > 1:
        primeFactors.append(number)
    return(primeFactors)

def permsOfList(list):
    perms = []
    for i in list:
        for j in list:
            if i * j in perms == False:
                perms.append(i * j)

def findFactor(terms):
    leadingCoFactors = primeFactors(terms[0])
    constantFactors = primeFactors(terms[-1])
    

equation = input("input a cubic in the form 'ax+bx+cx+d', with the terms in order of decending powers. Include all terms with a 0 coefficient, and include 1 coefficients (no naked x's). Don't input powers.\n")
terms = list(map(lambda x: int(x), equation.split("x")))

print(terms)
print(int(terms[1]))