import math

def is_prime(n):
    """
    Check if a given number is prime.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Check for valid input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle special cases
    if n <= 1:
        return False
    
    # Optimization for 2 and 3
    if n <= 3:
        return n > 1
    
    # Even numbers greater than 2 are not prime
    if n % 2 == 0:
        return False
    
    # Check up to the square root of n
    sqrt_n = int(math.sqrt(n)) + 1
    
    # Check for divisibility by odd numbers
    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False
    
    # If no divisors are found, the number is prime
    return True