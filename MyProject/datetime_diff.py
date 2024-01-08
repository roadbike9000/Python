import datetime

date_1 = datetime.datetime.strptime('11/29/2023 10:25', '%m/%d/%Y %H:%M')  
date_2 = datetime.datetime.strptime('11/29/2023 11:18', '%m/%d/%Y %H:%M')

diff = date_2 - date_1  

days = diff.days
seconds = diff.seconds    
hours = days * 24 + seconds // 3600
minutes = (seconds % 3600) // 60

print('{}:{}'.format(hours, minutes))
