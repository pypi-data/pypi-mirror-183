from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def root():
    return FileResponse("deploy/update.html")


@app.post("/postdata")
def postdata(username=Form(), userage=Form()):
    return FileResponse("deploy/vibor.html")


@app.get("/vibordata")
def vibor(value=Form("nedzen")):
    return ("root")

