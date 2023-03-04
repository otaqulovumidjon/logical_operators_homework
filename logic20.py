def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """

    return n==int(n) and n>=10000 and n<=99999 and n//10000 + n//1000%10 + n//100%10 + n//10%10 + n%10 > 2

print(main(10011))