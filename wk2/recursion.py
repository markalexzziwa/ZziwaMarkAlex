#factorial
num = int(input("Enter a whole number:"))
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(factorial(num))

#fibinachi
def fib():
    sequence = [0, 1]
    while len(sequence) < 10:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
print(fib())


#binary search
def binary_search(arr, target, left, right):
    # Base case: element not found
    if left > right:
        return -1
        
    mid = (left + right) // 2
    
    # Base case: element found
    if arr[mid] == target:
        return mid
    # Target is in the left half
    elif arr[mid] == target:
        return binary_search(arr, target, left, mid - 1)
    # Target is in the right half
    else:
        return binary_search(arr, target, mid + 1, right)

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]

# Corrected variable name from 'sorted' to 'sorted_array'
print(binary_search(sorted_array, 7, 0, len(sorted_array) - 1))  # Output: 3


