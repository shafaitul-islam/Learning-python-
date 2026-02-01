try:
    N = int(input("Enter a number: "))

    if N <= 1:
        print("No prime numbers found.")
    else:
        primes = []

        for num in range(2, N + 1):
            is_prime = True

            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(num)

        if len(primes) == 0:
            print("No prime numbers found.")
        else:
            print(f"Prime numbers up to {N}: ", end="")
            print(", ".join(map(str, primes)))

except ValueError:
    print("Invalid input! Please enter a positive integer.")
