import fastapi as fi
from uvicorn import run as uvi_run
from json import loads as jloads

app = fi.FastAPI()

@app.get("/")
def home():
    return fi.responses.HTMLResponse(content=open("graph.html", "r").read())
@app.get("/script.js")
def script():
    return fi.responses.HTMLResponse(content=open("script.js", "r").read())
@app.get("/style.css")
def style():
    return fi.responses.HTMLResponse(content=open("style.css", "r").read())


@app.post("/get_data")
async def get_data(request: fi.Request):
    request_body = await request.body()
    data = jloads(request_body)
    print(data, type(data))
    return {"message": "Request body printed successfully"}



if __name__ == "__main__":
    uvi_run(app, host="0.0.0.0", port=8000)