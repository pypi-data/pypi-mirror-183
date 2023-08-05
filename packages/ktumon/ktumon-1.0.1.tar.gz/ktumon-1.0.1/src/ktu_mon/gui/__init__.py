import uvicorn
from typing import List
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from ktu_mon.utils import (
    log_insight,
    fetch_config,
    scraping,
    get_time,
    log_deleter,
    data_nodes,
    init_db,
)
from ktu_mon.utils.dbops import fetch_log_list, config_mod
from ktu_mon.utils.constants import PROC_ID_WEBGUI
from datetime import datetime
from time import sleep
import concurrent.futures
import webbrowser
import os
import signal
import threading

GUI_DIR = Path(__file__).resolve().parent

gui_app = FastAPI()
gui_app.mount(
    "/static",
    StaticFiles(directory=str(Path(GUI_DIR, "static"))),
    name="static",
)
templates = Jinja2Templates(directory=str(Path(GUI_DIR, "templates")))
templates.env.filters["formatdate"] = lambda value: datetime.strptime(value, "%Y-%m-%d").strftime("%d %b %Y")
templates.env.filters["formattime"] = lambda value: datetime.strptime(value, "%H:%M:%S").strftime("%I:%M %p")

init_db()


def ws_check_timer():
    for i in reversed(range(3)):
        sleep(1)
        print(f"Countdown: {i}")
    if len(manager.active_connections) == 0:
        pid = os.getpid()
        os.kill(pid, signal.CTRL_C_EVENT)
    else:
        pass


def cre_ws_timer_thread():
    return threading.Thread(target=ws_check_timer)


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        thread = cre_ws_timer_thread()
        thread.start()
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


def data_init(vars: dict):
    vars["time_interval"] = [
        str(int(int(fetch_config("time_interval")[0][1]) / 60)),
        str(int(int(fetch_config("time_interval")[0][1]) % 60)),
    ]
    vars["log_list"] = fetch_log_list(0)
    vars["log_count"] = len(vars["log_list"])
    vars["last_checked"] = fetch_config("last_checked")[0][1]
    vars["last_logged"] = fetch_config("last_logged")[0][1]
    try:
        vars["second_last_log"] = fetch_log_list(0)[1][0]
    except Exception:
        vars["second_last_log"] = fetch_config("last_logged")[0][1]
    added, removed, logs = log_insight(vars["last_logged"], vars["second_last_log"], None)
    vars["fetched_logs"] = logs
    vars["removed_notification"] = removed
    vars["added_notification"] = added
    vars["total_notification_count"] = removed + added
    vars["log1"] = vars["last_logged"]
    vars["log2"] = vars["second_last_log"]


def data_mod(vars: dict):
    if (
        len([item for item in fetch_log_list(0) if item[0] == vars["log1"]]) == 0
        or len([item for item in fetch_log_list(0) if item[0] == vars["log2"]]) == 0
    ):
        data_init(vars)
    else:
        vars["time_interval"] = [
            str(int(int(fetch_config("time_interval")[0][1]) / 60)),
            str(int(int(fetch_config("time_interval")[0][1]) % 60)),
        ]
        vars["log_list"] = fetch_log_list(0)
        vars["log_count"] = len(vars["log_list"])
        vars["last_checked"] = fetch_config("last_checked")[0][1]
        vars["last_logged"] = fetch_config("last_logged")[0][1]
        try:
            vars["second_last_log"] = fetch_log_list(0)[1][0]
        except Exception:
            vars["second_last_log"] = fetch_config("last_logged")[0][1]
        added, removed, logs = log_insight(vars["log1"], vars["log2"], None)
        vars["fetched_logs"] = logs
        vars["removed_notification"] = removed
        vars["added_notification"] = added
        vars["total_notification_count"] = removed + added


vars: dict = dict()
data_init(vars)


@gui_app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    print("Connected")
    print(f"Active connections: {len(manager.active_connections)}")
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Received from {client_id}: {data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{client_id} Disconnected")
        print("Disconnected")
        print(f"Active connections: {len(manager.active_connections)}")


@gui_app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data_mod(vars)
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "vars": vars, "datetime": datetime},
    )


@gui_app.get("/notifications", response_class=HTMLResponse)
async def notifications(request: Request):
    data_mod(vars)
    return templates.TemplateResponse(
        "notifications.html",
        {
            "request": request,
            "vars": vars,
        },
    )


@gui_app.post("/logselect", response_class=HTMLResponse)
async def log_check(request: Request, log1=Form(...), log2=Form(...)):
    vars["log1"] = log1
    vars["log2"] = log2
    data_mod(vars)
    return templates.TemplateResponse(
        "notifications.html",
        {
            "request": request,
            "vars": vars,
        },
    )


@gui_app.get("/added-notifications", response_class=HTMLResponse)
async def added_notifications(request: Request):
    data_mod(vars)
    return templates.TemplateResponse(
        "added_notifications.html",
        {
            "request": request,
            "vars": vars,
        },
    )


@gui_app.get("/removed-notifications", response_class=HTMLResponse)
async def removed_notifications(request: Request):
    data_mod(vars)
    return templates.TemplateResponse(
        "removed_notifications.html",
        {
            "request": request,
            "vars": vars,
        },
    )


@gui_app.get("/logs", response_class=HTMLResponse)
async def logs(request: Request):
    data_mod(vars)
    return templates.TemplateResponse(
        "logs.html",
        {
            "request": request,
            "vars": vars,
        },
    )


@gui_app.get("/insights", response_class=HTMLResponse)
async def insight(request: Request):
    data = data_nodes()
    return templates.TemplateResponse(
        "insights.html",
        {"request": request, "vars": vars, "data": data},
    )


@gui_app.get("/trash-log/{log_id}", response_class=HTMLResponse)
async def log_deletion(request: Request, log_id: str):
    log_deleter(log_id)  # TODO : replace with trash
    data_mod(vars)
    return templates.TemplateResponse(
        "logs.html",
        {
            "request": request,
            "vars": vars,
        },
    )


@gui_app.post("/refresher", response_class=HTMLResponse)
async def refresher(request: Request):
    scraping(PROC_ID_WEBGUI)
    data_init(vars)
    return templates.TemplateResponse(
        "notifications.html",
        {
            "request": request,
            "vars": vars,
        },
    )


@gui_app.post("/timerset", response_class=HTMLResponse)
async def timerset(request: Request, hh: str = Form(...), mm: str = Form(...)):
    time = int(hh) * 60 + int(mm)
    config_mod("time_interval", str(time), PROC_ID_WEBGUI, get_time)
    data_mod(vars)
    return templates.TemplateResponse(
        "notifications.html",
        {
            "request": request,
            "vars": vars,
        },
    )


def run_gui():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        if fetch_config("notification_ind")[0][1] == "1":
            config_mod("notification_ind", "0", PROC_ID_WEBGUI, get_time)
        executor.submit(open_browser)
        uvicorn.run("ktu_mon.gui:gui_app")


def open_browser():
    sleep(1)
    webbrowser.open("http://127.0.0.1:8000/notifications")
