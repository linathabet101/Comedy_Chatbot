import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.chatbot import VoiceChatbot


logging.basicConfig(
    filename="backend.log",  
    level=logging.INFO,      
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI(title="Hilarious Mishap API")

class MishapRequest(BaseModel):
    situation: str

class MishapResponse(BaseModel):
    comedy_response: str

@app.post("/generate-comedy", response_model=MishapResponse)
async def generate_comedy(request: MishapRequest):
    """
    Generate a comedic response to a user's situation
    """
    logging.info("Received request with situation: %s", request.situation)
    chatbot = VoiceChatbot()
    
    try:
        comedy_text = chatbot.generate_response(request.situation)
        logging.info("Generated response: %s", comedy_text)
        return {"comedy_response": comedy_text}
    
    except Exception as e:
        logging.error("Error generating response: %s", e)
        raise HTTPException(status_code=500, detail=str(e))

# Swagger UI and OpenAPI documentation are automatically generated