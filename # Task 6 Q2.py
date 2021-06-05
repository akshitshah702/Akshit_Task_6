# Task 6 Q2
  
# initializing lists
test_keys = ["karan", "User", "Admin"]
test_values = ["Physics", "Chemistry", "Mathematics"]
  
print ("Original key list is : " + str(test_keys))
print ("Original value list is : " + str(test_values))
res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break  
  
# Printing dictionary 
print ("Resultant dictionary is : " +  str(res))