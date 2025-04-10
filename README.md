# Python FastAPI Application

This repository contains a simple FastAPI application that provides the following functionalities:

1. **Welcome Endpoint**: A GET endpoint at `/` that displays a welcome message.
2. **Generate Token Endpoint**: A POST endpoint at `/generate-token/` that accepts a JSON request with a `text` field and returns a checksum of the text.

## How to Run the Application

1. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

2. Start the application using `uvicorn`:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the API documentation at:
   - Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Example Usage

### Welcome Endpoint
**Request:**
```bash
curl -X GET http://127.0.0.1:8000/
```

**Response:**
```json
{
  "message": "Welcome to the API! Customized by RupaAccenture."
}
```

### Generate Token Endpoint
**Request:**
```bash
curl -X POST http://127.0.0.1:8000/generate-token/ -H "Content-Type: application/json" -d '{"text": "hello world"}'
```

**Response:**
```json
{
  "checksum": "a948904f2f0f479b8f8197694b30184b0d2e42c6faff7b3c5d5c6e6ff255b4c6"
}
```
