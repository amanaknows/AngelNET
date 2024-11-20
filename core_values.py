import hashlib

def compute_checksum(file_path, hash_algo=hashlib.sha256):
    """Compute the checksum of a file using the specified hash algorithm."""
    hash_instance = hash_algo()
    try:
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(8192), b''):
                hash_instance.update(chunk)
    except (IOError, OSError) as e:
        print(f"Error reading file: {e}")
        return None
    return hash_instance.hexdigest()

def validate_checksum(file_path, expected_checksum, hash_algo=hashlib.sha256):
    """Validate the checksum of a file against an expected checksum."""
    return compute_checksum(file_path, hash_algo) == expected_checksum

# Example usage
file_path = 'example_file.txt'
expected_checksum = 'your_expected_checksum_here'

# Compute and validate checksum
computed_checksum = compute_checksum(file_path)
if computed_checksum:
    print(f'Computed Checksum: {computed_checksum}')
    if validate_checksum(file_path, expected_checksum):
        print("Checksum is valid.")
    else:
        print("Checksum is invalid or data is corrupted.")
else:
    print("Failed to compute checksum.")
