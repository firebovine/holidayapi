# Simple holidayAPI implementation

```
  from holiday import *
  holiday = Holiday(key = 'secret api key')
  print holiday.today()
  print holiday.upcoming()
  print holiday.previous()
  print holiday.(year='2016', month='12', day='25')
  [ x['name'] for x in [holi for sublist in holiday.get()['holidays'].values() for holi in sublist] ]
```
