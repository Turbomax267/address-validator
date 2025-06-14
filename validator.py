import re
def is_valid_address(address):
    if not isinstance(address, str):
        return False
    # Simplee check: must contain a street name and number
    pattern = r'^[A-Za-zÁÉÍÓÚÑáéíóúñ.\s]+\s\d+$'
    return bool(re.match(pattern, address.strip())) 