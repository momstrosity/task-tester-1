from typing import List

def prime_factorization(n: int) -> List[int]:
    """
    Compute the prime factorization of a given positive integer.
    
    Args:
        n (int): The positive integer to factorize.
    
    Returns:
        List[int]: A list of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is less than 1.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Handle special cases
    if n == 1:
        return []
    
    # Prime factorization algorithm
    factors = []
    
    # First, handle 2 as a special case to optimize odd number checking
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd prime factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors