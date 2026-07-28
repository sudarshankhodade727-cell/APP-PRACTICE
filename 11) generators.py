# 1. Basic Generator
def count_up_to(n):
    for i in range(1, n + 1):
        yield i

print("1. Basic Generator:")
for num in count_up_to(5):
    print(num)

# 2. Generator with next()
def fruits():
    yield "Apple"
    yield "Banana"
    yield "Cherry"

print("\n2. Using next():")
g = fruits()
print(next(g))
print(next(g))
print(next(g))

# 3. Infinite Generator
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

print("\n3. Infinite Generator (First 5 Even Numbers):")
g = even_numbers()
for _ in range(5):
    print(next(g))

# 4. Generator Expression
print("\n4. Generator Expression:")
squares = (x * x for x in range(6))
for square in squares:
    print(square)

# 5. Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\n5. Fibonacci Generator:")
for num in fibonacci(10):
    print(num)

# 6. File Reading Generator (Example)
def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

# 7. Generator vs List
print("\n7. List vs Generator:")

# List stores everything in memory
list_squares = [x * x for x in range(10)]

# Generator creates values one at a time
gen_squares = (x * x for x in range(10))

print("List:", list_squares)

print("Generator:")
for value in gen_squares:
    print(value)

print("\nAll generator examples executed successfully!")
