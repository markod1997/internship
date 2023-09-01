import csv
import random

# Date generation function
def generate_date():
  # Pick a random year between 1960 and 2022
  year = random.randint(1960, 2022)
  # Pick a random month
  month = random.randint(1, 12)
  # Pick a random day
  max_day=31
  if month==2:
      #Check if leap year
      if (year % 400==0) or (year % 100 !=0 and year % 4==0):
          max_day=29
      else:
          max_day=28
  elif month in [4, 6, 9, 11]:
      max_day=30
  day = random.randint(1, max_day)

  # List of format patterns
  format_patterns = [
      "{day} {month_name} {year}",
      "{day}/{month}/{year}",
      "{day}.{month}.{year}",
      "{day}-{month}-{year}"
  ]

  # Select a random format pattern
  format_pattern = random.choice(format_patterns)

  # Get the month name
  month_names = {
      1: 'janvier',
      2: 'février',
      3: 'mars',
      4: 'avril',
      5: 'mai',
      6: 'juin',
      7: 'juillet',
      8: 'août',
      9: 'septembre',
      10: 'octobre',
      11: 'novembre',
      12: 'décembre'
  }
  month_name = month_names[month]

  # Format the date using the selected pattern
  date = format_pattern.format(day=day, month=month, month_name=month_name, year=year)

  return date

# Write a .csv file with 2000 generated dates
dates=[]
for _ in range(2000):
  date=generate_date()
  dates.append(date)

with open('Dates_spreadsheet.csv', 'w', encoding='utf-8', newline='') as csv_file:
  fieldnames=['dates']
  writer=csv.writer(csv_file)
  writer.writerow(fieldnames)

  for date in dates:
    writer.writerow([date])
