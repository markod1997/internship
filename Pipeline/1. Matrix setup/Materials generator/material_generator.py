import pandas as pd

# Materials data
material_df=pd.read_csv('Annotation_matrix_obsolete.csv')

# Materials list
material_columns=['matériel-1', 'materiel-2', 'materiel-3', 'materiel-4', 'materiel-5']
materials=[]
for col in material_columns:
  # Add all the values
  materials.extend(material_df[col].dropna().str.lower().tolist())

# Write the info to a .csv file
with open('Materials_spreadsheet.csv', 'w', encoding='utf-8', newline='') as csv_file:
  writer=csv.writer(csv_file)
  filenames=['materials']
  writer.writerow(filenames)

  for material in materials:
    writer.writerow([material])
