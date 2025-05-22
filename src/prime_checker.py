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
    # Check input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle known non-prime cases
    if n <= 1:
        return False
    
    # Special case for 2 (the only even prime number)
    if n == 2:
        return True
    
    # Eliminate even numbers greater than 2
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to the square root of n
    # This is an optimization to reduce unnecessary iterations
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True