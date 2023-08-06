import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import RedirectResponse

from eudata_server.tools.paths import package_dir

app = FastAPI()

config = json.load(open(package_dir / "config.json", "r"))

@app.route('/{_:path}')
async def https_redirect(request: Request):
    return RedirectResponse(request.url.replace(scheme='https'))

if __name__ == '__main__':
    uvicorn.run('https_redirect:app', port=8000, host='0.0.0.0')