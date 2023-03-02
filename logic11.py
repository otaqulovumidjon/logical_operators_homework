def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a == int(a) and abs(a) >= 100 and abs(a) <= 999

print(main(123))