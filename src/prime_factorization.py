def prime_factorization(n):
    """
    Compute the prime factorization of a given integer.
    
    Args:
        n (int): The number to factorize.
    
    Returns:
        list: A list of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Handle edge cases
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n < 2:
        return []
    
    # Initialize factors list
    factors = []
    
    # Handle 2 as a special case to optimize odd number factorization
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check odd factors up to square root of n
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