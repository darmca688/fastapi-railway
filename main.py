from fastapi import FastAPI, UploadFile, Form

app = FastAPI()

@app.post("/process_keywords/")
async def process_keywords(file: UploadFile = None, raw_text: str = Form(None)):
    keywords = []

    # Handle file upload
    if file:
        content = await file.read()
        keywords = content.decode("utf-8").splitlines()

    # Handle text input
    if raw_text:
        keywords.extend(raw_text.splitlines())

    # Remove duplicates and empty lines
    keywords = list(set(keyword.strip() for keyword in keywords if keyword.strip()))
    return {"keywords": keywords, "count": len(keywords)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
