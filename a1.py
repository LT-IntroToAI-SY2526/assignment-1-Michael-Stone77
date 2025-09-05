# Assignment 1: AI-Generated Python Problems
# Name: Michael Stone

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I have some experience with C++ and python. Can you create 5-7 practice problems that cover: Variables and basic data types Conditionals (if/elif/else) Loops (for and while) Functions Basic list operations Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs. Can you make the questions free response instead of multiple choice?

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Variable Assignment and Type Conversion
Create a variable x with the string value "25". Convert it to an integer and store it in a new variable y. Then print the result of y + 10.

PROBLEM 2: Conditional Logic
Write a program that asks the user to input a number. If the number is divisible by both 3 and 5, print "FizzBuzz". If only divisible by 3, print "Fizz". If only divisible by 5, print "Buzz". Otherwise, print the number itself.

PROBLEM 3: Looping with for
Use a for loop to print all the odd numbers between 1 and 20 (inclusive).

PROBLEM 4: Looping with while
Write a while loop that starts with n = 10 and keeps dividing n by 2 until n is less than 1. Print the value of n at each step.

PROBLEM 5: Function with Parameters
Define a function called calculate_area that takes two parameters: length and width. It should return the area of a rectangle. Then call the function with length = 5 and width = 3, and print the result.


Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""


# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
def calculate_area(length, width):
    length = 5 #should make length = 5
    width = 3 #should make width = 3
    calculate_area = length * width #Should multiple the length and width to get 15
    print(calculate_area) #should print the area
# This was my attempt at solving the problem, I ended up getting it wrong as I made three big mistakes:  1. overwriting the parameters with length = 5 and width = 3, making the parameters pointless, 2. naming a variable the same thing as my function as that can confuse the program and cause bugs, and 3. using print instead of return as that limits the use of the function.
def calculate_area(length, width):
    return length * width

result = calculate_area(5, 3)
print(result)
#This was the solution I was able to come up with the assistance of the AI (Copilot) which is bettter as it uses the parameters, avoids naming conflicts, and the return adds flexability to the program.

