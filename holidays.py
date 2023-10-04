#!/usr/bin/python3
''' This script is a convenience class that
    will determine the holidays for
    a given year.
'''


import os
import sys
from datetime import datetime, timedelta

class Holidays(object):
    ''' Convenience class that returns dict of holidays for a given year
        as a dict of strings in the format d['NewYear'] = 'yyyy-mm-dd'
    '''
    def __init__(self, year):
        if type(year) == str:
            self.year= int(year)
        else:
            self.year = year
        self.aweek = timedelta(weeks=1)
        self.aday = timedelta(days=1)
        self.dates = {}
        self.holiday_name_given_date = {}
        self.date_given_holiday = {}
        self.dates['datetime'] = [] # list of holiday datetimes are placed here
        self.dates['string'] = [] # list of holiday datetimes in string format
        # other dates would be in form: self.dates['NewYear'] = '2000-01-01'

        # New Year
        self.dates['datetime'].append(datetime(self.year, 1, 1))
        self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))
        self.date_given_holiday['NewYear'] = self.convert_dt_to_str(self.dates['datetime'][-1])
        self.holiday_name_given_date[self.date_given_holiday['NewYear']] = 'NewYear'

        # Canada Day
        self.dates['datetime'].append(datetime(self.year, 7, 1))
        self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))
        self.date_given_holiday['CanadaDay'] = self.convert_dt_to_str(self.dates['datetime'][-1])
        self.holiday_name_given_date[self.date_given_holiday['CanadaDay']] = 'CanadaDay'

        # Christmas Day
        self.dates['datetime'].append(datetime(self.year, 12, 25))
        self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))
        self.date_given_holiday['Christmas'] = self.convert_dt_to_str(self.dates['datetime'][-1])
        self.holiday_name_given_date[self.date_given_holiday['Christmas']] = 'Christmas'

        # Remembrance Day
        self.dates['datetime'].append(datetime(self.year, 11, 11))
        self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))
        self.date_given_holiday['RemembranceDay'] = self.convert_dt_to_str(self.dates['datetime'][-1])
        self.holiday_name_given_date[self.date_given_holiday['RemembranceDay']] = 'RemembranceDay'

        # Boxing Day
        self.dates['datetime'].append(datetime(self.year, 12, 26))
        self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))
        self.date_given_holiday['BoxingDay'] = self.convert_dt_to_str(self.dates['datetime'][-1])
        self.holiday_name_given_date[self.date_given_holiday['BoxingDay']] = 'BoxingDay'

        # Victoria Day: Monday before May 25
        self.dates['datetime'].append(self.get_victoria_day())
        self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))
        self.date_given_holiday['VictoriaDay'] = self.convert_dt_to_str(self.dates['datetime'][-1])
        self.holiday_name_given_date[self.date_given_holiday['VictoriaDay']] = 'VictoriaDay'

        # Family Day: 3rd Monday in February
        self.dates['datetime'].append(self.get_date(3, 1, 2))
        self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))
        self.date_given_holiday['FamilyDay'] = self.convert_dt_to_str(self.dates['datetime'][-1])
        self.holiday_name_given_date[self.date_given_holiday['FamilyDay']] = 'FamilyDay'

        # Thanksgiving: 2nd Monday in October
        self.dates['datetime'].append(self.get_date(2, 1, 10))
        self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))
        self.date_given_holiday['ThanksgivingDay'] = self.convert_dt_to_str(self.dates['datetime'][-1])
        self.holiday_name_given_date[self.date_given_holiday['ThanksgivingDay']] = 'ThanksgivingDay'
        
        # Labour Day: 1st Monday in September
        self.dates['datetime'].append(self.get_date(1, 1, 9))
        self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))
        self.date_given_holiday['LabourDay'] = self.convert_dt_to_str(self.dates['datetime'][-1])
        self.holiday_name_given_date[self.date_given_holiday['LabourDay']] = 'LabourDay'

        # Heritage/Civic Day: 1st Monday in August
        self.dates['datetime'].append(self.get_date(1, 1, 8))
        self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))
        self.date_given_holiday['CivicDay'] = self.convert_dt_to_str(self.dates['datetime'][-1])
        self.holiday_name_given_date[self.date_given_holiday['CivicDay']] = 'CivicDay'

        # Easter : -----
        easter = self.get_easter()
        
        # Good Friday: -----
        self.dates['datetime'].append(easter - 2*self.aday)
        self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))
        self.date_given_holiday['GoodFriday'] = self.convert_dt_to_str(self.dates['datetime'][-1])
        self.holiday_name_given_date[self.date_given_holiday['GoodFriday']] = 'GoodFriday'
        # Easter Monday: -----
        # self.dates['datetime'].append(easter + self.aday)
        # self.dates['string'].append(self.convert_dt_to_str(self.dates['datetime'][-1]))

    def convert_dt_to_str(self, dt): # format is 'yyyy-mm-dd'
        return '-'.join([str(x).zfill(2) for x in [dt.year, dt.month, dt.day]])

    def get_easter(self):
        g = self.year % 19
        c = self.year // 100
        h = (c - (c // 4) - (8 * c + 13) // 25 + 19 * g + 15) % 30
        i = h - (h // 28) * (1 - h//28  * (29 // (h+1)) * (21-g)//11)
        day = i -((self.year + self.year//4 + i + 2 - c + (c//4)) % 7) + 28
        month = 3
        if day > 31:
            month += 1
            day -= 31
        return datetime(self.year, month, day)

    def get_victoria_day(self):
        for i in range(24, 17, -1):
            new_day = datetime(self.year, 5, i)
            if new_day.weekday() == 0:
                break
        return new_day

    # order is 3 for third, Monday is 1, Jan is 1
    def get_date(self, order, yday, ymonth):
        ''' order is 1 for first, 2 for second, 3 for third, etc
            yday is 1 for Monday, 2 for Tuesday, etc
            ymonth is 1 for Jan, 2 for Feb, etc.
            So, if you want to know the date of
            3rd Friday of March, order=3, yday=5 and ymonth=3
        '''
        first_day = datetime(self.year, ymonth, 1)
        yday -= 1
        for i in range(7):
            new_day = datetime(self.year, ymonth, i+1)
            if new_day.weekday() == yday:
                break
        return new_day+(order-1)*self.aweek

if __name__ == '__main__':
    hol = Holidays('2014')
    print('list of holiday dates:')
    for x in hol.dates['string']:
        print(x)

    print('\n\nHoliday Details:')
    for name, xdate in hol.date_given_holiday.items():
        print(f'{name}: {xdate}')

    print('\n\nReverse Holiday')
    for xdate, xname in hol.holiday_name_given_date.items():
        print(f'{xdate}: {xname}')

