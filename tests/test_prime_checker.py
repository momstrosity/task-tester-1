import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test numbers that are known to be prime."""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for num in prime_numbers:
        assert is_prime(num) is True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test numbers that are known to be non-prime."""
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
    for num in non_prime_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_large_prime_number():
    """Test a large prime number."""
    assert is_prime(104729) is True, "Large prime number not correctly identified"

def test_large_non_prime_number():
    """Test a large non-prime number."""
    assert is_prime(104730) is False, "Large non-prime number not correctly identified"

def test_negative_numbers():
    """Test that negative numbers are not considered prime."""
    negative_numbers = [-1, -2, -3, -5, -7]
    for num in negative_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_invalid_input_type():
    """Test that non-integer inputs raise a TypeError."""
    invalid_inputs = [3.14, "7", [7], None]
    for invalid_input in invalid_inputs:
        with pytest.raises(TypeError):
            is_prime(invalid_input)