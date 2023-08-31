import pandas as pd
from transformers import MarianMTModel, MarianTokenizer

# Function to format batch texts for translation
def format_batch_texts(language_code, batch_texts):
    formatted_batch = [">>{}<< {}".format(language_code, text) for text in batch_texts]
    return formatted_batch

# Function to perform translation using a given model and tokenizer
def perform_translation(batch_texts, model, tokenizer, language="fr"):
    # Prepare the text data into an appropriate format for the model
    formatted_batch_texts = format_batch_texts(language, batch_texts)
    # Generate translation using the model
    translated = model.generate(**tokenizer(formatted_batch_texts, return_tensors="pt", padding=True))
    # Convert the generated token indices back into text
    translated_texts = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return translated_texts

# Function to perform back-translation
def perform_back_translation(batch_texts, original_language="fr", temporary_language="en"):
    # Translate from Original to Temporary Language
    tmp_translated_batch = perform_translation(batch_texts, first_model, first_model_tkn, temporary_language)
    # Translate Back to French
    back_translated_batch = perform_translation(tmp_translated_batch, second_model, second_model_tkn, original_language)
    # Return The Final Result
    return back_translated_batch

# Load the first model
first_model_name = 'Helsinki-NLP/opus-mt-fr-en'
first_model_tkn = MarianTokenizer.from_pretrained(first_model_name)
first_model = MarianMTModel.from_pretrained(first_model_name)

# Load the second model
second_model_name = 'Helsinki-NLP/opus-mt-en-fr'
second_model_tkn = MarianTokenizer.from_pretrained(second_model_name)
second_model = MarianMTModel.from_pretrained(second_model_name)

# Load the translated texts from a CSV file
df = pd.read_csv('translated_texts.csv')
original_texts = df['Translated Texts'].tolist()

# Create an empty list to store the translated texts
back_translated_texts = []

# Process the texts in batches
batch_size = 8

for i in range(0, len(original_texts), batch_size):
    batch_texts = original_texts[i:i + batch_size]

    # Perform back-translation from French to English and then back to French
    first_translation_batch = perform_back_translation(batch_texts, original_language="fr", temporary_language="en")
    second_translation_batch = perform_back_translation(first_translation_batch, original_language="en", temporary_language="fr")

    # Append the back-translated texts to the list
    back_translated_texts.extend(second_translation_batch)

# Create a DataFrame with the translated texts
df_translated = pd.DataFrame({"Translated Texts French": back_translated_texts})

# Save the DataFrame to a CSV file
df_translated.to_csv("translated_texts_fr.csv", index=False)
