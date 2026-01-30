import random

# Show all functions in random module
print(dir(random))

# Show documentation of random module
print(random.__doc__)

# Random float number between 0 and 1
print(random.random())

# Random float number between 5 and 10
print(random.uniform(5, 10))

# Random integer between 1 and 100
print(random.randint(1, 100))

# Random number from range with step
print(random.randrange(1, 100, 5))

# List of fruits
fruits = ["Apple", "Banana", "Cherry"]

# Random choice from list
print(random.choice(fruits))

# Shuffle the list
random.shuffle(fruits)
print(fruits)

# Function to generate 4-digit PIN
def generate_pin():
    return random.randint(1000, 9999)

# Print generated PIN
print(f"Your 4 digit pin: {generate_pin()}")
