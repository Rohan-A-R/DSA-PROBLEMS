# 1st method
def convert_to_roman(n):
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    roman=""

    for values,symbol in values:
        while n>=values:
            roman+=symbol
            n-=values

    return roman
n=232
print(convert_to_roman(n))

# 2nd method(better)
def convert_to_roman_2nd_method(n):
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    roman=""
    for value,symbol in values:
        count=n//value
       
        roman+=symbol*count
        n%=value
    return roman
n=2500
print(convert_to_roman_2nd_method(n))

