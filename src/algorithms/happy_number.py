"""
happy number implementation
"""

def is_happy(n: int) -> bool:
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum_of_squares(n)
        if n == 1:
            return True
        
    return False

def sum_of_squares(n: int) -> int:
    output = 0
    while n != 0:
        digit = n % 10
        digit = digit * digit
        output += digit
        n = n // 10

    return output