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
    return x==int(x) and x>=10 and x<=999 and (x == x//10 + (x%10)*10 or x == x//100 + (x//10%10)*10 + (x%10)*100)
    
print(main(303))