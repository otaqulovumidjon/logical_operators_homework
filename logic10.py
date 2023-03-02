def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return abs(a)//10 > 0 and abs(a)%10 >= 0

print(main(12))