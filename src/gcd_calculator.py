def get_prime_factors(n):
    """
    Decompose a number into its prime factors.
    
    Args:
        n (int): The number to factorize.
    
    Returns:
        list: A list of prime factors.
    
    Raises:
        ValueError: If input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    # Handle special cases
    if n < 0:
        n = abs(n)
    
    if n <= 1:
        return []
    
    prime_factors = []
    divisor = 2
    
    while divisor * divisor <= n:
        if n % divisor == 0:
            prime_factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    
    # If n is still greater than 1, it's a prime factor itself
    if n > 1:
        prime_factors.append(n)
    
    return prime_factors

def gcd_prime_factors(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        a (int): First number.
        b (int): Second number.
    
    Returns:
        int: The Greatest Common Divisor.
    
    Raises:
        ValueError: If inputs are not integers.
    """
    # Validate inputs
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    
    # Handle special cases
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined when both numbers are zero")
    
    # Handle zero case
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    
    # Get absolute values
    a, b = abs(a), abs(b)
    
    # Get prime factors
    a_factors = get_prime_factors(a)
    b_factors = get_prime_factors(b)
    
    # Find common prime factors
    gcd = 1
    a_factor_count = {}
    b_factor_count = {}
    
    # Count factors in a
    for factor in a_factors:
        a_factor_count[factor] = a_factor_count.get(factor, 0) + 1
    
    # Count factors in b
    for factor in b_factors:
        b_factor_count[factor] = b_factor_count.get(factor, 0) + 1
    
    # Calculate GCD by multiplying common factors
    for factor, count in a_factor_count.items():
        if factor in b_factor_count:
            common_count = min(count, b_factor_count[factor])
            gcd *= factor ** common_count
    
    return gcd