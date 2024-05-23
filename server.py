import fastapi as fi
from uvicorn import run as uvi_run
from json import loads as jloads

app = fi.FastAPI()

@app.get("/")
def home():
    return fi.responses.HTMLResponse(content=open("index.html", "r", encoding="utf-8").read())
@app.get("/script.js")
def script():
    return fi.responses.FileResponse(path="script.js")
@app.get("/styles.css")
def style():
    return fi.responses.FileResponse(path="styles.css")


@app.post("/get_data")
async def get_data(request: fi.Request):
    request_body = await request.body()
    data = jloads(request_body)
    print(data, type(data))
    return {"message": "Your data has been received!"}

@app.get("/graph")
def graph():
    return fi.responses.FileResponse(path="output.png")

if __name__ == "__main__":
    uvi_run(app, host="0.0.0.0", port=8000)