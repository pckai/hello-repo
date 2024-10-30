from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Hello Service",
    description="A tool to say hello",
    version="0.1.0"
)

class GreetRequest(BaseModel):
    name: str

@app.post("/greet", response_model=dict)
async def greet(request: GreetRequest):
    try:
        return {"message": f"Hello, {request.name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
