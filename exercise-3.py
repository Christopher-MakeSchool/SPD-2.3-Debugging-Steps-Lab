"""
Exercise 3
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
# HINT: It may help to draw a picture to clarify what your assumptions are.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr


# [5, 2, 3, 1, 6]    i = 1  |  key = 2  |  j = 0  |  arr[j] = 5  |  arr[j+1] = 2    --> replace right to left giving us [2, 5, 3, 1, 6]
# [2, 5, 3, 1, 6]    i = 2  |  key = 3  |  j = 1  |  arr[j] = 5  |  arr[j+1] = 3    --> replace right to left giving us [2, 3, 5, 1, 6]
# [2, 3, 5, 1, 6]    i = 3  |  key = 1  |  j = 2  |  arr[j] = 5  |  arr[j+1] = 1    --> replace right to left giving us [2, 3, 1, 5, 6]

# [2, 3, 1, 5, 6]    i = 4  |  key = 6  |  j = 3  |  arr[j] = 5  |  arr[j+1] = 6    While statement not met    | key > arr[j]



if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)


#! Plan OF Attack
'''
First, Skim the Functions main and insertion_sort from above, what do you expect to be outputed?
  - expected output
    - ### Problem 3 ###
    - [1, 2, 3, 5, 6]
Next, Run the code in the terminal with pyhron3 exercise-3.py to view the Actual Output
  - actual
    - ### Problem 3 ###
      Traceback (most recent call last):
        File "exercise-3.py", line 34, in <module>
          answer = insertion_sort([5, 2, 3, 1, 6])
        File "exercise-3.py", line 26, in insertion_sort
          while key < arr[j] : 
      IndexError: list index out of range
Looks Like we got a call to the Traceback, can you spot what the error message is?
  - IndexError: list index out of range
Can you find what line(s) may be causing said error?
    - File "exercise-3.py", line 26, in insertion_sort
    - File "exercise-3.py", line 34, in <module>
  - Lines 26 & 34
What can you deduce about the cause of the error?
  - Index Errors typically happen when using an array or loop,
  - Assuming the developers didn't properly account for the index starting at 0 rather than 1
  - This error is most likely to be solved on by fixing one of the 2 contitons for the avalibe loops (for & while)
What assumptions did the developer(s) make, State them here
  - The Developers assumed the array would not alreay be sorrted
State your Solutions/Assumptions here
  - This is a common algorithm, there is definitally examples online I can compare or borrow from, googling around we get this article from [GeeksforGeeks on Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)
  - To Fix this error Change it looks like we need to add ```j >= 0 and``` To line 26 making it ``` while j >= 0 and key < arr[j]: ```
'''
