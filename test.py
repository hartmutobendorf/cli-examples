from datetime import timedelta
from mydates.dates import format_timedelta
delta = timedelta(seconds=10840)
print (format_timedelta(delta, threshold=100, format='long', granularity='second', locale='en_US'))
print (format_timedelta(delta, threshold=100, format='short', granularity='second', locale='en_US'))
print (format_timedelta(delta, threshold=100, format='narrow', granularity='second', locale='en_US'))
print (format_timedelta(delta, threshold=100, format='narrow', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, threshold=100, format='short', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, threshold=100, format='long', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, format='long', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, granularity='second', locale='de_DE'))

print ('--------------')

print (format_timedelta(delta, depth='full', threshold=1, format='short', granularity='second', locale='en_US'))
print (format_timedelta(delta, depth='full', threshold=1, format='long', granularity='second', locale='en_US'))
print (format_timedelta(delta, depth='full', threshold=1, format='narrow', granularity='second', locale='en_US'))
print (format_timedelta(delta, depth='full', threshold=1, format='narrow', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, depth='full', threshold=1, format='short', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, depth='full', threshold=1, format='long', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, depth='full', format='long', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, depth='full', granularity='second', locale='de_DE'))

print ('--------------')

print (format_timedelta(delta, depth='fullest', threshold=1, format='short', granularity='second', locale='en_US'))
print (format_timedelta(delta, depth='fullest', threshold=1, format='long', granularity='second', locale='en_US'))
print (format_timedelta(delta, depth='fullest', threshold=1, format='narrow', granularity='second', locale='en_US'))
print (format_timedelta(delta, depth='fullest', threshold=1, format='narrow', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, depth='fullest', threshold=1, format='short', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, depth='fullest', threshold=1, format='long', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, depth='fullest', format='long', granularity='second', locale='zh_CN'))
print (format_timedelta(delta, depth='fullest', granularity='second', locale='de_DE'))
