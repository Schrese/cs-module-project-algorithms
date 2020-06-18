'''
Input: a List of integers
Returns: a List of integers
'''
# Optimizing
def moving_zeroes(arr):
    # create a "left" pointer
    left_pointer = 0
    # create a "right" pointer
    right_pointer = len(arr) - 1

    print(right_pointer)
    # loop through the array
    # This loop needs to last until the the left and right pointers meet. We can tell if they have met if they are pointing at the same value
    while right_pointer > left_pointer:
        # if the left pointer is at a 0 and the right pointer is not at 0
        if arr[left_pointer] == 0 and arr[right_pointer] != 0:
            # swap the elements at hte left and right pointers, then decrement the right pointer and increment the left pointer
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer] 
            left_pointer += 1
            right_pointer -= 1
            
        # if the left pointer isn't at a 0
        if arr[left_pointer] != 0:
            # increment the left pointer
            left_pointer += 1
        # if the right pointer is at a 0
        if arr[right_pointer] == 0:
            # decrement the right pointer
            right_pointer -= 1
    return arr

# arr = [2, 4, 6, 8] * 10
# arr.append(0)
# print(arr)

# def moving_zeroes(arr):
#     # pass
#     # Your code here
#     # store zeroes in a temp array
#     stored_zeroes = [] 
#     # count for the index
#     incrementing = 0
#     # save original length of array
#     orig_len = len(arr)

#     # edge case for last test
#     # if the first and second values in the array are zero, reverse the array and set that equal to the array
#     if arr[0] == 0 and arr[1] == 0:
#         arr == arr.reverse()


#     # loop through the array
#     for i in range(0, len(arr)):
#         print(arr)
#     # if the value at current index is 0

#         if arr[i] == 0:
#             stored_zeroes.append(arr[i])
#             arr.pop(i)
#             # incrementing += incrementing

    # pop off the element and store it in a holding array
    # once all of the elements have been searched, append the holding array onto the array
    # for j in range(0, len(stored_zeroes)):
        # print(stored_zeroes)
        # arr.extend(stored_zeroes)
        # arr = arr[:orig_len]
    # return the newly mutated array
    # return arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")