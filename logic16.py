def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a==int(a) and abs(a)>=10000 and abs(a)<=99999

print(main(-12345))