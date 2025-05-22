from typing import List
from src.prime_checker import is_prime

def prime_factorization(n: int) -> List[int]:
    """
    Compute the prime factorization of a given number.
    
    Args:
        n (int): The number to factorize.
    
    Returns:
        List[int]: A list of prime factors.
    
    Raises:
        ValueError: If the input is less than 2.
        TypeError: If the input is not an integer.
    """
    # Handle edge cases
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        return []
    
    # List to store prime factors
    factors = []
    
    # Handle 2 as a special case
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check odd factors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0 and is_prime(i):
            factors.append(i)
            n //= i
    
    # If the remaining number is a prime greater than 2
    if n > 2:
        factors.append(n)
    
    return factors