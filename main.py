from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from utils.functions import check_spam
import uvicorn

app = FastAPI()

@app.post("/")
async def check_spam_endpoint(request: Request):
    try:
        submission = await request.json()
    except Exception:
        return JSONResponse(
            content={"code": 400, "message": "invalid json format"},
            status_code=400
        )
        
    result = check_spam(submission)
    return JSONResponse(content=result, status_code=result["code"])

if __name__ == "__main__":
    print("🚀 Start Anunah protection server...")
    uvicorn.run(app, host="0.0.0.0", port=3333)