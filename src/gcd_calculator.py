from typing import List
from src.prime_factorization import prime_factorization

def gcd_prime_factors(*numbers: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        *numbers (int): Variable number of integers to find GCD for.
    
    Returns:
        int: The Greatest Common Divisor of the input numbers.
    
    Raises:
        ValueError: If no arguments are provided.
        TypeError: If any argument is not an integer.
    """
    # Handle edge cases
    if len(numbers) == 0:
        raise ValueError("At least one number must be provided")
    
    # Validate inputs
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All arguments must be integers")
    
    # Handle special cases
    if len(numbers) == 1:
        return abs(numbers[0])
    
    # Calculate prime factorizations for each number
    factorizations = [prime_factorization(abs(num)) for num in numbers]
    
    # Find the common prime factors
    gcd_factors = []
    
    # Use the factorization of the first number as a reference
    for prime in set(factorizations[0]):
        # Find the minimum count of this prime factor across all numbers
        min_count = min(
            fact.count(prime) for fact in factorizations
        )
        
        # Add the prime factor the minimum number of times
        gcd_factors.extend([prime] * min_count)
    
    # Calculate GCD by multiplying common prime factors
    return multiply_factors(gcd_factors)

def multiply_factors(factors: List[int]) -> int:
    """
    Multiply all factors together.
    
    Args:
        factors (List[int]): List of prime factors.
    
    Returns:
        int: Product of all factors.
    """
    if not factors:
        return 1
    
    result = 1
    for factor in factors:
        result *= factor
    
    return result