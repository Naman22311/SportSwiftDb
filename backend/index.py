from backend.app import app as application

def handler(event, context):
    return application(event, context)
