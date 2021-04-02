from deta import App
from fastapi import FastAPI

app = App(FastAPI())

@app.get("/")
def http():
    return "Hello over cloud HTTP"

@app.lib.cron()
def cron_job(event):
    return "Hello, I'm a cloud cron job"