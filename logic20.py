def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.

    Bir va noldan iborat raqam berilgan (raqam birdan boshlanadi).
    Agar birliklar soni noldan katta bo'lsa, rost, aks holda False qaytariladi.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """

    return n%10 > 0

print(main(10001))