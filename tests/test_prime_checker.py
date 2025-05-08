import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers."""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for num in prime_numbers:
        assert is_prime(num) is True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers."""
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22]
    for num in non_prime_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_large_prime():
    """Test a large prime number."""
    assert is_prime(104729) is True, "104729 is a large prime number"

def test_large_non_prime():
    """Test a large non-prime number."""
    assert is_prime(100000) is False, "100000 should not be prime"

def test_negative_numbers():
    """Test negative numbers."""
    negative_numbers = [-1, -2, -3, -5, -7]
    for num in negative_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_prime(3.14)
    
    with pytest.raises(TypeError):
        is_prime("17")
    
    with pytest.raises(TypeError):
        is_prime(None)