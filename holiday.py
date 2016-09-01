#!/usr/bin/python
# Author: firebovine
# Purpose: HolidayAPI library
# Date: 08/31/2016
# Goals: The bear minimum.

import urllib
import urllib2
import json
import datetime

API_URL = "https://holidayapi.com/v1/holidays"

class Holiday:

  def __init__(self, key, country='US'):
    self.key = key
    self.country = country

  def __repr__(self):
    return "HolidayAPI Instance"

  def get(self, year=datetime.date.today().year, **kwargs):
    args = { 'key': self.key,
             'country': self.country,
             'year': year }
    args.update(kwargs)
    params = urllib.urlencode(args)
    try:
      url = "%s?%s" % (API_URL, params)
      response = urllib2.urlopen(url)
      status_code = response.getcode()
      data = json.load(response)
    except urllib2.URLError, e:
      print e.reason
      return None
    else:
      return data

  def today(self, **kwargs):
    date = datetime.date.today()
    params = { 'year': date.year,
               'month': date.month,
               'day': date.day }
    params.update(kwargs)
    return self.get(**params)

  def upcoming(self):
    params = { 'upcoming': 'true' }
    return self.today(**params)

  def previous(self):
    params = { 'previous': 'true' }
    return self.today(**params)
