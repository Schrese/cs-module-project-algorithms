'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    right_pointer = k
    # final_arr = []
    for i in range(len(nums)):
        # small_arr = nums[i:right_pointer]
        if len(nums[i:right_pointer]) == k:
            # new_num = max(nums[i:right_pointer])
            nums[i] = max(nums[i:right_pointer])
            # final_arr.append(max(nums[i:right_pointer]))
            # nums[i] = new_num
            # print(i, new_num, small_arr, right_pointer, k)
            right_pointer += 1
        else:
            nums.pop()
                # k += 1
            # sliding_window_max(small_arr, k)
    return nums


# def sliding_window_max(nums, k):
#     right_pointer = k

#     for i in range(len(nums)):
#         # small_arr = nums[i:right_pointer]
#         if len(nums[i:right_pointer]) == k:
#             # new_num = max(nums[i:right_pointer])
#             nums[i] = max(nums[i:right_pointer])
#             # nums[i] = new_num
#             # print(i, new_num, small_arr, right_pointer, k)
#             right_pointer += 1
#         else:
#             nums.pop()
#                 # k += 1
#             # sliding_window_max(small_arr, k)
#     return nums

    # Your code here
    # final_arr = []
    # create a pointer that will point to the element to remove
    # pointer = 0
    # # to get rid of this "final_arr" I will need to replace the element at i with the max number 
    # for i in range(len(nums)):
    #     small_arr = nums[i:k]
    #     largest = max(small_arr)
    #     print(small_arr)
    #     nums[i] = largest
    #     # final_arr.append(largest)
    #     # i += 1
    #     k += 1

    #     # increment the pointer
    #     pointer += 1
    # print(pointer)
    # if pointer > len(nums):
    #     return
    # return nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

# def find_highest(arr):
#     max = arr[0]
#     for i in arr:
#         if i > max:
#             max = i
#     return max

# def sliding_window_max(nums, k):
#     # Your code here
#     # create an array to return
#     final_arr = []
#     # pass
#     # loop through the elements in nums until we get to the end of the array + 1
#     for i in range(len(nums) - k+1):
#         # set a smaller array for the "window"
#         small_arr = nums[i:k]
#         # print(small_arr)
#         # set a variable to the result of the find_highest function
#         largest = find_highest(small_arr)
#         # append that result to the output array
#         final_arr.append(largest)
#         # print(largest)
#         # increment i and k
#         i += 1
#         k += 1
#         # for j in range(nums[i:k]):
#         #     small_nums = nums[i:k]
#         #     print(nums[i:k])
#     return final_arr

