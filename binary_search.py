def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2  # Corrected calculation
        if list[midpoint] == target:
            return list[midpoint]
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

# Test data

def verify (index):
    if index is not None:
        print("Target found at index: ",index)
    else:
        print("Target not found in list")

numbers=[1,2,3,4,5,6,7,8,9,10]

result=binary_search(numbers,7)
print(result)

result=binary_search(numbers,11)
verify(result)
""""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7  # Target value is 10
result = binary_search(numbers, target)
print(result)  # Should print 9 if everything is correct
"""