import hashlib

class uid:
    def __init__(self,unique_12_digit_number):
        self.unique_12_digit_number=unique_12_digit_number

    
    def generate_unique_12_digit_number(self):
        # Convert the input number to bytes
        input_bytes = str(self.unique_12_digit_number).encode('utf-8')

        # Calculate the hash using SHA-256 (you can use other hash functions as well)
        hash_result = hashlib.sha256(input_bytes).hexdigest()

        # Take the first 12 characters of the hexadecimal hash
        hash_str = hash_result[:12]

        # Convert the hexadecimal hash to an integer
        hash_integer = int(hash_str, 16)

        # Ensure the generated number is 12 digits long
        unique_12_digit_number = str(hash_integer % (10 ** 12)).zfill(12)

        return unique_12_digit_number

# Example usage
# unique_12_digit_number = "374927094667"
# generated_number = generate_10_digit_number(unique_12_digit_number)
# print("Generated 10-digit number:", generated_number)