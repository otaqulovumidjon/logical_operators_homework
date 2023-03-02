def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a == int(a) and abs(a) >= 10 and abs(a) <= 99

print(main(100))