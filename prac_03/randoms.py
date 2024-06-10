import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
print(random.randint(5, 20))
What was the smallest number you could have seen, what was the largest?
Smallest is 5 and largest is 20.

What did you see on line 2?
print(random.randrange(3, 10, 2))
What was the smallest number you could have seen, what was the largest?
Smallest is 3 and largest is 9.
Could line 2 have produced a 4?
No

What did you see on line 3?
print(random.uniform(2.5, 5.5))
What was the smallest number you could have seen, what was the largest?
Smallest is 2.672501407264016 and largest is 5.470996858871242
"""

print(random.randint(1, 100))
