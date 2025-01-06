# Write a program that calculates the sum of all even numbers from 1 to 100, including 100.

sum_of_even = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum_of_even = number + sum_of_even
print(f"The sum of even numbers from 1 to 100 is {sum_of_even}")