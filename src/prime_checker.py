def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Check for valid input type (must be integer)
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle non-positive numbers
    if n <= 1:
        return False
    
    # Check for divisibility up to the square root of n
    # This is an optimization to reduce computational complexity
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True