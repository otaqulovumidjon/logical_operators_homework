def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a==int(a) and abs(a)>=100 and abs(a)<=999 and (abs(a)//100 + abs(a)//10%10 + abs(a)%10)%2 ==1

print(main(997))