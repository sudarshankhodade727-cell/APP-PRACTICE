# Closure Example in Python

def outer_function(message):
    def inner_function():
        print("Message:", message)
    return inner_function

# Create a closure
closure = outer_function("Hello, Python!")

# Call the closure
closure()
