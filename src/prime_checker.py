def is_prime(n: int) -> bool:
    """
    Check if a given number is prime.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        ValueError: If the input is less than 2.
    """
    # Handle edge cases
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        return False
    
    # Check for divisibility up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True