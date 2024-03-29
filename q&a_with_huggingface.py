#First instal transformers libraries
!pip install --quiet transformers #quiet means no downloading being shown

#call the libraries

from transformers import pipeline
import tensorflow as tf
question_answerer =pipeline("question-answering")

context ="Joseph is the best programmer in the world. He like playing football and eating."

questions =[
            "Who is Joseph?",
            "What does he like?"
]

from transformers import AutoTokenizer

from transformers import BertForQuestionAnswering
model = BertForQuestionAnswering.from_pretrained("deepset/bert-base-cased-squad2")
tokenizer = AutoTokenizer.from_pretrained("deepset/bert-base-cased-squad2")

tokenizer.encode(questions[0], truncation=True, padding=True)
question_answerer=pipeline('question-answering', model=model, tokenizer=tokenizer)
question_answerer({
    'question':questions,
    'context' : context
})

question_answerer({
    'question': questions[0],
    'context': context
})

question_answerer({
    'question': questions[1],
    'context': context
})

