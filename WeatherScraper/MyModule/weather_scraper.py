import requests
from bs4 import BeautifulSoup

# Get URL from National Weather Forecast, after searching for location (La Jolla)
source = requests.get('https://forecast.weather.gov/MapClick.php?lat=32.8592&lon=-117.2519#.Xe9MFpNKh0s').text
soup = BeautifulSoup(source, 'lxml')
week = soup.find(id = 'seven-day-forecast-body')
# Set up BeautifulSoup for reading the table of weather conditions

# Organize items from HTML container
items = week.find_all(class_='tombstone-container')

weekly_periods = []
for period in items:
    period_names = period.find(class_='period-name').get_text()
    weekly_periods.append(period_names)

weekly_descs = []
for desc in items:
    short_descriptions = desc.find(class_='short-desc').get_text()
    weekly_descs.append(short_descriptions)

weekly_temps = []
for temp in items:
    temperatures = temp.find(class_='temp').get_text()
    weekly_temps.append(temperatures)
