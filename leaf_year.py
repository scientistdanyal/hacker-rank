def is_leap(year):
    leap = False
    
    if year%4==0 or year%400==0:
        leaf = True
    else:
        pass    
    
    return leap

year = int(input())
print(is_leap(year))
