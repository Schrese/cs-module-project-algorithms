'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# with dictionaries
def single_number(nums): # O(n)
    # keep track of number of times an item occurs in input
    counts = {}
    # loop through input list O(n)
    for num in nums:
        # if item in counts
        if num in counts:
            # remove item
            del counts[num]
        # otherwise
        else:
            counts[num] = 1
            # add item
    for k, v in counts.items(): # O(1)
        if v == 1:
            return k
# So. The reason that this is an 0(1) space complexity is because it is setting aside a CONSTANT amount of extra memory (with the counts dictionary or the s set). and the runtime is now O(n) because we're only looping through once (instead of twice which comes with the "count" list method)

# with sets (like in lecture)
# def single_number(arr):
#     s = set() 
#     # use either a dictionary or a set 
#     # sets: holding onto unique elements 
#     # loop through our arr
#     for x in arr:
#         # for each element
#         # check if it is already in our set
#         # if it is, then that's not our out-element-out 
#         if x in s:
#             # remove the element from our set 
#             s.remove(x)
#         else:
#             s.add(x)
#     # the odd-element-out will be the only element in the set 
#     return list(s)[0]



    # I was thinking way too hard about this... I forgot about the count method until halfway through writing the first solution
    # this solution is actually O(n^2) because the count method inherrently does another loop
    # for i in range(0, len(arr)):
    #     if arr.count(i) == 1:
    #         return i


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

    # pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")