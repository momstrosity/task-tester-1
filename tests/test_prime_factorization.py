import pytest
from src.prime_factorization import prime_factorization

def test_prime_number_factorization():
    """Test factorization of prime numbers."""
    assert prime_factorization(7) == [7]
    assert prime_factorization(11) == [11]
    assert prime_factorization(13) == [13]

def test_composite_number_factorization():
    """Test factorization of composite numbers."""
    assert prime_factorization(24) == [2, 2, 2, 3]
    assert prime_factorization(100) == [2, 2, 5, 5]
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_edge_cases():
    """Test edge cases like 0, 1, and small numbers."""
    assert prime_factorization(0) == []
    assert prime_factorization(1) == []
    assert prime_factorization(2) == [2]

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        prime_factorization(-5)
    
    with pytest.raises(ValueError):
        prime_factorization(3.14)
    
    with pytest.raises(ValueError):
        prime_factorization("not a number")

def test_large_number():
    """Test factorization of a relatively large number."""
    result = prime_factorization(123456)
    assert result == [2, 2, 2, 2, 2, 2, 643, 3]
    assert all(is_prime(x) for x in result)

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True