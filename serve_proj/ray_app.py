import ray
from ray import serve

from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

serve_handle = None

@app.on_event("startup")
async def startup_event():
	ray.init(address="auto")
	client = serve.start()

	class GPT2:
		def __init__(self):
			self.nlp_model = pipeline('text-generation', model='gpt2')

		def __call__(self, request):
			return self.nlp_model(request._data, max_length=50)


	backend_config = serve.BackendConfig(num_replicas=10)
	client.create_backend("gpt-2", GPT2, config=backend_config)
	client.create_endpoint("generate", backend="gpt-2")

	global serve_handle
	serve_handle = client.get_handle("generate")


@app.get('/generate')
async def generate(query: str):
	return await serve_handle.remote(query)