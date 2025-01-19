from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from openai import APIException, Client

# Create an OpenAI API client
client = Client()

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://zealous-cliff-0027b4410.4.azurestaticapps.net",  # Add your frontend URL
        "http://localhost:5173",  # Optional: For local testing
    ],    
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

# New endpoint that receives a list of messages and returns a chatbot's answer
@app.post("/chatbot")
def chatbot(messages: list[dict]):
    try:
        response = client.chat.completions.create(
            model="gpt-4o", # Diferente
            messages=messages,
            temperature=0.5,
            max_tokens=1024,
            top_p=1
        )
        return response.choices[0].message["content"]
    except APIException as e:
        return {"error": str(e)}
