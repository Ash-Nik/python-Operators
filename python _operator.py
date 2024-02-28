#  Calculate the sum, difference, product, and quotient of two numbers.
num1 = 7
num2 = 4
print("Sum = ", num1 + num2)
print("Difference = ", num1 - num2)
print("Product = ", num1 * num2)
print("Quotient = ", num1 % num2)

print()
# Perform various assignment operations on a variable
var = 100
var += 2  # var = var + 2
var -= 4  # var = var - 4
var *= 4  # var = var * 4
var /= 4  # var = var / 4
var //= 2  # var = var // 2 floor division
print(var)
print()
# S, Compare two numbers and print the results.
x=2
y=3
print( "Both are equal ?",x==y)
print("Both are not equal ? ",x!=y)
print()

# Check conditions using logical operators.
x = 5
y = 10
print(x > 0 and y < 20)  # Output: True
print(x > 0 or y > 20)
z = True
print(not z)
print()

# Check the identity of variables.
var2 = 4
var4=5
print("identity of var2 = ",id(var2),"Identity of var4 = ",id(var4))

# Perform bitwise operations on any two integers.
a = 10
b = 12
result_and = a & b
print("Bitwise AND:", result_and)

result_or = a | b
print("Bitwise OR:", result_or)

result_xor = a ^ b
print("Bitwise XOR:", result_xor)

result_not_a = ~a
print("Bitwise NOT (complement) of a:", result_not_a)
print()

#Use unary operators to change the sign of a number.

x = 5
x = -x
print("After changing sign = ",x)
print()
# Use the ternary operator to assign values based on conditions.

x= 3
y=0 if x%2==0 else 1
print("Value assigned to y = ",y)