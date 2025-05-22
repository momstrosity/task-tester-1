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
    # Check for valid input type (must be an integer)
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle special cases
    if n <= 1:
        return False
    
    # 2 is the smallest prime number
    if n == 2:
        return True
    
    # Even numbers greater than 2 are not prime
    if n % 2 == 0:
        return False
    
    # Check for divisibility up to the square root of n
    # This is more efficient than checking all numbers up to n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True