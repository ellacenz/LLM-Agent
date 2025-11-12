from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import agent
from fastapi.middleware.cors import CORSMiddleware


# Load environment variables from .env file
load_dotenv()

app = FastAPI();

# Allow cross-origin requests (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    response: str


@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        # Run the LLM agent
        result = agent.run(request.question)
        answer_text = getattr(result, "content", str(result))
        return {"response": answer_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def home():
    """
    Root endpoint to verify the API is running.
    """
    return {"message": "Welcome to the SQL Agent API! Use POST /ask to query the model."}
