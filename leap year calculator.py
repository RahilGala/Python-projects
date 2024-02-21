def leapyr(n):
    if n%4==0 and n%100!=0:
        if n%400==0:
            return True
    elif n%4!=0:
        return False
    else:
        return False