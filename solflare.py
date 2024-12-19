BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def base58_encode(data: bytes) -> str:
    # Convert the byte array to a single integer
    num = int.from_bytes(data, "big")
    
    # Encode the integer into Base58
    encoded = ""
    while num > 0:
        num, remainder = divmod(num, 58)
        encoded = BASE58_ALPHABET[remainder] + encoded

    # Add leading '1's for each leading zero byte in the data
    num_zeros = len(data) - len(data.lstrip(b'\x00'))
    return "1" * num_zeros + encoded

# Get user input for the list of integers
user_input = input("Enter a list of integers (comma-separated): ")
try:
    # Convert the input string into a list of integers
    data_list = [int(x.strip()) for x in user_input.split(",")]
    
    # Convert the list of integers into a byte array
    data = bytes(data_list)
    
    # Encode the byte array into Base58
    encoded = base58_encode(data)
    print("Base58 Encoded:", encoded)
except ValueError:
    print("Invalid input. Please enter a list of integers separated by commas.")

