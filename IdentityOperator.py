# Identitiy operators in Python 
# is True if operand are identical 
# is not True if operand are not identical 

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

# Here x3 and y3 are not identical because the interpreter locates them seperatley 