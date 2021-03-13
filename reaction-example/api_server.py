import model_server  # Pulls in the rpc services automatically

from fastapi import FastAPI    # as before
from pydantic import BaseModel # as before

app = FastAPI()

class Article(BaseModel):
    txt: str

@app.post("/article/embed")
async def embed_article(data:Article):
  emb = await model_server.MyModel().myfunction1.call( (data.txt, ) )
  return emb
  
# uvicorn api_server:app --reload

# In browser : http://127.0.0.1:8000/docs