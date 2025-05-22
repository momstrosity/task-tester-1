from typing import List, Union
from math import sqrt

def get_prime_factors(n: int) -> List[int]:
    """
    Decompose a number into its prime factors.
    
    Args:
        n (int): The number to factorize (must be a positive integer)
    
    Returns:
        List[int]: A list of prime factors
    
    Raises:
        ValueError: If input is less than 1
    """
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Handle special cases
    if n == 1:
        return [1]
    
    factors = []
    
    # Check for 2 as a factor
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd prime factors
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is a prime greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

def gcd_prime_factors(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        a (int): First number 
        b (int): Second number
    
    Returns:
        int: The Greatest Common Divisor
    
    Raises:
        ValueError: If either input is less than 1
    """
    # Handle zero cases
    if a == 0 and b == 0:
        return 0
    
    # Take absolute values to handle negative inputs
    a, b = abs(a), abs(b)
    
    # If either number is 0, return the other number
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Get prime factors for both numbers
    a_factors = get_prime_factors(a)
    b_factors = get_prime_factors(b)
    
    # Calculate GCD by multiplying common prime factors
    gcd = 1
    a_factor_counts = {}
    b_factor_counts = {}
    
    # Count occurrences of factors
    for factor in a_factors:
        a_factor_counts[factor] = a_factor_counts.get(factor, 0) + 1
    for factor in b_factors:
        b_factor_counts[factor] = b_factor_counts.get(factor, 0) + 1
    
    # Find common factors with minimum count
    for factor, count in a_factor_counts.items():
        if factor in b_factor_counts:
            common_count = min(count, b_factor_counts[factor])
            gcd *= factor ** common_count
    
    return gcd