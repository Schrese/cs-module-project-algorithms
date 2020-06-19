'''
Input: a List of integers
Returns: a List of integers
'''
# Create a function that uses args/kwargs to multiply the number of elements in an array
def multiply(*numbers):
    x = 1
    for n in numbers:
        x *= n
    return x


def product_of_all_other_numbers(arr):
    # Your code here
    # pass
    # get result of all numbers passed in
    result = multiply(*arr)
    print(result)
    # loop over arr
    for i in range(len(arr)):
        # multiple i by next element
        new_number = result// arr[i]
        arr[i] = new_number

    return arr

# Idea for tomorrow:
    # keep track of current index
    # while current index > len(arr)
    # using slicing with the current index
    # to create a list of arguments to pass in
    # send ^ list into a helper product function
    # for each product add it to a new array



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
