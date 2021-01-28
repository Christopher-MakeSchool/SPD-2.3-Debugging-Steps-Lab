"""
Exercise 2
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

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True

#! Plan OF Attack
'''
First, Skim the functions main and contains_3_consecutive from above, what do you expect to be outputed?
  - expected output
      - for answer1: [1,2,4] it would make evaulate based on 
          # if (list_of_nums[i+1] == list_of_nums[i] + 1 and list_of_nums[i+2] == list_of_nums[i] + 2):
          Thus between      ( indexes 0 & 1)              and              (indexes 0 & 2)
          or vaules             ( 1 , 2 )                 and                  ( 1 , 4 )
          Evaulated as             true                   and                    false              --> false
      - We would then expect it to print false

      - for answer2 
          # if (list_of_nums[i+1] == list_of_nums[i] + 1 and list_of_nums[i+2] == list_of_nums[i] + 2):
          Thus between      ( indexes 0 & 1)             and              (indexes 0 & 2)
          or vaules             ( 4 , 1 )                and                   ( 4 , 2 )
          Evaulated as            false                  and                     false              --> false
      - We would then expect it to go to the next index and compare but it fails/exits
    
    - output would be:
      - ### Problem 2 ###
      - False
      - True
Next, Run the code in the terminal with pyhron3 exercise-2.py to view the Actual Output
  - actual
    - ### Problem 2 ###
    - False
    - Flase
What error message (if any) is there?
Can you find what line(s) may be causing said error?
  - No Error message, But I Have a hunch it has something to do with the logic of the if statement of line 21
What can you deduce about the cause of the error?
  - Due to the and comparison in the if statement, but value must equate to true for it to pass
What assumptions did the developer(s) make, State them here
  - They may have assumed that the input list was sorted in assending order i.e. [1,2,3] or [24,25,26]
State your Solutions/Assumptions here
  # For loop only Looks through all but the last 2 elements
  # The Function defaults to false
  # If the value one position after me is 1 bigger than me by 1 and the value 2 positions after me is 2 bigger than me
  #   --> Then return true | otherwise return false

  - To Fix this edge case / error, remove the else statement
'''
