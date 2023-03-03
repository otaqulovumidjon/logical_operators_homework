def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a==int(a) and (abs(a)//10000>abs(a)//1000%10>abs(a)//100%10>abs(a)//10%10>abs(a)%10 or \
                          abs(a)//10000<abs(a)//1000%10<abs(a)//100%10<abs(a)//10%10<abs(a)%10)

print(main(54321))