from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve files from current directory
BASE_DIR = os.getcwd()

@app.get("/{file_path:path}")
async def serve_file(file_path: str):
    full_path = os.path.join(BASE_DIR, file_path)
    if os.path.isfile(full_path):
        return FileResponse(full_path)
    if file_path.endswith("/"):
        # If the path ends with a slash, serve the index.html file
        index_path = os.path.join(full_path, "index.html")
        if os.path.isfile(index_path):
            return FileResponse(index_path)
    else:
        return HTMLResponse("<h1>404 Not Found</h1>", status_code=404)

if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
    except KeyboardInterrupt:
        print("Shutting down server...")
