import pandas as pd

# Event list
event_df=pd.read_csv('Event_dataframe.csv')
event_columns=['Accident',
               'CBRN Event',
               'Agitating Trouble Making',
               "Coup d'Etat",
               "Civil War Outbreak",
               "Demonstration",
               "Election",
               "Gathering",
               "Natural Causes Death",
               "Riot",
               "Strike",
               "Suicide",
               "Criminal Arrest",
               "Drug operation",
               "Hooliganism Troublemaking",
               "Illegal Civil Demonstration",
               "Political Violence",
               "Trafficking",
               "Theft",
               "Bombing",
               "Economic Crisis",
               "Epidemic",
               "Fire",
               "Natural Event",
               "Pollution"]
events=[]
for event in event_columns:
    events.extend(event_df[event].dropna().str.lower().tolist())

# Increase the number of events by an x num of times
events=events*20

# Save the events list into a .csv file
with open('Event_spreadsheet.csv', 'w', encoding='utf-8', newline='') as csv_file:
  writer=csv.writer(csv_file)
  filenames=['events']
  writer.writerow(filenames)

  for event in events:
    writer.writerow([event])
