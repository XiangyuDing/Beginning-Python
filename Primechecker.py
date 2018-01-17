# n = int(input("n = "))
for n in range(-10, 10):
    if n < 2:
        print("{:d} is not prime!".format(n))

    else:
        divisors = []
        for divisor in range(2, n):
            if n % divisor == 0:
                divisors.append(divisor)

        if len(divisors) == 0:
            print("{:d} is  prime!".format(n))
        else:
            print("{:d} is not prime because {:} divide {:d}".format(n, str(divisors), n))