def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence[:n]

# Get user input
num_terms = int(input("Enter the number of Fibonacci terms: "))

# Generate and display Fibonacci series
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Sequence:", fibonacci(num_terms))