y = int(input("Enter the year you want to test: "))
def is_leap_year(y: int):
    return y%4==0 and not (y%100!=0 and not y%400==0)

print(is_leap_year(y))

##Last Test