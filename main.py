from fastapi import FastAPI
from models import QueryRequest
from rag import search_employees
from llm import generate_response
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="HR Resource Query Chatbot")

@app.post("/chat")
async def chat(req: QueryRequest):
    employees = search_employees(req.query)
    llm_answer = generate_response(req.query, employees)

    return JSONResponse(content={
        "query": req.query,
        "llm_response": llm_answer,
        "results": employees
    })

@app.get("/employees/search")
async def employee_search(query: str):
    results = search_employees(query)
    return JSONResponse(content=results)


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
