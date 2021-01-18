#(int, int) --> int
#num is the int that should be converted. b is the new base it's converting to.
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    convert_string = "0123456789ABCDEF"
    quotient = num//b
    remainder = num%b
    #quotient and remainder are both ints obtained after dividing num by b
    if quotient == 0:
        return convert_string[remainder]
    
    # concatenate the converted quotient 
    # with the current remainder as a single character string
    return convert(quotient,b) + convert_string[remainder]
print(convert(316,16))