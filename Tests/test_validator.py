from validator import is_valid_address
def test_valid_address():
    assert is_valid_address("Av. Siempre Viva 742") == True
def test_missing_number():
    assert is_valid_address("Av. Siempre Viva") == False
def test_empty_string():
    assert is_valid_address("") == False
def test_not_a_string():
    assert is_valid_address(12345) == False