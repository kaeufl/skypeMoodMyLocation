# -*- coding: utf-8 -*-

'''
Update the skype mood message with a custom message depending on current
geographic location.

Created on 16.02.2012

@author: pk
'''
import dbus
import urllib
import GeoIP
from curses.has_key import has_key

message_prefix = '@'

message_by_country = {
                      'de' : u'München',
                      'nl' : u'Utrecht'
                      }

myip = urllib.urlopen('http://automation.whatismyip.com/n09230945.asp').read()

gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
mycountry = gi.country_code_by_addr(myip)

if message_by_country.has_key(mycountry.lower()):
    message = message_prefix + message_by_country[mycountry.lower()]
else:
    message = message_prefix + mycountry

# tell skype the new message via dbus
bus = dbus.SessionBus()
obj = bus.get_object("com.Skype.API", "/com/Skype")
iface = dbus.Interface(obj, "com.Skype.API")
iface.Invoke('NAME skypeMoodMyLocation')
iface.Invoke('PROTOCOL 5')
iface.Invoke('SET PROFILE RICH_MOOD_TEXT %s' % message)