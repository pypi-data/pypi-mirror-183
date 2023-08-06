#A Method to find if a number is even or not
def is_even(number):
    if number%2==0 and number>0:
        return True
    return False
#A Method to find if a number is odd or not
def is_odd(number):
    if number%2==1 and number>0:
        return True
    return False
#A Method to find Sum of First N Numbers
def sum_n(number):
    return (number * (number+1))//2
#A Method to find a number is prime or not
def is_prime(number):
    if number<2:
        return False
    for fact in range(2, 1+int(number**.5)):
        if number%fact==0:
            return False
    return True
        