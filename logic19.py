def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.
    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    return x==int(x) and x>=10 and x<=999 and (x//10 == x%10 or x//100 == x%10)
    
print(main(343))