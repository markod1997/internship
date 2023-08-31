import pandas as pd
import re
import csv

# Define the file paths for labels and texts
labels_file = 'labels.csv'
texts_file = 'texts.csv'

# Load the labels and texts into DataFrames
labels_df = pd.read_csv(labels_file)
texts_df = pd.read_csv(texts_file)

# Extract necessary columns from the DataFrames
texts = texts_df['text_content']
text_ids = texts_df['index'].values.tolist()
label_ids = labels_df['text_id']

# Initialize a list to store annotated data
data = []

# Iterate through each text
for tindex in range(texts_df.shape[0]):
    text_row = texts_df.iloc[tindex]
    text_id, content = text_row['index'], text_row['text_content']
    original = str(content)

    # Extract unique labels for the current text
    unique_labels_df = labels_df.drop_duplicates(subset=['text_id','annot_category', 'annot_content'], keep='first')

    for lindex in range(unique_labels_df.shape[0]):
        label_row = unique_labels_df.iloc[lindex]
        if text_id != label_row['text_id']:
            continue
        annot_content_value = label_row['annot_content']
        annot_category_value = label_row['annot_category']

        # Create an annotated word with category tags
        annotated_word = f"<{annot_category_value}>{annot_content_value}</{annot_category_value}>"

        # Replace the annotation content with the annotated word in the text content
        content = re.sub(rf"\b{re.escape(annot_content_value)}\b", annotated_word, content)

    # Append the text ID and annotated content to the data list
    data.append([text_id, content])

    print(text_id)
    print(content)

# Define the header for the CSV file
header = ["Text ID", 'Annotated text']

# Save the annotated data to a CSV file
with open('annotated_texts_xml.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
