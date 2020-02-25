from . import DateTimeFunctions as DTF

def get_txt_file_name():
    #directory = "/WorkingTemp/"
    name = DTF.get_date_and_time(False) + ".txt"
    return name

def get_video_file_name():
    directory = "/WorkingTemp/"
    name = directory + DTF.get_date_and_time(False) + ".txt"
    return name