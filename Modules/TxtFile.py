from . import DateTimeFunctions as DTF
from . import FileManagement as FM

def create_file():
    """Creates a txt file with filename and format: Date    Time    GPS Data    Speed"""
    fileName = FM.get_txt_file_name()
    f = open(fileName, "w")
    f.write(fileName + "\n")
    f.write("Date        Time        GPS Co-ords    Speed [km/h]\n")
    f.close
    return fileName

def add_to_file(fileName: str):
    f = open(fileName, "a")
    for i in range(2):
        info = DTF.get_date_and_time(separated = True)
        #gpsData = callfunction
        f.write(info + "     GPS Data\n")
        time.sleep(1)
    f.close