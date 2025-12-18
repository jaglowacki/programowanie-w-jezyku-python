def is_prime(n: int) -> bool:
    if n < 0:
        raise ValueError('Podany argument musi być >=0')
    prime = n >= 2
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
    return prime
