# Printing the generated Fibonacci sequence
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = []
if n >= 1:
    fibonacci_sequence.append(0)
if n >= 2:
    fibonacci_sequence.append(1)
for i in range(2, n):
    next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
    fibonacci_sequence.append(next_number)
print("The first", n, "numbers in the Fibonacci sequence are:", fibonacci_sequence)
