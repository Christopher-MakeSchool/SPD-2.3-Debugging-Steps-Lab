"""
Exercise 1
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)


#! Plan OF Attack
'''
First, Skim the Functions find_largest_diff and main from above, what do you expect to be outputed?
  - expected output
    - [2, 2, 1, 4, 2]   --> 4 is the largest difference
    - output would be 4
Next, Run the code in the terminal with pyhron3 exercise-1.py to view the Actual Output
  - actual
    ### Problem 1 ###
    Traceback(most recent call last):
      File "exercise-1.py", line 35, in <module >
      answer = find_largest_diff([5, 3, 1, 2, 6, 4])
      File "exercise-1.py", line 27, in find_largest_diff
      diff = abs(list_of_nums[i] - list_of_nums[i+1])
    IndexError: list index out of range
Looks Like we got a call to the Traceback, can you spot what the error message is?
  - IndexError: list index out of range
Can you find what line(s) may be causing said error?
    - File "exercise-1.py", line 35, in <module >
    - File "exercise-1.py", line 27, in find_largest_diff
  - Lines 35 at 27 are indicated in the traceback
What can you deduce about the cause of the error?
  - Looking at the error and code setup, The Indexing Error occurs in these 2 lines
      - for i in range(len(list_of_nums)):
      -   diff = abs(list_of_nums[i] - list_of_nums[i+1]);
  # Index Errors typically happen when using an array or loop,
What assumptions did the developer(s) make, State them here
  - Assuming the developers didn't account for the index starting at 0 rather than 1
  - This causes the last index value being to 1 to high
State your Solutions/Assumptions here
  - To Fix this error Change ```for i in range(len(list_of_nums)):``` to ```for i in range(len(list_of_nums)-1):```
'''
