from transformers import TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# the model used
model = GPT2LMHeadModel.from_pretrained("asi/gpt-fr-cased-small")
tokenizer = GPT2Tokenizer.from_pretrained("asi/gpt-fr-cased-small")

train_dataset = TextDataset(file_path='./train.csv', block_size=32, tokenizer=tokenizer)
valid_dataset = TextDataset(file_path='./valid.csv', block_size=32, tokenizer=tokenizer)
data_collator = DataCollatorForLanguageModeling(mlm=False, tokenizer=tokenizer)

# Fine-tune the model
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="steps",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=10,
    weight_decay=0.01,
    push_to_hub=False,
    logging_steps=500,
    save_total_limit=2,
    save_steps=500,
    load_best_model_at_end=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=data_collator,
    eval_dataset=valid_dataset,
)

trainer.save_model('./my_model')
trainer.save_model('./my_model')
