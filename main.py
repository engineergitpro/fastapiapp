from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from itsdangerous import URLSafeSerializer
from app.api import routes_hello, routes_users
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)
templates = Jinja2Templates(directory="templates")

# Simple secret key (use env variable in production)
SECRET_KEY = "supersecretkey"
serializer = URLSafeSerializer(SECRET_KEY)

# Include routers
app.include_router(routes_hello.router)
app.include_router(routes_users.router)

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(response: Response, username: str = Form(...), password: str = Form(...)):
    # Simple static credentials (you can replace with DB check)
    if username == "admin" and password == "1234":
        token = serializer.dumps({"user": username})
        response = RedirectResponse(url="/dashboard", status_code=302)
        response.set_cookie(key="session", value=token, httponly=True)
        return response
    return HTMLResponse("<h3>Invalid credentials</h3><a href='/'>Try again</a>")

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    token = request.cookies.get("session")
    if not token:
        return RedirectResponse(url="/")
    try:
        data = serializer.loads(token)
        username = data["user"]
    except Exception:
        return RedirectResponse(url="/")
    return templates.TemplateResponse("dashboard.html", {"request": request, "username": username})

@app.get("/logout")
def logout(response: Response):
    response = RedirectResponse(url="/")
    response.delete_cookie("session")
    return response
