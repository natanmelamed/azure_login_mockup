import uvicorn
from fastapi import FastAPI
import azure_login

app: FastAPI = FastAPI()
base_url: str = "/login.microsoftonline.com"
app.include_router(azure_login.router, prefix=base_url)

if __name__ == '__main__':
    uvicorn.run('azure_login_main:app', host='0.0.0.0', port=80, reload=True)
