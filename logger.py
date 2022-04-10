from datetime import datetime  as dt
from time import strftime

def logger():
    #data = ui.choice()[2]
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{} \n'.format(time))