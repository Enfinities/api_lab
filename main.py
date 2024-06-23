import random

def random_data_string():
    random_number = random.randint(10000, 99999)
    return f"your random data {random_number}"

# Example usage
print(random_data_string())

