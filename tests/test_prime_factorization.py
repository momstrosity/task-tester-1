import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test prime factorization for basic numbers."""
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_numbers():
    """Test prime factorization for prime numbers."""
    assert prime_factorization(7) == [7]
    assert prime_factorization(17) == [17]

def test_prime_factorization_edge_cases():
    """Test edge cases for prime factorization."""
    assert prime_factorization(1) == []
    assert prime_factorization(0) == []

def test_prime_factorization_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        prime_factorization(3.14)
    with pytest.raises(TypeError):
        prime_factorization("not a number")