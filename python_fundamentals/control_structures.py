#if, else, and elif Statements:
  # Conditional control si straightforward in Python, using indentation instead of parentheses.

x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

#for Loops:
 # Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Loop through a range
for i in range(5):
    print(i)
#while Loops:
# While loop until the condition becomes False
i = 0
while i < 5:
    print(i)
    i += 1 # increment i by 1