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

print(primeFactors(256))