print(0.1 + 0.1 + 0.1 == 0.3)

print(round(.1, 1) + round(.1, 1) + round(.1, 1) == round(.3, 1))

from decimal import Decimal

print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) == Decimal(0.3))

"""
Answer

They are all False

Explanation
Floats in Python are binary floating-point numbers. 

Neither decimal value 0.1 or 0.3 can be represented exactly as binary fractions they are both only approximations.

Rounding doesn’t help because the numbers cannot get any closer to their ‘real’ Base 10 decimal values.

When Decimal is initialised with a float it takes the exact value of the float so this is still equivalent to:
0.1 + 0.1 + 0.1 == 0.3

Only by passing strings to Decimal would we get the intuitive result of True: 
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3')

"""