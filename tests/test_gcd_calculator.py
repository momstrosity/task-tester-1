import pytest
from src.gcd_calculator import gcd_prime_factors, get_prime_factors

def test_get_prime_factors():
    # Test basic prime factorization
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(7) == [7]
    assert get_prime_factors(1) == [1]

def test_prime_factors_edge_cases():
    # Test edge cases
    with pytest.raises(ValueError):
        get_prime_factors(0)
    with pytest.raises(ValueError):
        get_prime_factors(-5)

def test_gcd_prime_factors():
    # Test various GCD scenarios
    assert gcd_prime_factors(48, 18) == 6
    assert gcd_prime_factors(54, 24) == 6
    assert gcd_prime_factors(17, 23) == 1  # Coprime numbers
    assert gcd_prime_factors(0, 5) == 5
    assert gcd_prime_factors(5, 0) == 5
    assert gcd_prime_factors(0, 0) == 0

def test_gcd_with_negative_numbers():
    # Test GCD with negative numbers
    assert gcd_prime_factors(-48, 18) == 6
    assert gcd_prime_factors(48, -18) == 6
    assert gcd_prime_factors(-48, -18) == 6

def test_gcd_large_numbers():
    # Test large numbers
    assert gcd_prime_factors(1234567, 7654321) == 1  # Coprime large numbers
    assert gcd_prime_factors(1000000, 10000) == 10000