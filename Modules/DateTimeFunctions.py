import datetime

def get_time():
    dateTime = datetime.datetime.now()
    theHour = str(dateTime.hour)
    theMinute = str(dateTime.minute)
    theSecond = str(dateTime.second)
    tm = theHour + "-" + theMinute + "-" + theSecond
    return tm

def get_date():
    dateTime = datetime.datetime.now()
    theYear = str(dateTime.year)
    theMonth = str(dateTime.month)
    theDay = str(dateTime.day)
    dt = theYear + "-" + theMonth +"-" + theDay
    return dt

def get_date_and_time(separated: bool):
    if(separated == True):
        return get_date() + "    " + get_time()
    else:
        return get_date() + "_" + get_time()

        

