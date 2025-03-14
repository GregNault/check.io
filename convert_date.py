#Converts the date format, also has to check the validity of the date inputted

#This one took awhile, tried to do it in one function but got to messy so changed it to three
#Also, had tried to leave variebles as their list address (i.e. int(str_list[0])), but renamed to mon, day, year
#to make it simpler/more readable

def leap_year_check(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year %400 == 0:
                return True
            return False
        return True
    return False
    

def day_check(day, mon, year):
    if day < 1 or day > 31 and mon < 1 or mon > 12:
        return False
    short_month = [4, 6, 9, 11]

    if mon in short_month and day > 30:
        return False
    
    if mon == 2 and leap_year_check(year) == False and day > 28:
        return False
    
    return True
    
def convert_date(date: str) -> str:
    str_list = date.split("/")
    if len(str_list) > 3 or day_check(int(str_list[0]), int(str_list[1]), int(str_list[2])) == False:
        return "Error: Invalid date."
    return str_list[2] + "-" + str_list[1] + "-" + str_list[0]
    


print("Example:")
print(convert_date("29/13/2019"))