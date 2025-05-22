import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for prime in primes:
        assert is_prime(prime), f"{prime} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers."""
    non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
    for non_prime in non_primes:
        assert not is_prime(non_prime), f"{non_prime} should not be prime"

def test_large_prime():
    """Test a large prime number."""
    assert is_prime(104729), "104729 is a prime number"

def test_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        is_prime(3.14)
    with pytest.raises(TypeError):
        is_prime("not a number")