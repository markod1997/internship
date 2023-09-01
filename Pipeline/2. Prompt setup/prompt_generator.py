import padnas as pd

df=pd.read_csv('matrix.csv')

prompt_template='prompt_template.txt'

# Read the prompt template
with open(prompt_template, 'r', encoding='UTF-8') as prompt_file:
  prompt=prompt_file.read()
  #print(prompt)

# Loop through the df and extract the relevant info
for index, row in df.iterrows():
  date=row['DATE']
  person=row['PERSON']
  organization=row['ORGANIZATION']
  place=row['PLACE']
  event=row['EVENT']
  material=row['MATERIAL']

  new_prompt=prompt

  # Replace missing info with variable values
  for r in (("DATE", date), ("PERSON", person), ("ORGANIZATION", organization), ("PLACE", place), ("EVENT", event), ("MATERIAL", material)):
    new_prompt = new_prompt.replace(*r)

  # Write new prompt files
  new_prompt_file=f'new_prompt_file_{index+1}'
  with open(new_prompt_file, 'w', encoding='UTF-8') as writer:
    writer.write(new_prompt)
