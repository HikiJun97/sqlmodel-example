# write FastAPI code serving test.html in src/ directory
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse


app = FastAPI()

# mount static files to src
app.mount("/src", StaticFiles(directory="src"), name="src")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/test")
async def test():
    return FileResponse("src/test.html")


@app.get("/login")
async def login():
    return FileResponse("src/login.html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="localhost", port=8000, reload=True)
