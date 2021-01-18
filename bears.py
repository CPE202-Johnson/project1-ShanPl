#int -> boolean
'''
A True return value means that it is possible to win
the bear game by starting with n bears. A False return value means
that it is not possible to win the bear game by starting with n
bears.

The rules: 
If n is even, then you may give back n/2 bears.
If n is divisible by 3 or 4, then you may multiply the last two 
digits of n and give back this many bears.
If n is divisible by 5, then you may give back 42 bears.
'''


def bears(n):
    # n is an int representing the number of bears
    #div_2 is a bool representing even divisibility and possible to win
    #div_3_4 is a bool for if it's divisible by either 3 or 4 
    # and possible to win
    #div_5 is a bool for if it's divisible by 5 and possible to win
    div_2 = False
    div_3_4 = False
    div_5 = False

    if n == 42:
        return True
    if n <= 0:
        return False
    if n%2 == 0: #if even, give back n/2 bears
        div_2 = bears(n/2)
    if ((n%3 == 0) or (n%4 == 0)) and div_2 == False:
        # If it wasn't divisible by 2 but it is divisible by 3 or 4,
        last = n%10 
        second_to_last = n//10%10
        if last*second_to_last != 0:
            div_3_4 = bears(n - (last*second_to_last))
        # div_3_4 is true if it is possible to win with that path
    if (n%5 == 0) and div_2 == False and div_3_4 == False:
        div_5 = bears(n - 42)
    
    if div_2 or div_3_4 or div_5:
        return True
    else:
        return False