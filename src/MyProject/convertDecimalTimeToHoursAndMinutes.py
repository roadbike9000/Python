import math

decimal_time = 0.45

hours = math.floor(decimal_time)
decimal_minutes = (decimal_time - hours) * 60
minutes = round(decimal_minutes)

time_format = '{:02}:{:02}'.format(int(hours), int(minutes))

print(time_format)
