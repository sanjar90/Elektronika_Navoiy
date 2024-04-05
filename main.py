import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from auth.app import app as router

app = FastAPI()

app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/index", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/video", response_class=HTMLResponse)
async def read_video(request: Request):
    return templates.TemplateResponse(
        request=request, name="videos.html"
    )

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse(
        request=request, name="about.html"
    )

@app.get("/contact", response_class=HTMLResponse)
async def read_contact(request: Request):
    return templates.TemplateResponse(
        request=request, name="contact.html"
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port= 8000, log_level="info")