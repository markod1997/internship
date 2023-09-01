import pandas as pd
import random
import csv

# Places list shuffle
def shuffle_items(item):
    random.shuffle(item)
    return item

# List of dates
dates_df=pd.read_csv('Dates_spreadsheet.csv')
dates=dates_df['dates']
shuffled_dates=shuffle_items(dates.tolist())

# List of people
people_df=pd.read_csv('People_spreadsheet.csv')
people_names=people_df['first_last_names']
shuffled_names=shuffle_items(people_names.tolist())

# List of places
places_df=pd.read_csv('Places_spreadsheet.csv')
city_names=places_df['Place']
shuffled_places=shuffle_items(city_names.tolist())

# List of organizations
organizations_df=pd.read_csv('Organizations_spreadsheet.csv')
organization_column=organizations_df['Organizations']
shuffled_orgs=shuffle_items(organization_column.tolist())

# List of materials
materials_df=pd.read_csv('Materials_spreadsheet.csv')
materials_column=materials_df['materials']
shuffled_materials=shuffle_items(materials_column.tolist())

# List of events
events_df=pd.read_csv('Events_spreadsheet.csv')
events_column=events_df['events']
shuffled_events=shuffle_items(events_column.tolist())


data = []
# Example 20 rows
for _ in range(200):
    date=shuffled_dates.pop(0)
    person = shuffled_names.pop(0)
    place=shuffled_places.pop(0)
    organization=shuffled_orgs.pop(0)
    material=shuffled_materials.pop(0)
    event=shuffled_events.pop(0)

    row = [date, person, place, organization, material, event]
    data.append(row)

# matrix column names
fieldnames = ["DATE", "PERSON", "PLACE", "ORGANIZATION", "MATERIAL", "EVENT"]
filename = "matrix.csv"

# Output file
with open(filename, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(fieldnames)
    writer.writerows(data)
