from PrimeNumber import is_prime

# to check the ngative
def test_can_handle_ngtv_values():
    assert is_prime(-3)== False
    
# to check the value with other datatypes 
def test_can_handle_other_data_types():
    assert is_prime(0.3)==False