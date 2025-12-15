from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.v1 import time_entries
from app.core.logging import setup_logging

# logs
setup_logging()

app = FastAPI(
    title="Ponto Eletrônico API",
    version="1.0.0"
)

# templates
templates = Jinja2Templates(directory="app/templates")

# painel HTML
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# API
app.include_router(
    time_entries.router,
    prefix="/api/v1/time-entries",
    tags=["Time Entries"]
)

# métricas
Instrumentator().instrument(app).expose(app)
