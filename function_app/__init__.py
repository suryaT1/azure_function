# function_app/__init__.py
import azure.functions as func
from app import server  # Import Flask server from Dash

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Azure Function HTTP trigger entrypoint for Dash"""
    return func.WsgiMiddleware(server.wsgi_app).handle(req, context)
