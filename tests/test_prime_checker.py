import pytest
from src.prime_checker import is_prime

def test_is_prime_small_primes():
    """Test small known prime numbers."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True

def test_is_prime_small_composites():
    """Test small known composite numbers."""
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(12) == False

def test_is_prime_larger_numbers():
    """Test larger prime and composite numbers."""
    assert is_prime(17) == True
    assert is_prime(19) == True
    assert is_prime(23) == True
    assert is_prime(29) == True
    
    assert is_prime(15) == False
    assert is_prime(21) == False
    assert is_prime(25) == False
    assert is_prime(27) == False

def test_is_prime_edge_cases():
    """Test edge cases."""
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(-1) == False
    assert is_prime(-2) == False
    assert is_prime(-17) == False

def test_is_prime_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(ValueError):
        is_prime(3.14)
    with pytest.raises(ValueError):
        is_prime("17")
    with pytest.raises(ValueError):
        is_prime(None)