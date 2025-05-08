def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factorization(n):
    """
    Compute the prime factorization of a given integer.
    
    Args:
        n (int): The number to factorize.
    
    Returns:
        dict: A dictionary of prime factors and their frequencies.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Handle edge cases
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n < 2:
        return {}
    
    # Initialize factors dictionary
    factors = {}
    
    # Validate primality of initial value
    if not is_prime(n) or n == 1:
        # Handle 2 as a special case to optimize odd number factorization
        while n % 2 == 0:
            factors[2] = factors.get(2, 0) + 1
            n //= 2
        
        # Check odd factors up to square root of n
        factor = 3
        while factor * factor <= n:
            # Validate primality of factor
            if is_prime(factor):
                while n % factor == 0:
                    factors[factor] = factors.get(factor, 0) + 1
                    n //= factor
            factor += 2
        
        # If n is a prime number greater than 2
        if n > 2 and is_prime(n):
            factors[n] = factors.get(n, 0) + 1
    else:
        # n itself is prime
        factors[n] = 1
    
    return factors