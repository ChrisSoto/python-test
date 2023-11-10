import _tester as test;

# check if you are correct by putting your answer as the argument

# MATH OPERATIONS
# QUESTION 1
 
# What are the basic math operators?

# A) + - * /
# B) -- ++ $
# C) < > = ==
# D) @ ! %  

#
#
# test.check_question("1", "A")
#
#

# there are a few more math operators such as "%" Modulo, "**" Exponents and "//" which is floor division
# we are going to learn these

# PROJECT : Write a test
# writing tests to confirm something is working as expected is important in programming
# it is like a small science experiment
# lets write a test to confirm we know how "+" addition works
# What is something we know about addition?

# We know that when two numbers are greater than zero then their sum must be greater than each individually

# this has two conditions to check for
# 1 are the numbers greater than 0
# 2 is the sum greater than each number

def adding_two_numbers_test(x, y):

  # check 1: are then number greater than 0
  if (x > 0 and y > 0):
    # check 2: is the sum greater than each number
    sum = x + y
    if ((sum > x) and (sum > y)):
      print('Addition is working as expected!')
    else:
      # the addition isn't adding because we ended up with a number less than or equal to our known number
      print('This is not addition')
  
  # number not greater than 0
  else:
    print('Test numbers must be greater than 0')

#      
#
# adding_two_numbers_test(1, 1)
#
#

# QUESTION 2

# What does Modulo do in this case: "10 % 5"

# A) divides by 5
# B) adds the numbers and turns the result into a percent (a percent is a number less than one, ex: 0.15 or 15%)
# C) gives the remainder of division

# write a test function that will test each of these
# this is going to be kinda difficult but it's important to understand how to test

def modulo_divides_test(x, y):
  # what would the result be if 10 % 5?
  result = x % y
  # replace '???' with ther result of ten divided by five

  if (result == '???'):
    print('modulo divides')
  else:
    print('modulo does not divide')

modulo_divides_test(10, 5)

# write tests to check the other possible answers to the problem

# B) adds the numbers and turns the result into a percent (a percent is a number less than one, ex: 0.15 or 15%)
# C) gives the remainder of division

def modulo_adds_and_makes_percent_test(x, y):
  print()

def modulo_gets_the_remainder(x, y):
  print()