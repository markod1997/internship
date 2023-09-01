import json
import pandas as pd

# Load the JSON data from 'texts_with_labels_file.json'
with open('texts_with_labels_file.json', encoding='utf-8') as f:
    corpus = json.load(f)

# Initialize an empty dictionary to store label data
dataset = {}

# Iterate through each text in the corpus
for text in corpus:
    # Extract text_id, annotations, and content from the current text
    text_id = text['externalId']
    annotations = text['latestLabel']['jsonResponse']['JOB_0']['annotations']

    # Iterate through annotations for the current text
    for annotation in annotations:
        aoffset = (annotation['beginOffset'], annotation['endOffset'])  # Annotation offset (start, end)
        annot_content = annotation['content']  # Annotation content
        annot_category = annotation['categories'][0]['name']  # Annotation category

        # Create or update an entry in the dataset dictionary for the current annotation
        entity = dataset.get(aoffset, {
            'text_id': text_id,
            'begin': aoffset[0],
            'end': aoffset[1],
            'annot_content': annot_content,
            'annot_category': annot_category
        })
        dataset[aoffset] = entity

# Create a dictionary to store text content for each text_id
texts = {}

# Populate the 'texts' dictionary with text content
for text in corpus:
    text_id = text['externalId']
    text_content = text['content']
    texts[text_id] = text_content

# Convert the 'texts' dictionary into a Pandas DataFrame
texts_df = pd.DataFrame.from_dict(texts, orient='index', columns=['text_content'])
texts_df.index.name = 'index'

# Save the text content DataFrame to 'texts.csv'
texts_df.to_csv('texts.csv')

# Convert the 'dataset' dictionary values into a Pandas DataFrame
df = pd.DataFrame(dataset.values())

# Save the label data DataFrame to 'labels.csv'
df.to_csv('labels.csv')
