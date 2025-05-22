import pytest
from src.gcd_calculator import gcd_prime_factors

def test_gcd_basic():
    """Test GCD for basic scenarios."""
    assert gcd_prime_factors(12, 18) == 6
    assert gcd_prime_factors(48, 18) == 6
    assert gcd_prime_factors(54, 24) == 6

def test_gcd_coprime():
    """Test GCD for coprime numbers."""
    assert gcd_prime_factors(17, 23) == 1
    assert gcd_prime_factors(5, 7) == 1

def test_gcd_multiple_numbers():
    """Test GCD for multiple numbers."""
    assert gcd_prime_factors(12, 18, 24) == 6
    assert gcd_prime_factors(100, 75, 50) == 25

def test_gcd_zero_and_numbers():
    """Test GCD involving zero."""
    assert gcd_prime_factors(0, 5) == 5
    assert gcd_prime_factors(0, 0) == 0

def test_gcd_negative_numbers():
    """Test GCD with negative numbers."""
    assert gcd_prime_factors(-12, 18) == 6
    assert gcd_prime_factors(-48, -18) == 6

def test_gcd_single_number():
    """Test GCD with a single number."""
    assert gcd_prime_factors(42) == 42

def test_gcd_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        gcd_prime_factors()
    
    with pytest.raises(TypeError):
        gcd_prime_factors(3.14, 5)
    
    with pytest.raises(TypeError):
        gcd_prime_factors("not", "numbers")