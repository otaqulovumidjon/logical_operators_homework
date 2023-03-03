def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a==int(a) and abs(a)>=10 and abs(a)<=99 and (abs(a)//10 + abs(a)%10)%2 == 1

print(main(45))