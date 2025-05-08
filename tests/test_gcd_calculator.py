import pytest
from src.gcd_calculator import get_prime_factors, gcd_prime_factors

def test_get_prime_factors():
    # Test basic prime factorization
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(100) == [2, 2, 5, 5]
    assert get_prime_factors(7) == [7]
    assert get_prime_factors(1) == []
    
    # Test zero and negative numbers
    assert get_prime_factors(0) == []
    assert get_prime_factors(-12) == [2, 2, 3]

def test_gcd_prime_factors():
    # Test basic GCD calculations
    assert gcd_prime_factors(48, 18) == 6
    assert gcd_prime_factors(54, 24) == 6
    assert gcd_prime_factors(17, 23) == 1
    assert gcd_prime_factors(100, 75) == 25
    
    # Test with zero
    assert gcd_prime_factors(0, 5) == 5
    assert gcd_prime_factors(5, 0) == 5
    
    # Test with negative numbers
    assert gcd_prime_factors(-48, 18) == 6
    assert gcd_prime_factors(48, -18) == 6
    assert gcd_prime_factors(-48, -18) == 6

def test_gcd_error_handling():
    # Test invalid inputs
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_prime_factors(3.14, 5)
    
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_prime_factors("10", 5)
    
    with pytest.raises(ValueError, match="GCD is undefined when both numbers are zero"):
        gcd_prime_factors(0, 0)

def test_get_prime_factors_error_handling():
    # Test invalid inputs
    with pytest.raises(ValueError, match="Input must be an integer"):
        get_prime_factors(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        get_prime_factors("10")