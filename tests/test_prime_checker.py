import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers"""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for prime in prime_numbers:
        assert is_prime(prime) == True, f"{prime} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers"""
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22]
    for non_prime in non_prime_numbers:
        assert is_prime(non_prime) == False, f"{non_prime} should not be prime"

def test_large_prime():
    """Test a large prime number"""
    assert is_prime(104729) == True, "Large prime number not recognized"

def test_large_non_prime():
    """Test a large non-prime number"""
    assert is_prime(100000) == False, "Large non-prime number not detected"

def test_negative_numbers():
    """Test negative numbers"""
    assert is_prime(-7) == False, "Negative numbers should not be prime"

def test_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        is_prime("not a number")
    
    with pytest.raises(TypeError):
        is_prime(3.14)
    
    with pytest.raises(TypeError):
        is_prime(None)