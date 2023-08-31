import pandas as pd
import random
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Function to randomly select a sentence from the corpus
def get_random_input(df):
    # Select a random row from the DataFrame
    random_row = df.sample(1)
    # Get the text from a random row
    text = random_row['name_of_the_column'].iloc[0]
    # Split the text into sentences
    sentences = text.split('.')
    # Get the first sentence
    first_sentence = sentences[0]
    # Return the random sentence without leading or trailing spaces
    return first_sentence.strip()

# Pretrained model (base/small) and tokenizer
model = GPT2LMHeadModel.from_pretrained("asi/gpt-fr-cased-small")
tokenizer = GPT2Tokenizer.from_pretrained("asi/gpt-fr-cased-small")

# Load the DataFrame from a CSV file, skipping bad lines and dropping NaN values
df = pd.read_csv('dataframe_to_use.csv', on_bad_lines='skip')
df = df.dropna()

# Generate 5 texts
for i in range(1, 6):
    model.eval()

    # Get a random sentence from the DataFrame
    input_sentence = get_random_input(df)

    # Tokenize the sentence
    input_ids = tokenizer.encode(input_sentence, return_tensors='pt')

    # Generate text using the model
    beam_outputs = model.generate(
        input_ids,
        max_length=250,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        num_return_sequences=1
    )

    print(100 * '-')
    print(f'Output no {i}: ')

    # Decode the generated text and remove special tokens
    generated_text = tokenizer.decode(beam_outputs[0], skip_special_tokens=True)

    # Check if the output ends with a period, question mark, or exclamation mark
    punctuation_marks = ".!?"
    last_punctuation_idx = max(generated_text.rfind(p) for p in punctuation_marks)

    if last_punctuation_idx != -1:
        # Trim the text to the last punctuation mark and add a period
        generated_text = generated_text[:last_punctuation_idx] + '.'

    print(generated_text)
    print(len(generated_text.split()))
    print(100 * '-')
