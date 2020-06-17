'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # I was thinking way too hard about this... I forgot about the count method until halfway through writing the first solution
    for i in range(0, len(arr)):
        if arr.count(i) == 1:
            return i


    # [3, 6, 4, 5, 6, 3, 4]
    # if we are at index 0 = 3
    # loop through copied arr

        # cur_index = i
        # for j in range(cur_index + 1, len(arr)):
        #     if j == cur_index:
        #         return 
        #     else:
        #         return j
    # and the value 3 is in the rest of the array,
    # we move to the next index
    # but if the value is not in the array we return that value

    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")