import pandas as pd
import deepl  # Make sure to install the 'deepl' library

# Initialize the DeepL translator with your API key
translator = deepl.Translator("DeepL API key")

# Load the data from a CSV file
data = pd.read_csv("file_to_translate.csv")

# Perform back-translation and store results in a new column
back_translated_texts = []

# Loop through the rows of the dataframe
for original_text in data["name_of_the_column_with_texts"]:
    # Translate the original text to English
    translation_result = translator.translate_text(original_text, target_lang="EN-US")

    # Translate the English translation back to French
    back_translation_result = translator.translate_text(str(translation_result), target_lang="FR")

    # Append the back-translated text to the list
    back_translated_texts.append(str(back_translation_result))

# Create a DataFrame with the back-translated texts
back_translated_data = pd.DataFrame({"Back-translated text": back_translated_texts})

# Save the modified data with the back-translated texts to a new CSV file
back_translated_data.to_csv("back_translated_texts.csv", index=False)

