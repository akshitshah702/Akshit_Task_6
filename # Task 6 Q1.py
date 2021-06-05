# Task 6 Q1

test_str = "ConsulTADd"
  
# printing original string 
print("The original string is : " + str(test_str))
  
# Extract Upper Case Characters 
# Using list comprehension + isupper()
res = [char for char in test_str if char.isupper()]
  
# printing result 
print("The uppercase characters in string are : " + str(res))