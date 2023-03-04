def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.

    Ikki xonali butun x son berilgan bo'lsa, agar x palindromli butun son bo'lsa, true qiymatini qaytaring.
    Butun son palindrom bo'lib, u oldinga qarab o'qisa.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    n1 = x%10
    n2 = x//10
    n = n1*10 + n2
    return x == n