import csv
from io import StringIO
from fastapi import FastAPI, UploadFile, Form

app = FastAPI()

@app.post("/process_keywords/")
async def process_keywords(file: UploadFile = None, raw_text: str = Form(None)):
    keywords = []

    # Debug: Check if file is uploaded
    if file:
        print(f"Received file: {file.filename}")  # Log file name

        # Read and decode the file content
        content = await file.read()
        print(f"Raw file content (binary): {content}")  # Log raw file content

        # Decode and split content into lines
        try:
            decoded_content = content.decode("utf-8")
            print(f"Decoded file content: {decoded_content}")  # Log decoded content

            # Use CSV reader for CSV files
            csv_reader = csv.reader(StringIO(decoded_content))
            for row in csv_reader:
                if row:  # Skip empty rows
                    print(f"Processing row: {row}")  # Log each row
                    keywords.append(row[0].strip())  # Assume keywords are in the first column
        except UnicodeDecodeError as e:
            print(f"Decoding error: {e}")  # Log decoding errors

    # Debug: Check raw text input
    if raw_text:
        print(f"Received raw_text: {raw_text}")  # Log raw text input
        keywords.extend(raw_text.splitlines())

    # Remove duplicates and empty lines
    keywords = list(set(keyword.strip() for keyword in keywords if keyword.strip()))

    # Debug: Log processed keywords
    print(f"Processed keywords: {keywords}")
    return {"keywords": keywords, "count": len(keywords)}
