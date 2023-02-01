
#Import date and time to get current year
import datetime

#Returns your guessed age
def GetAge(age):
    return datetime.date.today().year - age

