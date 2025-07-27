#Task 1: Calculate factorial Using function
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*(factorial(n-1))
number=int(input('enter_the_number: '))
result=factorial(number)

print(f"The factorial of {number} is {result}")



#task2: Using the Math module for calculations
import math
number=float(input("Enter the Number: "))
sqrt_result=math.sqrt(number)
log_result=math.log(number)
sine_result=math.sin(number)
print(f"\nResults for the number {number}: ")
print(f"Square root: {sqrt_result}")
print(f"Natural logarithm (base e): {log_result}")
print(f"Sine (in radians):{sine_result}")

