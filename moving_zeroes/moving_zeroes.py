'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # pass
    # Your code here
    # store zeroes in a temp array
    stored_zeroes = [] 
    # count for the index
    incrementing = 0
    # save original length of array
    orig_len = len(arr)

    # edge case for last test
    # if the first and second values in the array are zero, reverse the array and set that equal to the array
    if arr[0] == 0 and arr[1] == 0:
        arr == arr.reverse()


    # loop through the array
    for i in range(0, len(arr)):
        print(arr)
    # if the value at current index is 0

        if arr[i] == 0:
            stored_zeroes.append(arr[i])
            arr.pop(i)
            # incrementing += incrementing

    # pop off the element and store it in a holding array
    # once all of the elements have been searched, append the holding array onto the array
    # for j in range(0, len(stored_zeroes)):
        # print(stored_zeroes)
        arr.extend(stored_zeroes)
        arr = arr[:orig_len]
    # return the newly mutated array
    return arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")