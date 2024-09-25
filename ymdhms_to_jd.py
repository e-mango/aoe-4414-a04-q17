# script_name.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  This converts from year, month, day, hour, minute, second to fractional Julian date
# Parameters:
#  year: year of the time instant
#  month: month of the time instant
#  day: day of the time instant
#  hour: hour of the time instant
#  minute: minute of the time instant
#  second: second of the time instant
# Output:
#  jd_frac: Fractional Julian date

# Written by Evan Schlein
# Other contributors: None

# import Python modules
import sys 
import math

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456


# initialize script arguments
year = float('nan')    # year of the time instant
month = float('nan')   # month of the time instant
day = float('nan')     # day of the time instant
hour = float('nan')    # hour of the time instant
minute = float('nan')  # minute of the time instant
second = float('nan')  # second of the time instant


# parse script arguments
if len(sys.argv) == 7:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
else:
    print(
        'Usage: '
        'python3 ymdhms_to_jd.py year month day hour minute second'
    )
    exit()
# write script below this line

JD = math.floor(day-32075 + 1461*(year+4800+(month-14)/12)/4 + 367*(month-2-(month-14)/12*12)/12 - 3*((year+4900+(month-14)/12)/100)/4)
JD_midnight = JD - 0.5
D_frac = ((second + 60*(minute+60*hour))/86400)
jd_frac = JD_midnight + D_frac

print(jd_frac)