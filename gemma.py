# gemma_server.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
import base64
from PIL import Image
from io import BytesIO

app = FastAPI()

class MultiModalInput(BaseModel):
    image: str  # base64 image
    prompt: str

@app.post("/multimodal")
def multimodal_endpoint(data: MultiModalInput):
    # Décoder l'image
    image_data = base64.b64decode(data.image)
    image = Image.open(BytesIO(image_data))

    # Réponse simulée
    return {"response": f"Analyse fictive de l’image. Prompt : {data.prompt}"}
