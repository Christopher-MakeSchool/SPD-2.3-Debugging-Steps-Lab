"""
Exercise 4
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

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        high = len(arr) - 1
    
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            return binary_search(arr, element, low, mid-1)
        else:
            return binary_search(arr, element, mid+1, high)
    else:
      return -1

if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)


#! Plan OF Attack
'''
First, Skim the Functions main and binary_search from above, what do you expect to be outputed?
  - expected output
    - Index of the number being searched for is found, otherwise -1
    - output would be:
    - 4


Next, Run the code in the terminal with pyhron3 exercise-4.py to view the Actual Output
  - actual
      File "exercise-4.py", line 22
      if high == None:
                    ^
      IndentationError: unindent does not match any outer indentation level
Looks Like we got a call to the Traceback, can you spot what the error message is?
  - IndentationError: unindent does not match any outer indentation level
Can you find what line(s) may be causing said error?
    - Line 22 actually 21 the comment needs to align with the first line of code.

Let's rinse and repeat the sets above.
  - Output
      Traceback (most recent call last):
        File "exercise-4.py", line 41, in <module>
          answer = binary_search([1, 2, 4, 5, 7], 7)
        File "exercise-4.py", line 37, in binary_search
          return binary_search(arr, element, mid, high)
        File "exercise-4.py", line 37, in binary_search
          return binary_search(arr, element, mid, high)
        File "exercise-4.py", line 37, in binary_search
          return binary_search(arr, element, mid, high)
        [Previous line repeated 995 more times]
        File "exercise-4.py", line 22, in binary_search
          if high == None:
      RecursionError: maximum recursion depth exceeded in comparison
Looks Like we got a call to the Traceback, can you spot what the error message is?
  - RecursionError: maximum recursion depth exceeded in comparison
  - lines 22, 37, 37, 37, & 41

What can you deduce about the cause of the error?
  - This is a common algorithm, there is definitally examples online I can compare or borrow from,
  googling around we get this article from [GeeksforGeeks on Binary Search](https://www.geeksforgeeks.org/python-program-for-binary-search/)

  - After comparing ours with the article linked above, my solution to fix these errors are:
  1. Reverse the opperation on our second if statement from ```< (less than)``` to ```>= (greater than or equals)```,
      also move the ```return -1``` to an else statement at the bottom of the function.
  2. Indent lines 24 - 33 inside our new if statement.
  3. Last add ```-1``` to ```mid``` in the first call back to this function, and add ```+1``` to the other ```mid```,
      they should not look like this: ```return binary_search(arr, element, low, mid-1)``` & ```return binary_search(arr, element, mid+1, high)```
'''
