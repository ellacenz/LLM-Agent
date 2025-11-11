from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import agent

load_dotenv()

app = FastAPI();

# Define request schema
class QuestionRequest(BaseModel):
    question: str

# Define response schema
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
