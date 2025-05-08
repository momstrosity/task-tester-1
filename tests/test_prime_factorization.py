import pytest
from src.prime_factorization import prime_factorization, is_prime

def test_is_prime():
    """Test prime number checking function."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(4) == False
    assert is_prime(15) == False
    assert is_prime(1) == False
    assert is_prime(0) == False

def test_prime_number_factorization():
    """Test factorization of prime numbers."""
    assert prime_factorization(7) == {7: 1}
    assert prime_factorization(11) == {11: 1}
    assert prime_factorization(13) == {13: 1}

def test_composite_number_factorization():
    """Test factorization of composite numbers."""
    assert prime_factorization(24) == {2: 3, 3: 1}
    assert prime_factorization(100) == {2: 2, 5: 2}
    assert prime_factorization(84) == {2: 2, 3: 1, 7: 1}

def test_edge_cases():
    """Test edge cases like 0, 1, and small numbers."""
    assert prime_factorization(0) == {}
    assert prime_factorization(1) == {}
    assert prime_factorization(2) == {2: 1}

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
    
    # Verify the result contains only prime keys
    assert all(is_prime(key) for key in result.keys())
    
    # Verify the product of prime factors equals the original number
    product = 1
    for prime, freq in result.items():
        product *= (prime ** freq)
    assert product == 123456
    
    # Verify the number of prime factors
    total_factors = sum(result.values())
    assert total_factors > 0