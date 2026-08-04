def generate_primes(n):
    if n < 2:
        return ""
    
    primes = []
    for num in range(2, n + 1):
        # Check if num is prime
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
            
    return ", ".join(primes)

print(generate_primes(10))
print(generate_primes(20))
print(generate_primes(1))
print(generate_primes(2))