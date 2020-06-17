'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def find_highest(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

def sliding_window_max(nums, k):
    # Your code here
    # create an array to return
    final_arr = []
    # pass
    # loop through the elements in nums until we get to the end of the array + 1
    for i in range(len(nums) - k+1):
        # set a smaller array for the "window"
        small_arr = nums[i:k]
        # print(small_arr)
        # set a variable to the result of the find_highest function
        largest = find_highest(small_arr)
        # append that result to the output array
        final_arr.append(largest)
        # print(largest)
        # increment i and k
        i += 1
        k += 1
        # for j in range(nums[i:k]):
        #     small_nums = nums[i:k]
        #     print(nums[i:k])
    return final_arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
