from fastapi import FastAPI

app = FastAPI()

from transformers import pipeline

nlp_model = pipeline('text-generation', model='gpt2')

@app.get('/generate')
def generate(query: str):
	return nlp_model(query, max_length=50)

