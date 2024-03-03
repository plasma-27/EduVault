import hashlib

class uid:
    def __init__(self,unique_12_digit_number,who):
        self.unique_12_digit_number=unique_12_digit_number
        self.who=who  #1 for Student 
                      #0 for institute
    
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

        if self.who == 1:
            unique_12_digit_number = "S" + unique_12_digit_number
        elif self.who == 0:
            unique_12_digit_number = "I" + unique_12_digit_number
        else:
            raise ValueError("Invalid 'who' value. It should be either 0 or 1.")

        return unique_12_digit_number

# Example usage
# unique_12_digit_number = "374927094667"
# generated_number = generate_10_digit_number(unique_12_digit_number)
# print("Generated 10-digit number:", generated_number)