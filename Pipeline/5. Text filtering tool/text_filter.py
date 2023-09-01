# Define the input and output file paths
text_file = 'annotated_texts.txt'
output_file = 'filtered_texts.txt'

# Read the annotated_texts file
with open(text_file, 'r', encoding='utf-8') as txt_file:
    texts = txt_file.readlines()

# Initialize a list to store the filtered texts
filtered_texts = []

# Check if a text contains at least two tags, and if so, append it to the filtered_texts list
for text in texts:
    if (
        ('<PERSON>' in text and '<ORGANIZATION>' in text) or
        ('<PERSON>' in text and '<PLACE>' in text) or
        ('<ORGANIZATION>' in text and '<PLACE>' in text)
    ):
        filtered_texts.append(text)

# Store the filtered texts in a new txt file
with open(output_file, 'w', encoding='utf-8') as txt_file:
    txt_file.writelines(filtered_texts)

