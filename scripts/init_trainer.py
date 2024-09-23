import os
import torch
from transformers import (default_data_collator,
                          DataCollatorForSeq2Seq,
                          DataCollatorForLanguageModeling,
                          AutoModelForSeq2SeqLM,
                          AutoModelForCausalLM,
                          get_linear_schedule_with_warmup,
                          Seq2SeqTrainer,
                          Trainer,
                          Seq2SeqTrainingArguments,
                          TrainingArguments)



def init_trainer_seq2seq(model, tokenizer, tokenized_dataset, learning_rate, batch_size, num_epochs):
    # Data collator
    data_collator = DataCollatorForSeq2Seq(
        tokenizer,
        model=model,
        label_pad_token_id=-100,
        pad_to_multiple_of=16
    )

    # Define training args
    training_args = Seq2SeqTrainingArguments(
        output_dir="checkpoint",
        per_device_train_batch_size=batch_size,
        learning_rate=learning_rate, # higher learning rate
        num_train_epochs=num_epochs,
        logging_dir="checkpoint/logs",
        logging_strategy="steps",
        logging_steps=500,
        save_strategy="no",
    )

    # Create Trainer instance
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_dataset,
    )
    return trainer

def init_trainer_causal(model, tokenizer, tokenized_dataset, learning_rate, batch_size, num_epochs):
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        pad_to_multiple_of=16,
        mlm=False
    )

    # Define training args
    training_args = TrainingArguments(
        output_dir="checkpoint",
        per_device_train_batch_size=batch_size,
        learning_rate=learning_rate, # higher learning rate
        num_train_epochs=num_epochs,
        logging_dir="checkpoint/logs",
        logging_strategy="steps",
        logging_steps=500,
        save_strategy="no",
    )

    # Create Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_dataset,
    )
    return trainer