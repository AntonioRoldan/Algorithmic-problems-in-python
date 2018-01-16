
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
    return factorial

def factorial_division(number_pairs):
    n = 0
    m = 0
    for pair in number_pairs:
        n = pair[0]
        m = pair[1]
        if not factorial(n) % m:
            print(str(m) + " divides " + str(n) + "!")
        else:
            print(str(m) + " does not divide " + str(n) + "!")



number_pairs = [(6, 9), (6, 27), (20, 1000), (20, 100000)]

factorial_division(number_pairs)