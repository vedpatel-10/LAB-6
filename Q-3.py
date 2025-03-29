def is_leapyear(year):
    if ((year % 400) == 0) or (((year % 4 == 0) and (year % 100 != 0))):
        return True
    else :
        False

def number_of_days(day,month,year):
    days = 0
    for  i in range(1,year):
        if is_leapyear(i):
            days = days + 366
        else:
            days = days + 365    

    if is_leapyear(i):
        days_in_months = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    days = days + days_in_months[month-1]

    days =  days + day

    return days

date1 = (1,1,2023)
date2 = (20,3,2025)

d1,m1,y1 =date1
d2,m2,y2 =date2

days_of_date1 = number_of_days(d1,m1,y1)
days_of_date2 = number_of_days(d2,m2,y2)

difference = abs(days_of_date1 - days_of_date2)

print(f"Total days between are : {difference}")
