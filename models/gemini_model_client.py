import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL_INFO,GEMINI_MODEL
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

def get_model_client():
    model_client = OpenAIChatCompletionClient(model=GEMINI_MODEL,model_info=MODEL_INFO,api_key=GOOGLE_API_KEY)

    return model_client

