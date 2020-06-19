'''
Input: an integer
Returns: an integer
'''
# optimized solution
def eating_cookies(n, cache):
    # Your code here
    # pass 
    # change to be using elif's to run faster because it doesn't need to check the rest of the if's (but only if i'm not returning)
    if n < 0: 
        return 0
    elif n == 0: 
        return 1 
    # if n == 2: 
    #     return 2 
    # if n == 3: 
    #     return 4 
    elif cache[n] > 0:
        return cache[n]
    else: 
        cache[n] = eating_cookies(n - 3, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 1, cache) 
    return cache[n]

# def eating_cookies(n):
#     # Your code here
#     # pass 
#     # change to be using elif's to run faster because it doesn't need to check the rest of the if's (but only if i'm not returning)
#     if n < 0: 
#         return 0
#     if n == 0:
#         return 1
#     if n == 1: 
#         return 1 
#     if n == 2: 
#         return 2 
#     if n == 3: 
#         return 4 
#     if n > 3: 
#         return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1) 
 
if __name__ == "__main__": 
    # Use the main function here to test out your implementation 
    num_cookies = 5 
 
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies") 
