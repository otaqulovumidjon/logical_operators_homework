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
    x1=n//10000
    x2=n//1000%10
    x3=n//100%10
    x4=n//10%10
    x5=n%10

    a = 0
    a = a+(x1%2==1)
    a = a+(x2%2==1)
    a = a+(x3%2==1)
    a = a+(x4%2==1)
    a = a+(x5%2==1)

    b = 0
    b = b+(x1%2==0)
    b = b+(x2%2==0)
    b = b+(x3%2==0)
    b = b+(x4%2==0)
    b = b+(x5%2==0)
    
    return a > b

print(main(10011))